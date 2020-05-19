#!/usr/bin/python3


import requests, json 
import unicodedata
from coviddists import get_district_code_from_passing

def covid_data(keyToSearch):
	response = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
	print("RESPONSE", response)
	try:
		covid_data = response.json()
		y = json.dumps(covid_data[1])
		x = json.loads(y)
		districtDataofX=json.dumps(x["districtData"])
		districtDataofXjson = json.loads(districtDataofX)
		json_search_keys = create_filter(keyToSearch)
		print("covid_data--", json_search_keys)
		for k in covid_data:
			covid_states = json.dumps(k)
			covid_states_json = json.loads(covid_states)
			if covid_states_json["statecode"] == json_search_keys[0]:
				for k1 in covid_states_json["districtData"] :
					covid_states_dist = json.dumps(k1)
					covid_states_dist_json = json.loads(covid_states_dist)
					if covid_states_dist_json["district"] == json_search_keys[2]:
						#print("\n\nDistrict data: ",covid_states_dist_json)
						to_str_active = str(covid_states_dist_json["active"])
						to_str_confirmed = str(covid_states_dist_json["confirmed"])
						to_str_deceased = str(covid_states_dist_json["deceased"])
						to_str_recovered = str(covid_states_dist_json["recovered"])
						fin_data = "Cases in "+ covid_states_dist_json["district"]+ ", Confirmed: "+to_str_confirmed+\
							   ", Deceased: "+to_str_deceased+ ", Recovered: "+to_str_recovered+\
							   ", Active: "+to_str_active;
						print (fin_data)
						return fin_data
	except KeyError:
		print("Data error")
		return ": Data error or probably no data for your query"


def create_filter(cmd_string):
	print("Query ->",cmd_string)
	dist = get_dist(cmd_string)
	return dist

def get_dist(dist_code):
	broken = dist_code.split(" ")
	dist = broken[1]
	filter_keys = []
	filter_keys.append(dist[0:2])
	filter_keys.append(dist[2:])
	dist_name = get_district_code_from_passing(broken[1])
	filter_keys.append(dist_name)
	return filter_keys

def create_filter_for_state(state_query):
	try:
		broken = state_query.split(" ")
		if len(broken) == 4:
			if broken[3].upper() == "C":
				broken.append('Confirmed')
			elif broken[3].upper() == "D":
				broken.append('Deceased')
			elif broken[3].upper() == "R":
				broken.append('Recovered')
			elif broken[3].upper() == "A":
				broken.append('Active')
		else:
			return "Wrong Command"
	except KeyError:
		return ": Data error"
	return broken

def covid_data_by_state_and_date(keyToSearch):
        response = requests.get('https://api.covid19india.org/states_daily.json')
        print("RESPONSE", response)
        try:
                covid_data = response.json()
                json_search_keys = create_filter_for_state(keyToSearch)
                if json_search_keys == "Wrong Command" or json_search_keys == ": Data error":
                        return json_search_keys
                print("covid_data for states--", json_search_keys)
                daily_data = covid_data["states_daily"]
                for k in daily_data:
                        covid_states = json.dumps(k)
                        covid_states_json = json.loads(covid_states)
                        #print(covid_states_json["status"], " <-> ", json_search_keys[4])
                        if covid_states_json["date"] == json_search_keys[2] and covid_states_json["status"] == json_search_keys[4]:
                                #print("Data : ", covid_states_json[json_search_keys[1]])
                                return json_search_keys[1]+" "+json_search_keys[4]+"on date "+json_search_keys[2]+" -> "covid_states_json[json_search_keys[1]]
        except KeyError:
                print("Data error")
                return ": Data error or probably no data for your query"


#covid_data("covid AR28")
covid_data_by_state_and_date("Covid mh 18-May-20 r")
