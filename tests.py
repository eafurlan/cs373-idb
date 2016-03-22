import unittest


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from models import *

class TestQuery(unittest.TestCase):

	def test1_create_session_test(self):
		no_instances = session.query(Bill).all()
		self.assertEqual(0, len(no_instances))

	def test2_create_one_bill(self):
		test_bill = Bill(id=0)
		session.add(test_bill)
		session.commit()
		query = session.query(Bill).all()
		self.assertEqual(1, len(query))

	def test3_create_another_bill(self):
		test_bill = Bill(id=1)
		session.add(test_bill)
		session.commit()
		query = session.query(Bill).all()
		self.assertEqual(1, query[1].id)

	def test4_create_one_legislator(self):
		test_legis = Legislator(id = 0)
		session.add(test_legis)
		session.commit()
		query = session.query(Legislator).all()
		self.assertEqual(0,query[0].id)

	def test5_create_bill_relation(self):
		test_bill = Bill(id=2)
		test_legis = Legislator(id = 2)
		
		sba = SponsorBillAssociation()
		sba.legislator = test_legis
		test_bill.sponsors.append(sba)
		session.add(test_bill)
		session.add(test_legis)
		
		query = session.query(Bill).all() + session.query(Legislator).all() + session.query(SponsorBillAssociation).all()
		self.assertEqual(query[-1].bill_id,2)
		self.assertEqual(query[-1].leg_id,2)

if __name__ == "__main__":
	#TODO - see if we have to create a different SQL DB
	engine = create_engine('sqlite:///:memory:')
	Session = sessionmaker(bind=engine)
	session = Session()
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	unittest.main()
	Base.metadata.drop_all(engine)
