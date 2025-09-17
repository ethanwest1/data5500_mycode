# Ethan Westenskow

#Steps to work with jsons:
# 1. Put url in browser
# 2. Stare at int
# 3. Find keys 
# 4. Write the code


'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

import requests
import json

# example url to query datamuse web json api
example_url = "https://api.datamuse.com/words?ml=duck"

# variables to query alphavantage
word = 'duck'
key_word = "word"
key_score = "score"
search_word = "mallard"

#generate url
url = 'https://api.datamuse.com/words?ml=' + word
print(url)

# requests stock data from data muse
request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
dct_full = json.loads(request.text)




#####################################################################
# programming activity
# What is the score of the associated word: mallard
# Steps: 
# 1. load json into a dictionary
# 2. search for word "mallard"
# 3. print associated score value for mallard

# answer below, try yourself before looking
for item in dct_full:
    if 'duckling' in item:
        print('found it')

##my code above doesn't work
