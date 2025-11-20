# Ethan Westenskow

### Fetch Prices ###
#__________________________________________________________________________________________________
#Live API Call
import requests
import json 

#fetches live data from coingecko - returns a python dict with rates 
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

# #ada debugging
# prices_dict = get_prices()
# print()
# print("Top-level keys from API:", prices_dict.keys())
# print()
# print("\ncardano entry from API:", prices_dict.get("cardano"))

#use this in case you run out of api calls. (If it's uncommented, that's okay, the variable will be overrided.)
# prices_dict = {'bitcoin': {'eth': 30.723109, 'btc': 1.0, 'ltc': 999.622, 'xrp': 43089, 'bch': 185.875, 'eos': 395413}, 'bitcoin-cash': {'eth': 0.16526781, 'btc': 0.00538153, 'ltc': 5.376796, 'xrp': 231.673, 'bch': 1.0, 'eos': 2127}, 'cardano': {'eth': 0.00015399, 'btc': 5.01e-06, 'ltc': 0.00500998, 'xrp': 0.2158675, 'bch': 0.00093114, 'eos': 1.982239}, 'eos': {'eth': 7.772e-05, 'btc': 2.53e-06, 'ltc': 0.00252858, 'xrp': 0.10899587, 'bch': 0.00047018, 'eos': 1.0}, 'ethereum': {'eth': 1.0, 'btc': 0.0325611, 'ltc': 32.539272, 'xrp': 1403, 'bch': 6.050533, 'eos': 12871}, 'litecoin': {'eth': 0.03073081, 'btc': 0.00100067, 'ltc': 1.0, 'xrp': 43.07853, 'bch': 0.18581929, 'eos': 395.576}, 'ripple': {'eth': 0.00071292, 'btc': 2.321e-05, 'ltc': 0.02319401, 'xrp': 1.0, 'bch': 0.00431079, 'eos': 9.176902}}

#Use this to get live api calls
prices_dict = get_prices() 


### BUILD THE GRAPH ###
#__________________________________________________________________________________________________
import networkx as nx 

#create a directed graph of all our coins and their rates
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

# #ada debugging
# print("\n\n\n\n")
# print("\nNodes in graph:", list(g.nodes()))
# print()
# print("Edges *from* ada:", list(g.out_edges('ada', data=True)))
# print()
# print("Edges *to* ada:", list(g.in_edges('ada', data=True)))

#Running through all paths and finding disequilibrium
#__________________________________________________________________________________________________
#takes the graph (g) and a list of nodes (a path) - multiplies all the edge weights along that path to return the total exchange rate for that path.
def compute_path_weight(g,path):
    weight = 1.0

    for i in range(len(path)-1):
        from_node = path[i]
        to_node = path[i+1]

        #if edge doesn't exist, this path isn't valid in this direction. 
        if to_node not in g[from_node]:
            return None

        edge_weight = g[from_node][to_node]['weight']

        weight = weight * edge_weight
    return weight


def analyze_arbitrage(g):
    nodes = list(g.nodes)

    #tracks best/worst arbitrage
    min_factor = float('inf') #this garuntees that any value we find is greater than what we set this to originally. 
    max_factor = 0.0 #factors will always be positive so we can safely set this to 0.0
    min_paths = None #tuple (forward & reversed paths)
    max_paths = None #tuple (forward & reversed paths)

    #loop over all ordered currency pairs
    for source in nodes:
        for target in nodes:
            if source == target:
                continue #we continue because if the source and target coins are the same, then we can't find arbitrage because there is no trading.
            print(f"\npaths from {source} to {target}----------------------------------")

            #we identify the arbitrage in this loop. we find both the forward and reverse paths, multiply them together, and find our max/min factors. 
            for forward_path in nx.all_simple_paths(g, source, target):
                reverse_path = list(reversed(forward_path)) #we find the reverse path by simply reversing our forward path

                #compute weights for both paths (forward & reversed)
                forward_weight = compute_path_weight(g, forward_path)
                reverse_weight = compute_path_weight(g, reverse_path)

                # if either direction isn't a valid path, skip it
                if forward_weight is None or reverse_weight is None:
                    continue

                #mulitply to find dis-equilibrium
                factor = forward_weight * reverse_weight

                #print results
                print(forward_path, "Weight: ", forward_weight)
                print(reverse_path, "Weight: ", reverse_weight)
                print("Factor: ", factor)
                print()

        

                #Update max/min factors (best/worst arbitrage)
                if factor < min_factor:
                    min_factor = factor
                    min_paths = (forward_path, reverse_path)

                if factor > max_factor:
                    max_factor = factor
                    max_paths = (forward_path, reverse_path)

    #Final Summary of arbitrage
    print("\nSmallest Paths weight factor:", min_factor)
    print("Paths:", "\n", min_paths[0], "\n",min_paths[1])

    print("\nGreatest Paths weight factor:", max_factor)
    print("Paths:", "\n",max_paths[0],"\n", max_paths[1])


analyze_arbitrage(g)

