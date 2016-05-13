-Should aircraft be tweeted based on how far they've traveled, or just how long it's been since they were last tweeted?  Possible considerations include:
	- Helicopters, for example, firefighting or surveying aircraft.  Even if their position doesn't change much over time, it's still interesting to know where they are.
	- Planes on the ground (a counterexample) – we don't want to tweet them over and over.
		- If tweets are filtered by altitude, this wouldn't be an issue.
		- If tweets are contextualized (what geographic feature is the plane directly over) this might be interesting: "flight xxx is at 0000 feet at TIA," for example.
Should all flight information be included in a tweet?  Or should there be different tweet formats based on *what* has changed about the aircraft since it was last tweeted?
	- "Flight xxxx has changed direction"
	- "Flight xxxx is now descending at xxx ft./min through xxx feet."
	- "Flight xxxx has descended to 15,000 ft. and is making its final approach."
	- These would require a lot of machine learning (we'd have to teach the program about flight paths and cruising/approach altitudes, e.g.) but could make the program much more interesting to follow.