import pickle
from geopy.distance import vincenty
import prepare_1090_json as aircraft
from message import send_message
for craft in aircraft.data:
	print "%s (%s) seen %ss ago" % (craft['squawk'],craft['flight'],craft['seen'])
	pickle.dump( craft, open( "save.p", "wb" ) )
	send_message(craft)