# Import Modules
import os
from datetime import datetime
import requests
import json
import networkx as nx

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
RESULTS_FILE = "results.json"  # (we'll use this later for results)

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
    Adapted from your original function.
    Instead of just printing everything, we return a summary dict.
    """
    nodes = list(g.nodes)

    min_factor = float('inf')
    max_factor = 0.0
    min_paths = None
    max_paths = None

    interesting_cycles = []

    for source in nodes:
        for target in nodes:
            if source == target:
                continue

            for forward_path in nx.all_simple_paths(g, source, target):
                reverse_path = list(reversed(forward_path))

                forward_weight = compute_path_weight(g, forward_path)
                reverse_weight = compute_path_weight(g, reverse_path)

                if forward_weight is None or reverse_weight is None:
                    continue

                factor = forward_weight * reverse_weight

                # Track best / worst
                if factor < min_factor:
                    min_factor = factor
                    min_paths = (forward_path, reverse_path)

                if factor > max_factor:
                    max_factor = factor
                    max_paths = (forward_path, reverse_path)

                # Store cycles that are meaningfully away from 1
                if factor > 1.01 or factor < 0.99:
                    interesting_cycles.append({
                        "forward_path": forward_path,
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


if __name__ == "__main__":
    main()