import prepare_1090_json as planes
import json

from operator import itemgetter
print sorted(planes.json, key=itemgetter('seen'))[0]