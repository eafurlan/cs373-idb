import unittest
import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from models import *

def filter_unicode_chars(s):
	return s.replace(u"\u2018", "'").replace(u"\u2019","'").replace(u"\u201c", "\"").replace(u"\u201d", "\"")

def add_legislators(people_file) :
	data = open(people_file).read()
	legislators = json.loads(data)
	for leg in legislators :
		temp = Legislator(id = leg['id'], 
			firstname = leg['firstname'], 
			lastname = leg['lastname'], 
			party = leg['party'],
			description = leg['description'], 
			title = leg['title'], 
			state = leg['state'], 
			birthday = leg['birthday'], 
			twitter = leg['twitter'], 
			youtube = leg['youtube'], 
			start_date = leg['start_date'], 
			website = leg['website'],
			photo_link = leg['photo_link'],
			bioguide_id = leg['bioguide_id']
			)

		session.merge(temp)
		session.commit()
		# print(temp)

def add_bills(bills_file) :
	data = open(bills_file).read()
	bills = json.loads(data)
	for bill in bills :

		print(bill['name'])
		print(bill['id'])
		print(bill['current_status'])
		print(bill['bill_type'])
		print(bill['date'])
		print("***************************")

		temp = Bill(id = bill['id'],
					name = filter_unicode_chars(bill['name'])[:255],
					current_status = bill['current_status'],
					bill_type = bill['bill_type'],
					date = bill['date']
	)
		session.merge(temp)
		session.commit()

def add_relations(bills_file) :
	data = open(bills_file).read()
	bills = json.loads(data)

	for bill in bills :
		print(bill['name'])
		# print(bill['id'])
		print("Sponsor ID: %s" % bill['sponsor'])
		# print(bill['sponsor'])
		
		temp = SponsorBillAssociation(
		bill_id = bill['id'],
		leg_id = bill['sponsor'],
		type_of_sponsorship = 'sponsor'
		)

		session.merge(temp)
		session.commit()		
		
		# print(type(bill['cosponsor']))
		# for cosponsor in bill['cosponsor']:
		# 	print("***Cosponsors***")
			# print(bill['cosponsor'])
			# temp = SponsorBillAssociation(
			# bill_id = bill['id'],
			# leg_id = cosponsor,
			# type_of_sponsorship = "cosponsor"
			# )

			# session.merge(temp)
			# session.commit()
		print("___________________________________________")

# def create_schemas():
#	DANGEROUS!!!
# 	Base.metadata.drop_all(engine)
# 	Base.metadata.create_all(engine)

engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_dev')
Session = sessionmaker(bind=engine)
session = Session()

# create_schemas()


bills_file = 'allBills2.txt'
people_file = 'allPeople2.txt'

# add_legislators(people_file)
# add_bills(bills_file)

# do this after the first two.
add_relations(bills_file)

	#TODO - see if we have to create a different SQL DB

