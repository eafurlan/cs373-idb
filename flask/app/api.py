from flask import Flask, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from app.models import *
from app import app


engine = create_engine('mysql+pymysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()


class AllBills(Resource):
	def get(self):
		bill_list = session.query(Bill).all()

		bill_dict_list = [x.__dict__ for x in bill_list]

		for x in bill_dict_list:
			del x['_sa_instance_state']

		return bill_dict_list

class OneBill(Resource):
	def get(self, bill_id):
		bill_obj =session.query(Bill).filter_by(id=bill_id).first()

		if bill_obj is None:
			abort(404)

		bill_dict = bill_obj.__dict__
		del bill_dict['_sa_instance_state']
		return bill_dict

class AllLeg(Resource):
	
	def get(self):
		leg_list = session.query(Legislator).all()
		
		leg_dict_list = [x.__dict__ for x in  leg_list]

		for x in leg_dict_list:
			del x['_sa_instance_state']

		# return leg_dict
		return leg_dict_list

	

class OneLeg(Resource):
	def get(self, leg_id):
		leg_obj = session.query(Legislator).filter_by(id=leg_id).first()
		print(leg_obj is None)
		if leg_obj is None:
			abort(404)

		leg_dict = leg_obj.__dict__
		print(leg_dict.keys())
		del leg_dict['_sa_instance_state']



		return leg_dict
	

