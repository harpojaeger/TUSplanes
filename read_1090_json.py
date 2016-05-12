import json
import urllib

dump1090_json_loc = "http://raspberrypi.local:8080/data.json"
stale = 10

f = urllib.urlopen(dump1090_json_loc)
myfile = f.read()
json_plane_data = json.loads(myfile)

		
json_plane_data = [x for x in json_plane_data if(
	#Function to filter the list of planes
	int(x['validposition']) and x['seen'] < stale
	)]


print "%s planes currently 'visible' and not stale'" % len(json_plane_data)

