import json
import urllib

dump1090_json_loc = "http://raspberrypi.local:8080/data.json"
stale = 10

f = urllib.urlopen(dump1090_json_loc)
myfile = f.read()
json = json.loads(myfile)

		
json = [x for x in json if(
	#Function to filter the list of planes
	int(x['validposition']) and x['seen'] < stale
	)]



