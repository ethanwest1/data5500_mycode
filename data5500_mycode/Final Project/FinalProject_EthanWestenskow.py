# Import Modules
import os
from datetime import datetime
import requests
import json
import networkx as nx
from itertools import permutations

import warnings
warnings.filterwarnings("ignore")

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
CURRENCIES = {
    "bitcoin": "btc",
    "ethereum": "eth",
    "litecoin": "ltc",
    "ripple": "xrp",
    "cardano": "ada",
    "bitcoin-cash": "bch",
    "eos": "eos",
    "solana": "sol",
    "polkadot": "dot",
    "chainlink": "link",
    "uniswap": "uni",
    "avalanche-2": "avax",
    "stellar": "xlm",
}

VS_CURRENCY = "usd"         # we fetch everything vs USD
DATA_DIR = "/home/ubuntu/data5500_mycode/Final Project/data"            # folder for pair files
RESULTS_FILE = "/home/ubuntu/data5500_mycode/Final Project/results.json"

# ---------------- RESULTS FILE HELPERS ----------------

def load_results():
    """
    Load all past run results from results.json, or return an empty list
    if the file doesn't exist or is invalid.
    """
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_results(all_results):
    """
    Save the list of all run results back to results.json, nicely formatted.
    """
    with open(RESULTS_FILE, "w") as f:
        json.dump(all_results, f, indent=2)

# ---------------- ALPACA CONFIG ----------------

ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_ORDERS_ENDPOINT = f"{ALPACA_BASE_URL}/v2/orders"

# Read keys from environment variables (so they aren't hard-coded)
ALPACA_API_KEY_ENV = "ALPACA_API_KEY_ID"
ALPACA_SECRET_KEY_ENV = "ALPACA_API_SECRET_KEY"

# Our tickers that Alpaca can trade as crypto/USD pairs
ALPACA_SYMBOL_MAP = {
    "btc": "BTC/USD",
    "eth": "ETH/USD",
    "ltc": "LTC/USD",
    "xrp": "XRP/USD",
    "bch": "BCH/USD",
    "sol": "SOL/USD",
    "dot": "DOT/USD",
    "link": "LINK/USD",
    "uni": "UNI/USD",
    "avax": "AVAX/USD",
}

# ---------------- ALPACA ORDER HELPERS ----------------

def get_alpaca_credentials():
    """
    Read Alpaca credentials from environment variables.
    If they aren't set, print a warning and skip live trades.
    """
    api_key = os.environ.get(ALPACA_API_KEY_ENV)
    secret_key = os.environ.get(ALPACA_SECRET_KEY_ENV)
    if not api_key or not secret_key:
        print("Alpaca API keys not set in environment; skipping live paper trades.")
        return None, None
    return api_key, secret_key


def submit_alpaca_order(symbol, side="buy", notional=None, qty=None,
                        order_type="market", time_in_force="gtc"):
    """
    Submit a crypto order to Alpaca's PAPER endpoint.
    Uses notional (USD value) by default, or qty if provided.
    Returns parsed JSON or an error dict.
    """
    api_key, secret_key = get_alpaca_credentials()
    if api_key is None:
        # No keys set; skip placing real orders
        return None

    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "Content-Type": "application/json",
    }

    body = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "time_in_force": time_in_force,
    }

    if notional is not None:
        body["notional"] = str(notional)
    elif qty is not None:
        body["qty"] = str(qty)
    else:
        raise ValueError("Either notional or qty must be provided")

    try:
        resp = requests.post(ALPACA_ORDERS_ENDPOINT, headers=headers, json=body, timeout=10)
        if resp.status_code not in (200, 201):
            print("Alpaca order failed:", resp.status_code, resp.text)
            return {
                "error": True,
                "status_code": resp.status_code,
                "body": resp.text,
                "request": body,
            }
        return resp.json()
    except Exception as e:
        print("Error submitting Alpaca order:", e)
        return {
            "error": True,
            "exception": str(e),
            "request": body,
        }


