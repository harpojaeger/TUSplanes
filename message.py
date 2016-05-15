#The control script passes this function an aircraft and it sends an appropriate message.
import time
def send(craft):
	message = "%s: Flight %s at %s, %s with speed %s.\n" % (str(time.time()),craft['flight'],craft['lat'],craft['lon'],craft['speed'])
	#with open('tweets.txt', 'a') as f:
		#f.write(message)
	print(message)	