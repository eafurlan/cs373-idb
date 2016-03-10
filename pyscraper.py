#!/usr/bin/env python3

import requests
import json


peopleArr = []
billArr = []

def getPeople():
	url = 'https://www.govtrack.us/api/v2/role?current=true'
	response = requests.get(url).json()['objects']
	global peopleArr

	for p in range(3):
		temp = dict()
		temp['firstname'] = response[p]['person']['firstname']
		temp['lastname'] = response[p]['person']['lastname']
		temp['party'] = response[p]['party']
		temp['description'] = response[p]['description']
		temp['title'] = response[p]['title_long']
		temp['state'] = response[p]['state']
		temp['birthday'] = response[p]['person']['birthday']
		temp['twitter'] = response[p]['person']['twitterid']
		temp['youtube'] = response[p]['person']['youtubeid']
		temp['start_date'] = response[p]['startdate']
		temp['website'] = response[p]['website']
		temp['id'] = response[p]['person']['id']		#id for now
		
		"""
		singlepersonurl = 'https://www.govtrack.us/api/v2/person/' + str(temp['id'])
		r = requests.get(url).json()
		temp['roles'] = r['roles']
		"""

		peopleArr.append(temp)

def getBills():
	url = 'https://www.govtrack.us/api/v2/bill'
	response = requests.get(url).json()['objects']

	global billArr

	for b in range(3):
		temp = dict()
		temp['name'] = response[b]['title_without_number']
		temp['id'] = response[b]['id']			#id for now
		temp['current_status'] = response[b]['current_status']
		temp['bill_type'] = response[b]['bill_type']
		temp['sponsor'] = response[b]['sponsor']

		singlebillurl = url + '/' + str(temp['id'])
		r = requests.get(singlebillurl).json()		
		temp['terms'] = r['terms']
		temp['cosponsor'] = r['cosponsors']

		billArr.append(temp)


url =  'https://www.govtrack.us/api/v2/bill/76416'
response = requests.get(url).json()


getPeople()

with open('people.txt', 'w') as outfile:
	json.dump(peopleArr, outfile)


getBills()

with open('bills.txt', 'w') as outfile:
	json.dump(billArr, outfile)
	