def place_alpaca_trades_from_cycles(interesting_cycles, notional_per_trade=10.0, max_trades=3):
    """
    Take 'interesting_cycles' from analyze_arbitrage(g)
    and place up to max_trades paper orders on Alpaca.

    Simple strategy:
    - For each cycle, use the FIRST coin in forward_path.
    - If that coin has a USD pair on Alpaca, buy `notional_per_trade` of it.
    - Record the orders so we can log them in results.json.
    """
    orders = []
    trade_count = 0

    for cycle_info in interesting_cycles:
        if trade_count >= max_trades:
            break

        forward_path = cycle_info["forward_path"]
        if not forward_path:
            continue

        first_coin = forward_path[0]  # e.g. "btc"
        ticker = str(first_coin).lower()

        symbol = ALPACA_SYMBOL_MAP.get(ticker)
        if not symbol:
            # This coin isn't tradable on Alpaca in USD
            continue

        print(f"Placing Alpaca paper trade: BUY {notional_per_trade} USD of {symbol} "
              f"based on cycle {forward_path} (factor={cycle_info['factor']:.4f})")

        order_resp = submit_alpaca_order(
            symbol=symbol,
            side="buy",
            notional=notional_per_trade,
            order_type="market",
            time_in_force="gtc",
        )

        orders.append({
            "cycle": forward_path,
            "factor": cycle_info["factor"],
            "alpaca_symbol": symbol,
            "notional_usd": notional_per_trade,
            "order_response": order_resp,
        })

        trade_count += 1

    return orders


# ---------------- DATA FETCH & PAIR FILE ----------------

def fetch_usd_prices():
    """
    Calls CoinGecko and returns a dict:
    { 'bitcoin': 12345.67, 'ethereum': 2345.67, ... } in USD
    """
    ids = ",".join(CURRENCIES.keys())
    params = {
        "ids": ids,
        "vs_currencies": VS_CURRENCY
    }

    response = requests.get(COINGECKO_API_URL, params=params, timeout=10)

    if response.status_code != 200:
        print("Request failed:", response.status_code, response.text)
        return None

    data = response.json()
    prices_usd = {}

    for cg_id in CURRENCIES.keys():
        coin_entry = data.get(cg_id)
        if coin_entry is None:
            print(f"Warning: no data for {cg_id}")
            continue
        price = coin_entry.get(VS_CURRENCY)
        prices_usd[cg_id] = price

    return prices_usd


def build_pair_rates(prices_usd):
    """
    Given USD prices, compute all pairwise exchange rates.
    Returns a list of tuples: (from_symbol, to_symbol, rate)
    where rate = price_usd[from] / price_usd[to].
    """
    pair_rates = []
    cg_ids = list(CURRENCIES.keys())

    for from_id in cg_ids:
        for to_id in cg_ids:
            if from_id == to_id:
                continue

            price_from = prices_usd.get(from_id)
            price_to = prices_usd.get(to_id)

            if price_from is None or price_to is None:
                continue
            if price_to == 0:
                continue

            rate = price_from / price_to

            from_symbol = CURRENCIES[from_id]
            to_symbol = CURRENCIES[to_id]

            pair_rates.append((from_symbol, to_symbol, rate))

    return pair_rates


def save_pair_file(pair_rates):
    """
    Save to data/currency_pair_YYYY.MM.DD:HH.MM.txt
    with header: currency_from,currency_to,exchange_rate
    """
    # Make sure the data folder exists
    os.makedirs(DATA_DIR, exist_ok=True)

    now = datetime.utcnow()
    filename = now.strftime("currency_pair_%Y.%m.%d:%H.%M.txt")
    path = os.path.join(DATA_DIR, filename)

    with open(path, "w") as f:
        f.write("currency_from,currency_to,exchange_rate\n")
        for cur_from, cur_to, rate in pair_rates:
            f.write(f"{cur_from},{cur_to},{rate}\n")

    return path


def get_latest_data():
    """
    1. Fetch USD prices from CoinGecko
    2. Build pair rates
    3. Save them to a timestamped file

    Returns: (prices_usd, pair_rates, file_path)
    """
    prices_usd = fetch_usd_prices()
    if prices_usd is None:
        raise RuntimeError("Failed to fetch prices")

    pair_rates = build_pair_rates(prices_usd)
    file_path = save_pair_file(pair_rates)

    return prices_usd, pair_rates, file_path

# ---------------- GRAPH & ARBITRAGE ANALYSIS ----------------

