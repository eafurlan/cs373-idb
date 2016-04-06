import unittest


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from flask import Flask

from models import *

def single_session(func):
	'''
		Makes sure each test runs with an empty DB
	'''
	def launch_session(*args,**kwargs):
		
		print(func.__name__)
		func(*args,**kwargs)

		if(session.query(SponsorBillAssociation)):
			session.query(SponsorBillAssociation).delete()
		if(session.query(Bill)):
			session.query(Bill).delete()
		if(session.query(Legislator)):
			session.query(Legislator).delete()
		session.commit()
		
	return launch_session


class TestQuery(unittest.TestCase):

	@single_session
	def test1_create_session_test(self):
		no_instances = session.query(Bill).all()
		self.assertEqual(0, len(no_instances))

	@single_session
	def test2_create_one_bill(self):
		test_bill = Bill(id=0)
		session.add(test_bill)
		session.commit()
		query = session.query(Bill).all()
		self.assertEqual(1, len(query))

	@single_session
	def test3_create_another_bill(self):
		test_bill = Bill(id=1)
		session.add(test_bill)
		session.commit()
		query = session.query(Bill).all()
		self.assertEqual(1, query[0].id)

	@single_session
	def test4_create_one_legislator(self):
		test_legis = Legislator(id = 2000)
		session.add(test_legis)
		session.commit()
		query = session.query(Legislator).all()
		self.assertEqual(2000,query[0].id)

	@single_session
	def test5_create_bill_relation(self):
		test_bill = Bill(id=2)
		test_legis = Legislator(id = 2)
		
		sba = SponsorBillAssociation()
		sba.legislator = test_legis
		test_bill.sponsors.append(sba)
		session.add(test_bill)
		session.add(test_legis)
		session.commit()
		
		cur_sba = session.query(SponsorBillAssociation).first()
		self.assertEqual(cur_sba.bill_id,2)
		self.assertEqual(cur_sba.leg_id,2)

	@single_session
	def test6_create_sponsor_relation(self):
		test_bill = Bill(id=20)
		test_legis = Legislator(id = 21)
		
		sba = SponsorBillAssociation()
		sba.bill = test_bill
		test_legis.sponsored_bills.append(sba)
		session.add(test_bill)
		session.add(test_legis)
		session.commit()
		
		cur_sba = session.query(SponsorBillAssociation).first()
		self.assertEqual(cur_sba.bill_id,20)
		self.assertEqual(cur_sba.leg_id,21)
		pass
		

	@single_session
	def test7_delete_bill(self):
		test_bill = Bill(id=3)
		session.add(test_bill)
		session.commit()

		cur_bill = session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill.id,3)

		session.delete(cur_bill)

		cur_bill = session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill,None)

	@single_session
	def test8_delete_multiple(self):
		
		test_bill_1 = Bill(id=4)
		test_bill_2 = Bill(id=5)
		session.add(test_bill_1)
		session.add(test_bill_2)
		session.commit()

		session.query(Bill).filter(Bill.id > 3).delete()

		cur_bill = session.query(Bill).filter_by(id=4).first()
		self.assertEqual(cur_bill,None)
		
		cur_bill = session.query(Bill).filter_by(id=5).first()
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

		session.add(test_bill)
		session.add(test_legis_1)
		session.add(test_legis_2)
		session.commit()
		
		q_item = session.query(Bill).filter_by(id = 10).first()
		self.assertEqual(len(q_item.sponsors),2)

	@single_session
	def test10_test_empty_session(self):
		
		no_instances = session.query(Bill).all()
		self.assertEqual(0, len(no_instances))


if __name__ == "__main__":
	#TODO - see if we have to create a different SQL DB
	engine = create_engine('mysql+pymysql://dev1:swesquad@172.99.70.111:3306/ildb_dev')
	Session = sessionmaker(bind=engine)
	session = Session()
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	unittest.main()
	Base.metadata.drop_all(engine)
