import unittest

from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine
#from sqlalchemy.orm import db.sessionmaker, relationship
from flask import Flask
from app import app

from models import *

#THIS IS SUPER IMPORTANT, NOT SURE HOW TO DESIGN THIS TO MAKE DB NOT GLOBAL
db = None

def single_session(func):
	'''
		Makes sure each test runs with an empty DB
	'''
	def launch_session(*args,**kwargs):
		
		print(func.__name__)
		func(*args,**kwargs)

		if(db.session.query(SponsorBillAssociation)):
			db.session.query(SponsorBillAssociation).delete()
		if(db.session.query(Bill)):
			db.session.query(Bill).delete()
		if(db.session.query(Legislator)):
			db.session.query(Legislator).delete()
		db.session.commit()
		
	return launch_session


class TestQuery(unittest.TestCase):

	@single_session
	def test1_create_db.session_test(self):
		no_instances = db.session.query(Bill).all()
		self.assertEqual(0, len(no_instances))

	@single_session
	def test2_create_one_bill(self):
		test_bill = Bill(id=0)
		db.session.add(test_bill)
		db.session.commit()
		query = db.session.query(Bill).all()
		self.assertEqual(1, len(query))

	@single_session
	def test3_create_another_bill(self):
		test_bill = Bill(id=1)
		db.session.add(test_bill)
		db.session.commit()
		query = db.session.query(Bill).all()
		self.assertEqual(1, query[0].id)

	@single_session
	def test4_create_one_legislator(self):
		test_legis = Legislator(id = 2000)
		db.session.add(test_legis)
		db.session.commit()
		query = db.session.query(Legislator).all()
		self.assertEqual(2000,query[0].id)

	@single_session
	def test5_create_bill_relation(self):
		test_bill = Bill(id=2)
		test_legis = Legislator(id = 2)
		
		sba = SponsorBillAssociation()
		sba.legislator = test_legis
		test_bill.sponsors.append(sba)
		db.session.add(test_bill)
		db.session.add(test_legis)
		db.session.commit()
		
		cur_sba = db.session.query(SponsorBillAssociation).first()
		self.assertEqual(cur_sba.bill_id,2)
		self.assertEqual(cur_sba.leg_id,2)

	@single_session
	def test6_create_sponsor_relation(self):
		test_bill = Bill(id=20)
		test_legis = Legislator(id = 21)
		
		sba = SponsorBillAssociation()
		sba.bill = test_bill
		test_legis.sponsored_bills.append(sba)
		db.session.add(test_bill)
		db.session.add(test_legis)
		db.session.commit()
		
		cur_sba = db.session.query(SponsorBillAssociation).first()
		self.assertEqual(cur_sba.bill_id,20)
		self.assertEqual(cur_sba.leg_id,21)
		pass
		

	@single_session
	def test7_delete_bill(self):
		test_bill = Bill(id=3)
		db.session.add(test_bill)
		db.session.commit()

		cur_bill = db.session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill.id,3)

		db.session.delete(cur_bill)

		cur_bill = db.session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill,None)

	@single_session
	def test8_delete_multiple(self):
		
		test_bill_1 = Bill(id=4)
		test_bill_2 = Bill(id=5)
		db.session.add(test_bill_1)
		db.session.add(test_bill_2)
		db.session.commit()

		db.session.query(Bill).filter(Bill.id > 3).delete()

		cur_bill = db.session.query(Bill).filter_by(id=4).first()
		self.assertEqual(cur_bill,None)
		
		cur_bill = db.session.query(Bill).filter_by(id=5).first()
		self.assertEqual(cur_bill,None)

	@single_session
	def test9_multiple_legislators(self):
		test_bill = Bill(id=10)
		test_legis_1 = Legislator(id = 11)
		test_legis_2 = Legislator(id = 12)

		
		sba1 = SponsorBillAssociation()
		sba1.legislator = test_legis_1
		test_bill.sponsors.append(sba1)

		sba2 = SponsorBillAssociation()
		sba2.legislator = test_legis_2
		test_bill.sponsors.append(sba2)

		db.session.add(test_bill)
		db.session.add(test_legis_1)
		db.session.add(test_legis_2)
		db.session.commit()
		
		q_item = db.session.query(Bill).filter_by(id = 10).first()
		self.assertEqual(len(q_item.sponsors),2)

	@single_session
	def test10_test_empty_db.session(self):
		
		no_instances = db.session.query(Bill).all()
		self.assertEqual(0, len(no_instances))

class TestSearch(unittest.TestCase):
    @single_session
    def test1_search_objects(self):
        test_bill_1 = Bill(id=0,name="Oliver's Bill",current_status="Committee",date="",link="")
        test_bill_2 = Bill(id=0,name="Bill's Bill",current_status="Committee",date="",link="")
        db.session.add(test_bill_1, test_bill_2)
        db.session.commit()
        Bill.query.whoosh_search('Oliver')
    

if __name__ == "__main__":
    global db
    app['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://travis1:swesquad123@172.99.70.111:3306/ildb_travis'
    db = SQLAlchemy(app) 

    db.
	Base.metadata.create_all(engine)
	unittest.main()
	Base.metadata.drop_all(engine)
