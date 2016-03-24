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
		session.commit()
		
		cur_sba = session.query(SponsorBillAssociation).first()
		self.assertEqual(cur_sba.bill_id,2)
		self.assertEqual(cur_sba.leg_id,2)

	def test6_delete_bill(self):
		test_bill = Bill(id=3)
		session.add(test_bill)
		session.commit()

		cur_bill = session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill.id,3)

		session.delete(cur_bill)

		cur_bill = session.query(Bill).filter_by(id=3).first()
		self.assertEqual(cur_bill,None)

	def test7_delete_multiple(self):
		
		test_bill_1 = Bill(id=4)
		test_bill_2 = Bill(id=5)
		session.add(test_bill_1)
		session.add(test_bill_2)
		session.commit()

		session.query(Bill).filter(Bill.id > 3).delete()

		cur_bill = session.query(Bill).filter_by(id=4).first()
		self.assertEqual(cur_bill,None)
		print(cur_bill)
		cur_bill = session.query(Bill).filter_by(id=5).first()
		self.assertEqual(cur_bill,None)




if __name__ == "__main__":
	#TODO - see if we have to create a different SQL DB
	engine = create_engine('sqlite:///:memory:')
	Session = sessionmaker(bind=engine)
	session = Session()
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	unittest.main()
	Base.metadata.drop_all(engine)
