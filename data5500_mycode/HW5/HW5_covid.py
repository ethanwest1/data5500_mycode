# Ethan Westenskow

#read in the state list and turn it into a list.
def state_list():  
    with open("data5500_mycode/HW5/states_territories.txt", "r") as file:
        lines = file.readlines()
    state_codes = [line.strip() for line in lines]
    return state_codes







#### I've got the state list read in, it's ready for me to pull from the api and use a for loop to pull data for each state. 



# import requests
# import json

# # example url to query datamuse web json api
# example_url = "https://api.datamuse.com/words?ml=duck"

# # variables to query 
# word = 'duck'
# key_word = "word"
# key_score = "score"
# search_word = "mallard"

# #generate url
# url = 'https://api.datamuse.com/words?ml=' + word
# print(url)

# # requests stock data from data muse
# request = requests.get(url)
# # print(request.text) # print to double check data from web json api is good
# dct_full = json.loads(request.text)


