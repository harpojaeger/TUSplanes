import prepare_1090_json as aircraft
import message
from select_aircraft import evaluate

aircraft_list = aircraft.retrieve()
#print aircraft_list
if aircraft_list:
	for craft in aircraft_list:
		action = evaluate(craft)
