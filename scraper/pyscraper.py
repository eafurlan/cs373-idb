#!/usr/bin/env python3

import requests
import json


billArr = []
assocArray = []
threePpl = []
threeBil = []

def printDebug(str) :
	debug = True
	if debug :
		print(str)

def getPeople():
	url = 'https://www.govtrack.us/api/v2/role?current=true&limit=600'
	people_response = requests.get(url).json()['objects']
	
	peopleArr = []
	billsNeeded = []

	# for p in range(1):
	for p in range(300, 542):

		temp = dict()
		temp['firstname'] = people_response[p]['person']['firstname']
		temp['lastname'] = people_response[p]['person']['lastname']
		temp['party'] = people_response[p]['party']
		temp['description'] = people_response[p]['description']
		temp['title'] = people_response[p]['title_long']
		temp['state'] = people_response[p]['state']
		temp['birthday'] = people_response[p]['person']['birthday']
		temp['twitter'] = people_response[p]['person']['twitterid']
		temp['youtube'] = people_response[p]['person']['youtubeid']
		temp['start_date'] = people_response[p]['startdate'] 	
		temp['website'] = people_response[p]['website']
		temp['id'] = people_response[p]['person']['id']		#id for now
		temp['photo_link'] = "https://www.govtrack.us/data/photos/"+str(temp['id'])+"-200px.jpeg"
		temp['bioguide_id'] = people_response[p]['person']['bioguideid']
		"""
		singlepersonurl = 'https://www.govtrack.us/api/v2/person/' + str(temp['id'])
		r = requests.get(url).json()
		temp['roles'] = r['roles']
		"""
		
		# Debug: See which person we are on
		printDebug("Person: %s %s" % (temp['firstname'], temp['lastname']))
		printDebug(p)

		# write the people
		# peopleArr.append(temp)
		

		# add the bills that this person sponsors from this session of congress
		sponsored_bill_url = 'https://www.govtrack.us/api/v2/bill?limit=6000&congress=114&sponsor=%s' % temp['id']
		sponsored_response = requests.get(sponsored_bill_url).json()['objects']
		

		print("STARTING SPONSORED BILLS")
		for b in sponsored_response:
			bill_to_add = {}
			bill_to_add ['name'] = b['title_without_number']
			bill_to_add['id'] = b['id']
			bill_to_add['current_status'] = b['current_status']
			bill_to_add['bill_type'] = b['bill_type']
			bill_to_add['sponsor'] = b['sponsor']['id']
			bill_to_add['link'] = b['link']
			bill_to_add['date'] = b['introduced_date']

			# write the bills
			# if bill_to_add not in billsNeeded :
			# 	print("Adding bill: %s" % b['id'])
			# 	billsNeeded.append(bill_to_add)

			tempAssoc = {}
			tempAssoc['bill_id'] = b['id']
			tempAssoc['leg_id'] = temp['id']
			tempAssoc['type_of_sponsorship'] = 'sponsor'



			if tempAssoc not in assocArray:
				print("Adding sponsor association between bill %s and legislator %s" % (b['id'], temp['id']))
				assocArray.append(tempAssoc)

		#add the bills that this person co-sponsors
		cosponsored_bill_url = 'https://www.govtrack.us/api/v2/bill?limit=6000&congress=114&cosponsors=%s' % temp['id']
		cosponsored_response = requests.get(cosponsored_bill_url).json()['objects']
		# print("cosponsored response for person id:%s len = %d" % (temp['id'], len(cosponsored_response)) )

		# roy blunt example: all the bills he has cosponsored
		# https://www.govtrack.us/api/v2/bill?limit=6000&congress=114&cosponsors=400034
		
		print("STARTING COSPONSORED BILLS")
		for c in cosponsored_response:
			bill_to_add = {}
			bill_to_add['name'] = c['title_without_number']
			bill_to_add['id'] = c['id']
			bill_to_add['current_status'] = c['current_status']
			bill_to_add['bill_type'] = c['bill_type']
			bill_to_add['sponsor'] = c['sponsor']['id']
			bill_to_add['link'] = c['link']
			bill_to_add['date'] = c['introduced_date']

			if bill_to_add not in billsNeeded :
				billsNeeded.append(bill_to_add)

			tempAssoc = {}
			tempAssoc['bill_id'] = c['id']
			tempAssoc['leg_id'] = temp['id'] # person id
			tempAssoc['type_of_sponsorship'] = 'cosponsor'

			if tempAssoc not in assocArray:
				print("Adding cosponsor association between bill %s and legislator %s" % (c['id'], temp['id']))
				assocArray.append(tempAssoc)


	# #write the people
	# with open('../flask/allPeople4.txt', 'w') as outfile:
	# 	json.dump(peopleArr, outfile)

	# #write the bills
	# with open('../flask/allBills4.txt', 'w') as outfile:
	# 	json.dump(billsNeeded, outfile)

	#write the associations
	with open('../flask/allAssocs4_300-542.txt', 'w') as outfile:
		json.dump(assocArray, outfile)


		

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
