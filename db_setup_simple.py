import unittest
import json

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






engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()

add_legislators()
	#TODO - see if we have to create a different SQL DB
