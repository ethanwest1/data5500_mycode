# Ethan Westenskow

#Import any needed library
import cloudscraper 
import json



## --- Set up ---
#read in the state list and turn it into a list.
def state_list():  
    with open("data5500_mycode/HW5/states_territories.txt", "r") as file:
        lines = file.readlines()
    state_codes = [line.strip() for line in lines]
    return state_codes
state_codes = state_list() #uncomment when done testing
# 
#This stores all of the data from each state in one big dictionary
def every_state_data(state_codes):
    state_data = {} #We're storing the state data in a dictionary so that we can keep each state's data seperate. It will be easier for calculation.
    #API pull:
    scraper = cloudscraper.create_scraper() 
    for state in state_codes:
        url = "https://api.covidtracking.com/v1/states/" + state + "/daily.json"
        response = scraper.get(url)
        raw_data = response.json() #gathers the raw data
        state_data[state] = raw_data
    #Save the raw json data to a json file.
        with open(f"data5500_mycode/HW5/Raw_State_Data/{state}.json", "w") as file: #creates a folder where each state's data is saved. (Assumes that the folder is already created. Just remove the filepath if you'd rather the files export without a folder.)
            json.dump(raw_data, file, indent=2) #dumps the data into the file
    return state_data
state_data = every_state_data(state_codes)



## --- Analysis of data ---
#Avergae calculation: Average new daily confirmed cases (per state) 
def avg_calculation(single_state_code, state_data):
    state_records = state_data[single_state_code] 
    new_cases = []
    for day in state_records: #this will fetch any new cases and add them to a list that we can then use for calculation.
        value = day.get("positiveIncrease")
        if value is not None:
            new_cases.append(value)
    if len(new_cases) == 0: #Outputs "N/A" if there are no new cases.
        return "N/A"
    else:
        avg = (sum(new_cases) / len(new_cases)) #computes the average using the new_cases list
    return round(avg, 2) 

#Date with the highest new number of cases
def date_highest_new_number_of_cases(single_state_code, state_data):
    state_records = state_data[single_state_code] #reads in the state_records for analysis.
    current_max = None
    date_for_max = None

    for day in state_records: #loops through each day and scans the values.
        value = day.get('positiveIncrease')
        if value is None:
            continue #this skips missing values
        if (current_max is None) or (value > current_max): #Compares the current day value of new cases to the max. 
            current_max = value #It will update it if a new max is found. 
            date_for_max = day.get('date') #Updates the date if a new max is found, returned as an interger.

    if date_for_max is None: #If there are no new cases and thus no max date, then "N/A" will be returned.
        return "N/A"

    date_str = str(date_for_max) #the date is an interger, so we change it to a string here so that we can format it. 
    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}" #formats the string date into something nice.
    return formatted_date

#Most recent date with no new covid cases:
def recent_date_with_no_new_cases(single_state_code, state_data):
    state_records = state_data[single_state_code] #reads in the state_records for analysis.
    most_recent_date = None

    for day in state_records: #loops through each day and scans the values.
        value = day.get("positiveIncrease")
        if value == 0:
            most_recent_date = day.get('date')
            break
    if most_recent_date is None: #Prevents an error if no most_recent_date is found.
        return "N/A"
        

    date_str = str(most_recent_date) #the date is an interger, so we change it to a string here so that we can format it. 
    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}" #formats the string date into something nice.
    return formatted_date

#Monthly max/min new cases: 
## CHATGPT HELPED ME A LOT WITH THIS ONE
#It recommended combining finding the max and min into one function because we would be repeating ourself, and it can keep it in one place. 
def monthly_max_min_new_cases(single_state_code, state_data): 
    state_records = state_data[single_state_code] #reads in the state_records for analysis.
   
    #I want the output to be nice for reading so we're gonna assign the months names. #ChatGPT helped with this a lot
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    monthly_totals ={} #
    for day in state_records:
        value = day.get("positiveIncrease")
        if value is None:
            continue
        d = day.get('date') #grabs the date as an interger
        year = d // 10000 #this math isolates the year
        month = (d // 100) % 100 #this math isolates the month
        monthly_totals[(year, month)] = monthly_totals.get((year, month), 0) + value #this takes the month day by day and sums up the new cases. 
    if not monthly_totals: #This will return "N/A" if there are no monthly totals.
        return "N/A", "N/A" 

    max_item = max(monthly_totals.items(), key=lambda x: (x[1], x[0][0], x[0][1])) #this scans the lsit and finds the month with the largest total. 
    min_item = min(monthly_totals.items(), key=lambda x: (x[1], x[0][0], x[0][1])) #this scans the lsit and finds the month with the smallest total. 

    (max_y, max_m), _ = max_item
    (min_y, min_m), _ = min_item

    #This restructures the max/min items to a string and assignes them a month name. 
    max_str = f"{month_names[max_m - 1]} {max_y}" 
    min_str = f"{month_names[min_m - 1]} {min_y}"

    return max_str, min_str
    







#This is the required output function. It outputs the info that the assignment requires.
def required_output(state_codes, state_data):
    for state in state_codes:
        print("\nCovid confirmed cases statistics:")
        print(f"State Name: {state.upper()}")
        print(f"Average number of new daily confirmed cases for the entire dataset: {avg_calculation(state, state_data)}")
        print(f"Date with the highest new number of covid cases: {date_highest_new_number_of_cases(state, state_data)}")
        print(f"Most recent date with no new covid cases: {recent_date_with_no_new_cases(state, state_data)}")
        max_month, min_month = monthly_max_min_new_cases(state, state_data)
        print(f"Month and Year, with the highest new number of covid cases: {max_month}")
        print(f"Month and Year, with the lowest new number of covid cases: {min_month}")

required_output(state_codes, state_data)