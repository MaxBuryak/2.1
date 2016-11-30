import json
from pprint import pprint

with open ('countries.json') as import_file:
	country = json.load(import_file)
	pprint (country)