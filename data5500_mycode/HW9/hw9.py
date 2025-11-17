# Ethan Westenskow

### Fetch Prices ###
#__________________________________________________________________________________________________
#Live API Call
import requests
import json 

def get_prices():
    #--Andy's URL (Chat said there was a problem with it.)
    # url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,ada,btc,eos" 
   
   #--ChatGPT gave me this corrected URL. 
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,ada,bch,eos"
    response = requests.get(url)
    # verify the response is OK
    if response.status_code == 200:
        prices_dict = response.json()
        return prices_dict
    else:
        print("Request failed: ", response.status_code)
        return None


prices_dict = {'bitcoin': {'eth': 30.723109, 'btc': 1.0, 'ltc': 999.622, 'xrp': 43089, 'bch': 185.875, 'eos': 395413}, 'bitcoin-cash': {'eth': 0.16526781, 'btc': 0.00538153, 'ltc': 5.376796, 'xrp': 231.673, 'bch': 1.0, 'eos': 2127}, 'cardano': {'eth': 0.00015399, 'btc': 5.01e-06, 'ltc': 0.00500998, 'xrp': 0.2158675, 'bch': 0.00093114, 'eos': 1.982239}, 'eos': {'eth': 7.772e-05, 'btc': 2.53e-06, 'ltc': 0.00252858, 'xrp': 0.10899587, 'bch': 0.00047018, 'eos': 1.0}, 'ethereum': {'eth': 1.0, 'btc': 0.0325611, 'ltc': 32.539272, 'xrp': 1403, 'bch': 6.050533, 'eos': 12871}, 'litecoin': {'eth': 0.03073081, 'btc': 0.00100067, 'ltc': 1.0, 'xrp': 43.07853, 'bch': 0.18581929, 'eos': 395.576}, 'ripple': {'eth': 0.00071292, 'btc': 2.321e-05, 'ltc': 0.02319401, 'xrp': 1.0, 'bch': 0.00431079, 'eos': 9.176902}}
# prices_dict = get_prices() #uncomment this to get live api calls

### BUILD THE GRAPH ###
#__________________________________________________________________________________________________
import networkx as nx 

def build_graph(prices_dict):
    # 1. create a directed graph
    g = nx.DiGraph()
    # 2. mapping from coin id (JSON outer key) to ticker (node name)
    id_to_ticker = {
        "bitcoin": "btc",
        "ethereum": "eth",
        "litecoin": "ltc",
        "ripple": "xrp",
        "cardano": "ada",
        "bitcoin-cash": "bch",
        "eos": "eos"
    }
    # 3. loop through the JSON and add edges
    for coin_id, vs_dict in prices_dict.items():
        from_ticker = id_to_ticker[coin_id]
        for to_ticker, rate in vs_dict.items():
            if rate is None:
                continue
            g.add_weighted_edges_from([(from_ticker, to_ticker, rate)])
    # 4. return the graph
    return g

g = build_graph(prices_dict)


## LEFT OFF AT GRAPH BEING BUILT. 
#We've built -fetching the prices -building the graph






