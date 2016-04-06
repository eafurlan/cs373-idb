#!/usr/bin/env python3

import requests
import json

from frozendict import frozendict

billArr = []
threePpl = []
threeBil = []

def printDebug(str) :
	debug = True
	if debug :
		print(str)

def getPeople():
	url = 'https://www.govtrack.us/api/v2/role?current=true&limit=600'
	response = requests.get(url).json()['objects']
	
	peopleArr = []
	billsNeeded = []


	
	for p in range(len(response)):

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
		temp['photo_link'] = "https://www.govtrack.us/data/photos/"+str(temp['id'])+"-200px.jpeg"
		temp['bioguide_id'] = response[p]['person']['bioguideid']
		"""
		singlepersonurl = 'https://www.govtrack.us/api/v2/person/' + str(temp['id'])
		r = requests.get(url).json()
		temp['roles'] = r['roles']
		"""
		
		# Debug: See which person we are on
		printDebug("Person: %s %s" % (temp['firstname'], temp['lastname']))
		printDebug(p)


		peopleArr.append(temp)
		

		# add the bills that this person sponsors
		sponsored_bill_url = 'https://www.govtrack.us/api/v2/bill?sponsor=%s' % temp['id']
		sponsored_response = requests.get(sponsored_bill_url).json()['objects']
		



		for b in sponsored_response:
			temp = {}
			temp['name'] = b['title_without_number']
			temp['id'] = b['id']
			temp['current_status'] = b['current_status']
			temp['bill_type'] = b['bill_type']
			temp['sponsor'] = b['sponsor']['id']
			temp['link'] = b['link']
			temp['date'] = b['introduced_date']

			if temp not in billsNeeded :
				billsNeeded.append(temp)

		#add the bills that this person co-sponsors
		cosponsored_bill_url = 'https://www.govtrack.us/api/v2/bill?limit=6000&cosponsors=%s' % temp['id']
		cosponsored_response = requests.get(cosponsored_bill_url).json()['objects']
		
		
		
		for c in cosponsored_response:
			temp = {}
			temp['name'] = c['title_without_number']
			temp['id'] = c['id']
			temp['current_status'] = c['current_status']
			temp['bill_type'] = c['bill_type']
			temp['sponsor'] = c['sponsor']['id']
			temp['link'] = c['link']
			temp['date'] = c['introduced_date']

			if temp not in billsNeeded :
				billsNeeded.append(temp)

	#write the people
	with open('../flask/allPeople2.txt', 'w') as outfile:
		json.dump(peopleArr, outfile)

	#write the bills
	with open('../flask/allBills2.txt', 'w') as outfile:
		json.dump(billsNeeded, outfile)

		

		# 	# if list does not contain a bill with this id, add the bill

		# cosponsored_bill_url = 'https://www.govtrack.us/api/v2/bill?cosponsors=%s' % temp['id']
		# cosponsored_response = requests.get(cosponsored_bill_url).json()['objects']
		# for c in cosponsored_response:
		# 	billsNeeded.append(c)
		

def getThreePeople():

	p_ids = [412378, 412542, 412247]

	global threePpl

	for p in p_ids:
		url = 'https://www.govtrack.us/api/v2/person/' + str(p)
		response = requests.get(url).json()

		roles = response['roles']

		temp = dict()
		temp['firstname'] = response['firstname']
		temp['lastname'] = response['lastname']
		temp['party'] = roles[len(roles)-1]['party']
		temp['description'] = roles[len(roles)-1]['description']
		temp['title'] = roles[len(roles)-1]['title_long']
		temp['state'] = roles[len(roles)-1]['state']
		temp['birthday'] = response['birthday']
		temp['twitter'] = response['twitterid']
		temp['youtube'] = response['youtubeid']
		temp['start_date'] = roles[len(roles)-1]['startdate']
		temp['website'] = roles[len(roles)-1]['website']
		temp['id'] = response['id']		#id for now
		temp['photo_link'] = "https://www.govtrack.us/data/photos/"+str(temp['id'])+"-200px.jpeg"



def getBills():
	url = 'https://www.govtrack.us/api/v2/bill'
	# response = requests.get(url).json()['objects']

	global billsNeeded
	global billArr

	for b in billsNeeded:
		temp = dict()
		temp['name'] = b['title_without_number']
		temp['id'] = b['id']			#id for now
		temp['current_status'] = b['current_status']
		temp['bill_type'] = b['bill_type']
		temp['sponsor'] = b['sponsor']['id']
		temp['link'] = b['link']
		temp['date'] = b['introduced_date']

		singlebillurl = url + '/' + str(temp['id'])
		r = requests.get(singlebillurl).json()
		temp['terms'] = r['terms']
		temp['cosponsor'] = []
		for person in r['cosponsors']:
			temp['cosponsor'].append(person['id'])

		billArr.append(temp)

	# for b in range(len(response)):
	# 	temp = dict()
	# 	temp['name'] = response[b]['title_without_number']
	# 	temp['id'] = response[b]['id']			#id for now
	# 	temp['current_status'] = response[b]['current_status']
	# 	temp['bill_type'] = response[b]['bill_type']
	# 	temp['sponsor'] = response[b]['sponsor']['id']
	# 	temp['link'] = response[b]['link']
	# 	temp['date'] = response[b]['introduced_date']

	# 	singlebillurl = url + '/' + str(temp['id'])
	# 	r = requests.get(singlebillurl).json()
	# 	temp['terms'] = r['terms']
	# 	temp['cosponsor'] = []
	# 	for person in r['cosponsors']:
	# 		temp['cosponsor'].append(person['id'])

	# 	billArr.append(temp)

def getThreeBills():

	b_ids = [343921, 336967, 343960]

	global threeBil

	for b in b_ids:
		url = 'https://www.govtrack.us/api/v2/bill/'+str(b)
		response = requests.get(url).json()

		temp = dict()
		temp['name'] = response['title_without_number']
		temp['id'] = response['id']			#id for now
		temp['current_status'] = response['current_status']
		temp['bill_type'] = response['bill_type']
		temp['sponsor'] = response['sponsor']['id']
		temp['link'] = response['link']
		temp['date'] = response['introduced_date']


		temp['terms'] = response['terms']
		temp['cosponsor'] = []
		for person in response['cosponsors']:
			temp['cosponsor'].append(person['id'])

		threeBil.append(temp)



getPeople()




# with open('../flask/allPeople2.txt', 'w') as outfile:
# 	json.dump(peopleArr, outfile)


# getBills()
# with open('../flask/allBills2.txt', 'w') as outfile:
# 	json.dump(billArr, outfile)

# getThreePeople()
# with open('people.txt', 'w') as outfile:
# 	json.dump(threePpl, outfile)

# getThreeBills()
# with open('bills.txt', 'w') as outfile:
# 	json.dump(threeBil, outfile)
