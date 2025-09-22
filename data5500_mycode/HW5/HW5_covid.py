# Ethan Westenskow

# #Import any needed library
# import cloudscraper 

# #read in the state list and turn it into a list.
# def state_list():  
#     with open("data5500_mycode/HW5/states_territories.txt", "r") as file:
#         lines = file.readlines()
#     state_codes = [line.strip() for line in lines]
#     return state_codes

# #This stores all of the data from each state in one big dictionary
# def every_state_data():
#     all_state_data = {}
#     for state in state_list():
#         #API pull:
#         scraper = cloudscraper.create_scraper() #Less efficient if teh scraper is inside the loop, but it organizes it better.
#         url = "https://api.covidtracking.com/v1/states/" + state + "/daily.json"
#         response = scraper.get(url)
#         data = response.json()
#         all_state_data[state] = data #Adds each state's data to the overseeing all_state_data dictionary. 
#     return all_state_data
# all_state_data = every_state_data() #with this variable, we can call on our data that our every_state_data() gives us. 

# #Calculations + Calculation output for each state
# def calculations(): 
#     #1. Average new daily confirmed cases (per state)




#########
##          SAVE KEYS FROM JSON AS VARIABLES
##          Loop through a list of dictionaries (just like the notes from class.)(you may need to delete your overarching dictionary)
##              ADD CALCULATIONS
#########


# THE CODE BELOW IS THE SAME AS ABOVE, BUT INSTEAD OF SAVING THE STATE DATA TO A DICTIONARY, IT SAVES IT TO A LIST AND WE CAN THEN LOOP THROUGH THE LIST OF DICTIONARIES. 
#Import any needed library
import cloudscraper 

#read in the state list and turn it into a list.
def state_list():  
    with open("data5500_mycode/HW5/states_territories.txt", "r") as file:
        lines = file.readlines()
    state_codes = [line.strip() for line in lines]
    return state_codes

#This stores all of the data from each state in one big dictionary
def every_state_data():
    for state in state_list():
        #API pull:
        scraper = cloudscraper.create_scraper() #Less efficient if teh scraper is inside the loop, but it organizes it better.
        url = "https://api.covidtracking.com/v1/states/" + state + "/daily.json"
        response = scraper.get(url)
        data_list = response.json()
    return data_list
data_list = every_state_data()
print(type(data_list))
