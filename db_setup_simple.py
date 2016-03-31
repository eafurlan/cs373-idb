import unittest
import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from models import *


def add_legislators() :
	data = open('flask/people.txt').read()
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
			website = leg['website']
			# sponsored_bills = leg['sponsored_bills'], 
			)

		session.add(temp)
		session.commit()
		# print(temp)

def add_bills() :
	data = open('flask/bills.txt').read()
	bills = json.loads(data)
	for bill in bills :
		temp = Bill(id = bill['id'],
		name = bill['name'],
		current_status = bill['current_status'],
		bill_type = bill['bill_type'],
		date = bill['date']
	)
		session.add(temp)
		session.commit()

def add_relations() :
	data = open('flask/bills.txt').read()
	bills = json.loads(data)

	for bill in bills :
		# print(bill['name'])
		# print(type(bill['id']))
		# print(bill['id'])
		temp = SponsorBillAssociation(
		bill_id = bill['id'],
		leg_id = bill['sponsor'],
		type_of_sponsorship = 'sponsor'
		)

		# session.merge(temp)
		# session.commit()		

		for cosponsor in bill['cosponsor']:
			temp = SponsorBillAssociation(
			bill_id = bill['id'],
			leg_id = cosponsor,
			type_of_sponsorship = "cosponsor"
			)

			session.merge(temp)
			session.commit()	

engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()

# add_legislators()
# add_bills()
add_relations()
	#TODO - see if we have to create a different SQL DB
