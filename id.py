#Given an aircraft info list, this function determines how it should be identified (by flight number, squawk, tail number, etc.)

def id(craft):
	if craft['flight'] <> '':
		return craft['flight'].strip()
	elif int(craft ['squawk']) <> 0:
		return "squawk %s" % craft['squawk'].strip()
	else:
		return "ICAO id %s" % craft['hex'].strip()
