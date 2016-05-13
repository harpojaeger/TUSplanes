from datetime import datetime
def send_message(craft):
	message = "%s: Flight %s at %s, %s with speed %s." % (str(datetime.now()),craft['flight'],craft['lat'],craft['lon'],craft['speed'])

	with open('tweets.txt', 'a') as f:
		f.write(message)