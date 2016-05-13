import json
import urllib
from operator import itemgetter

dump1090_json_loc = "http://raspberrypi.local:8080/data.json"
stale = 10
def retrieve():
	f = urllib.urlopen(dump1090_json_loc)
	myfile = f.read()
	data = json.loads(myfile)
	data = [x for x in data if(
		#Function to filter the list of planes
		int(x['validposition']) and x['seen'] < stale 
		#and x['flight'] <> ''
		)]
	if data:
		plane_data = sorted(data, key=itemgetter('seen'))
		return plane_data