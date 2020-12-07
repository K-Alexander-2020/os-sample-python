import requests  # need this to get data from API
import json
import datetime  # need this for time functions

class Races:
    # gets the data from the API
    response = requests.get(url="https://ergast.com/api/f1/current.json")

    # raises an error if there is a problem with the API
    response.raise_for_status()

    # stores the data from the API in the json_gp_data variable
    json_gp_data = response.json()

    def __init__(self):
        return self;

    # get_dates makes a list of the dates of all of the races in the season
    def get_dates(self):
        local_date_list = []
        MRData_access = self.json_gp_data['MRData']
        RaceTable_access = MRData_access['RaceTable']
        Races_access = RaceTable_access['Races']
        for each_race_data in Races_access:
            date_access = each_race_data['date']
            local_date_list.append(date_access)
        return local_date_list

    # get_today gets the current date and turns it into a string so that it can be compared to the json data later
    def get_today(self):

        local_today = datetime.datetime.now()
        local_today = local_today.strftime("%Y-%m-%d")
        return local_today

    # get_index_value_today gets the index value of today in the date list, for comparison in the other lists
    def get_index_value_today(self, date_list, today):
        date_index = date_list.index(today)
        return date_index

    # compare_day compares whether or not today's date is in the race date list
    def compare_day(self, today, passed_date_list):
        if today in passed_date_list:
            return True
        else:
            return False

    # get_race_name returns the name of the race that's happening today
    def get_race_name(self, date_index):
        race_name_list = []
        MRData_access = self.json_gp_data['MRData']
        RaceTable_access = MRData_access['RaceTable']
        Races_access = RaceTable_access['Races']
        for each_race_data in Races_access:
            race_name = each_race_data['raceName']
            race_name_list.append(race_name)
        todays_race_name = race_name_list[date_index]
        return todays_race_name

    # get_circuit_name returns the name of the circuit where today's race is happening
    def get_circuit_name(self, date_index):
        circuit_name_list = []
        MRData_access = self.json_gp_data['MRData']
        RaceTable_access = MRData_access['RaceTable']
        Races_access = RaceTable_access['Races']
        for each_race_data in Races_access:
            circuit_name = each_race_data['Circuit']['circuitName']
            circuit_name_list.append(circuit_name)
        todays_circuit_name = circuit_name_list[date_index]
        return todays_circuit_name

    # get_circuit_locality returns the name of the city where today's race is happening
    def get_circuit_locality(self, date_index):
        circuit_locality_list = []
        MRData_access = self.json_gp_data['MRData']
        RaceTable_access = MRData_access['RaceTable']
        Races_access = RaceTable_access['Races']
        for each_race_data in Races_access:
            circuit_locality = each_race_data['Circuit']['Location']['locality']
            circuit_locality_list.append(circuit_locality)
        todays_circuit_locality = circuit_locality_list[date_index]
        return todays_circuit_locality

    # get_circuit_country returns the name of the country where today's race is happening
    def get_circuit_country(self, date_index):
        circuit_country_list = []
        MRData_access = self.json_gp_data['MRData']
        RaceTable_access = MRData_access['RaceTable']
        Races_access = RaceTable_access['Races']
        for each_race_data in Races_access:
            circuit_country = each_race_data['Circuit']['Location']['country']
            circuit_country_list.append(circuit_country)
        todays_circuit_country = circuit_country_list[date_index]
        return todays_circuit_country

    def race_info(self):
        today = self.get_today(self)
        date_list = self.get_dates(self)
        # time = get_time_now()
        if self.compare_day(self, today, date_list):
            print("It's race day!")
            date_index = self.get_index_value_today(self, date_list, today)
            circuit_country = self.get_circuit_country(self, date_index)
            circuit_locality = self.get_circuit_locality(self, date_index)
            circuit_name = self.get_circuit_name(self, date_index)
            race_name = self.get_race_name(self, date_index)
            return "The " + race_name + "\nwill be held today at the\n" + circuit_name + "\nin " + circuit_locality + ", " + circuit_country + "."
            #return True


        else:
            return "There's no race today!"
            #print("There's no race today.")
            #return False
