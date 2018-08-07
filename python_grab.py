import requests

url = "https://swapi.co/api/starships"

starships_json = requests.get(url).json()

for ship in starships_json['results']:
	print
	print ship['name']
	if len(ship['pilots']) > 0:
		print "	This ship has been piloted by the following: "
		for pilot in ship['pilots']:
			pilot_name = requests.get(pilot).json()['name']
			print "		" + pilot_name
	elif len(ship['pilots']) == 0:
		print "	This ship has not been piloted"
	
	print
	print "*****************************************************"
	




