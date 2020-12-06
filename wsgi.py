from flask import Flask
application = Flask(__name__)

@application.route("/")
import requests  # need this to get data from API
#import requests_cache
#from tkinter import *  # need this for the GUI
import datetime  # need this for time functions

# caches data to avoid making too many calls to the API
#requests_cache.install_cache(cache_name='ergast_cache',
                             #expire_after=43200)

# gets the data from the API
response = requests.get(url="https://ergast.com/api/f1/current.json")

# raises an error if there is a problem with the API
response.raise_for_status()

# stores the data from the API in the json_gp_data variable
json_gp_data = response.json()


# get_dates makes a list of the dates of all of the races in the season
def get_dates():
    local_date_list = []
    MRData_access = json_gp_data['MRData']
    RaceTable_access = MRData_access['RaceTable']
    Races_access = RaceTable_access['Races']
    for each_race_data in Races_access:
        date_access = each_race_data['date']
        local_date_list.append(date_access)
    return local_date_list


# get_today gets the current date and turns it into a string so that it can be compared to the json data later
def get_today():

    local_today = datetime.datetime.now()
    local_today = local_today.strftime("%Y-%m-%d")
    return local_today


# get_index_value_today gets the index value of today in the date list, for comparison in the other lists
def get_index_value_today(date_list, today):
    date_index = date_list.index(today)
    return date_index


# compare_day compares whether or not today's date is in the race date list
def compare_day(today, passed_date_list):
    if today in passed_date_list:
        return True
    else:
        return False


# get_race_name returns the name of the race that's happening today
def get_race_name(date_index):
    race_name_list = []
    MRData_access = json_gp_data['MRData']
    RaceTable_access = MRData_access['RaceTable']
    Races_access = RaceTable_access['Races']
    for each_race_data in Races_access:
        race_name = each_race_data['raceName']
        race_name_list.append(race_name)
    todays_race_name = race_name_list[date_index]
    return todays_race_name


# get_circuit_name returns the name of the circuit where today's race is happening
def get_circuit_name(date_index):
    circuit_name_list = []
    MRData_access = json_gp_data['MRData']
    RaceTable_access = MRData_access['RaceTable']
    Races_access = RaceTable_access['Races']
    for each_race_data in Races_access:
        circuit_name = each_race_data['Circuit']['circuitName']
        circuit_name_list.append(circuit_name)
    todays_circuit_name = circuit_name_list[date_index]
    return todays_circuit_name


# get_circuit_locality returns the name of the city where today's race is happening
def get_circuit_locality(date_index):
    circuit_locality_list = []
    MRData_access = json_gp_data['MRData']
    RaceTable_access = MRData_access['RaceTable']
    Races_access = RaceTable_access['Races']
    for each_race_data in Races_access:
        circuit_locality = each_race_data['Circuit']['Location']['locality']
        circuit_locality_list.append(circuit_locality)
    todays_circuit_locality = circuit_locality_list[date_index]
    return todays_circuit_locality


# get_circuit_country returns the name of the country where today's race is happening
def get_circuit_country(date_index):
    circuit_country_list = []
    MRData_access = json_gp_data['MRData']
    RaceTable_access = MRData_access['RaceTable']
    Races_access = RaceTable_access['Races']
    for each_race_data in Races_access:
        circuit_country = each_race_data['Circuit']['Location']['country']
        circuit_country_list.append(circuit_country)
    todays_circuit_country = circuit_country_list[date_index]
    return todays_circuit_country


def race_info():
    today = get_today()
    date_list = get_dates()
    # time = get_time_now()
    if compare_day(today, date_list):
        print("It's race day!")
        date_index = get_index_value_today(date_list, today)
        circuit_country = get_circuit_country(date_index)
        circuit_locality = get_circuit_locality(date_index)
        circuit_name = get_circuit_name(date_index)
        race_name = get_race_name(date_index)
        print("The " + race_name + "\nwill be held today at the\n" + circuit_name + "\nin " + circuit_locality + ", " + circuit_country + ".")
        #data = "It's race day!\nThe " + str.format(race_name) + "\nwill be held today at the\n" + str.format(circuit_name) + "\nin " + str.format(circuit_locality) + ", " + str.format(circuit_country) + "."
        #quote = data
        #canvas.itemconfig(window_text, text=quote)

    else:
        print("There's no race today.")
        #data = "There's no race today."
        #quote = data
        #canvas.itemconfig(window_text, text=quote)


#window = Tk()
#window.title("Is it race day?")
#window.config(padx=5, pady=5)

#canvas = Canvas(window, width=800, height=400)
#background_img = PhotoImage(file="background.png")
#canvas.create_image(400, 200, image=background_img)
#window_text = canvas.create_text(400, 200, text="Click the tyre!", width=800, font=("Arial", 30, "bold"), fill="white")
#canvas.grid(row=0, column=0)

#tyre_img = PhotoImage(file="tyre_button.png")
#tyre_button = Button(image=tyre_img, highlightthickness=0, command=race_info)
#tyre_button.grid(row=1, column=0)

#window.mainloop()

race_info()

if __name__ == "__main__":
    application.run()
