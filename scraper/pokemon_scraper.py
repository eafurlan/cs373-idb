#!/usr/bin/env python3

import requests
import json

poke_list = []

def printDebug(str) :
	debug = True
	if debug :
		print(str)

def typeInfo(temp):
	if temp["type"] is "Normal":
		temp["color"] =  "72545c"
		temp["weakness"] = getRandomType()
	if t is "Fighting":
		return "9a3f22"
	if t is "Flying":
		return "4a667b"
	return "000000"

def getPokemon():
	chunk = 0
	while chunk <= 59 :
		url = 'http://swecune.com/api/pokemon?offset='+str(chunk)
		chunk += 1
		api_response = requests.get(url).json()
		for p in api_response:
			temp = dict()
			temp["id"] = p["id"]
			temp["name"] = p["name"]
			temp["hp"] = p["stats"][1]["base_stat"]
			temp["moves"] = p["moves"]
			temp["type"] = p["primary_type"]
			temp["color"] = getColor(temp["type"])
			
			poke_list.append(temp)

getPokemon()

with open('../flask/allPokemon.txt', 'w') as outfile:
	json.dump(poke_list, outfile)






# getBills()
# with open('../flask/allBills2.txt', 'w') as outfile:
# 	json.dump(billArr, outfile)

# getThreePeople()
# with open('people.txt', 'w') as outfile:
# 	json.dump(threePpl, outfile)

# getThreeBills()
# with open('bills.txt', 'w') as outfile:
# 	json.dump(threeBil, outfile)
