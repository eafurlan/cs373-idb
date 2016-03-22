import unittest


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

class TestQuery(unittest.TestCase):

	
	


	def test_1(self):
		no_instances = session.query(Bill).all()
		self.assertEqual(0, len(no_instances))

	def test_2(self):
		test_bill = Bill(id=2)
		session.add(test_bill)
		session.commit()
		one_instance = session.query(Bill).all()
		self.assertEqual(1, len(one_instance))
	
	def test_3(self):
		test_bill = Bill(id=3)
		session.add(test_bill)
		session.commit()
		current_instances = session.query(Bill).all()
		self.assertEqual(3, two_instances[1].id)
		

if __name__ == "__main__":
	engine = create_engine('sqlite:///:memory:')
	Session = sessionmaker(bind=engine)
	session = Session()
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	unittest.main()
	Base.metadata.drop_all(engine)