def build_graph_from_pairs(pair_rates):
    """
    pair_rates: list of (from_symbol, to_symbol, rate)
    Returns a directed graph with edge weights = rate.
    """
    g = nx.DiGraph()
    for cur_from, cur_to, rate in pair_rates:
        if rate is None:
            continue
        g.add_weighted_edges_from([(cur_from, cur_to, rate)])
    return g


def compute_path_weight(g, path):
    """
    Multiply weights along the path.
    Returns None if any edge is missing.
    """
    weight = 1.0

    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]

        if to_node not in g[from_node]:
            return None

        edge_weight = g[from_node][to_node]['weight']
        weight *= edge_weight

    return weight



def analyze_arbitrage(g):
    """
    Look for arbitrage opportunities using only 3-coin (triangle) cycles.
    This avoids the explosion from all_simple_paths on a dense 13-node graph.

    For each distinct triple of nodes (a, b, c), we consider all 6 possible
    directed 3-cycles (permutations). For each cycle, we compute:

        forward_weight  = product of edge weights around the cycle
        reverse_weight  = product around the reversed cycle
        factor          = forward_weight * reverse_weight

    If factor is meaningfully away from 1.0, we consider it an "interesting" cycle.
    We also track the smallest and largest factors overall.
    """
    nodes = list(g.nodes)
    n = len(nodes)

    min_factor = float('inf')
    max_factor = 0.0
    min_paths = None
    max_paths = None

    interesting_cycles = []

    # Iterate over all combinations of 3 distinct indices
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = nodes[i], nodes[j], nodes[k]

                # Consider all 6 permutations of (a, b, c) as directed 3-cycles
                for perm in permutations([a, b, c], 3):
                    cycle = list(perm) + [perm[0]]  # e.g. [a, b, c, a]
                    forward_weight = compute_path_weight(g, cycle)
                    reverse_path = list(reversed(cycle))
                    reverse_weight = compute_path_weight(g, reverse_path)

                    if forward_weight is None or reverse_weight is None:
                        continue

                    factor = forward_weight * reverse_weight

                    # Track global min/max factors and their paths
                    if factor < min_factor:
                        min_factor = factor
                        min_paths = (cycle, reverse_path)

                    if factor > max_factor:
                        max_factor = factor
                        max_paths = (cycle, reverse_path)

                    # Store cycles that are meaningfully away from 1
                    if abs(factor - 1.0) > 0.01:
                        interesting_cycles.append({
                            "forward_path": cycle,
                            "reverse_path": reverse_path,
                            "forward_weight": forward_weight,
                            "reverse_weight": reverse_weight,
                            "factor": factor,
                        })

    summary = {
        "min_factor": min_factor,
        "min_paths": min_paths,
        "max_factor": max_factor,
        "max_paths": max_paths,
        "interesting_cycles": interesting_cycles,
    }

    return summary


def main():
    # 1. Get latest data & save pair file
    prices_usd, pair_rates, pair_file_path = get_latest_data()
    print(f"Saved pair data to: {pair_file_path}")

    # 2. Build graph from pair rates
    g = build_graph_from_pairs(pair_rates)
    print(f"Graph has {len(g.nodes())} nodes and {len(g.edges())} edges.")

    # 3. Run arbitrage analysis
    summary = analyze_arbitrage(g)
    print("\nMin factor:", summary["min_factor"])
    print("Max factor:", summary["max_factor"])
    print("Number of interesting cycles:", len(summary["interesting_cycles"]))

    # 4. Place Alpaca paper trades based on interesting cycles
    alpaca_orders = place_alpaca_trades_from_cycles(
        summary["interesting_cycles"],
        notional_per_trade=10.0,   # you can tweak this amount
        max_trades=3,              # cap trades per run
    )
    print(f"Placed {len(alpaca_orders)} Alpaca paper trades.")

    # 5. Append this run to results.json
    all_results = load_results()
    run_entry = {
        "timestamp_utc": datetime.utcnow().isoformat(),
        "pair_file": pair_file_path,
        "prices_usd": prices_usd,
        "arbitrage_summary": {
            "min_factor": summary["min_factor"],
            "min_paths": summary["min_paths"],
            "max_factor": summary["max_factor"],
            "max_paths": summary["max_paths"],
            "num_interesting_cycles": len(summary["interesting_cycles"]),
        },
        "alpaca_orders": alpaca_orders,
    }
    all_results.append(run_entry)
    save_results(all_results)

if __name__ == "__main__":
    main()