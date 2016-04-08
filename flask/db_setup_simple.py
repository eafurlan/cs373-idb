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
		print("Adding %s" % leg['lastname'])
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

def add_bills(bills_file) :
	data = open(bills_file).read()
	bills = json.loads(data)
	for bill in bills :

		print(bill['name'])
		print(bill['id'])
		print(bill['current_status'])
		print(bill['bill_type'])
		print(bill['date'])
		print(bill['link'])
		print("***************************")

		temp = Bill(id = bill['id'],
					name = filter_unicode_chars(bill['name'])[:255],
					current_status = bill['current_status'],
					bill_type = bill['bill_type'],
					date = bill['date'],
					link = bill['link']
	)
		session.merge(temp)
	session.commit()

def add_relations(relations_file) :
	data = open(relations_file).read()
	relations = json.loads(data)

	for relation in relations:
		# print(type(relation))
		print(relation['bill_id'])
		print(relation['leg_id'])
		print(relation['type_of_sponsorship'])
		print(type(relation['bill_id']))
		print(type(relation['leg_id']))
		print(type(relation['type_of_sponsorship']))

		try:
			temp = SponsorBillAssociation(bill_id = relation['bill_id'],
										leg_id = relation['leg_id'],
										type_of_sponsorship = relation['type_of_sponsorship']
											)

			session.merge(temp)
		except :
			print("Failed.")
			# print("fail for bill_id=%d leg_id=%d" & (relation['bill_id'], relation['leg_id']))
			pass

		print("________________________________-")

	session.commit()	

		
	# DANGEROUS!!!
def create_schemas():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_dev')
Session = sessionmaker(bind=engine)
session = Session()

# create_schemas()


people_file = 'allPeople3.txt'
bills_file = 'allBills3.txt'
relations_file = 'allAssocs4_300-542.txt'

# add_legislators(people_file)
# add_bills(bills_file)

# do this after the first two.
add_relations(relations_file)

	#TODO - see if we have to create a different SQL DB

