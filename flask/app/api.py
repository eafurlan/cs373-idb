from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from app.models import *

app = Flask(__name__)
from app import views

api = Api(app)

engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()


class AllBills(Resource):
	def get(self):
		bill_obj = session.query(Bill).all()
		bill_dict = bill_obj.__dict__
		return bill_dict

class OneBill(Resource):
	def get(self, bill_id):
		bill_obj =session.query(Bill).filter_by(id=bill_id).first()
		bill_dict = bill_obj.__dict__
		return bill_dict

class AllLeg(Resource):
	def get(self):
		leg_obj = session.query(Legislator).all()
		leg_dict = leg_obj.__dict__
		return leg_dict

class OneLeg(Resource):
	def get(self, leg_id):
		leg_obj = session.query(Legislator).filter_by(id=leg_id).first()
		leg_dict = leg_obj.__dict__
		return leg_dict
		

api.add_resource(AllBills, '/api/bills')
api.add_resource(AllLeg, '/api/legislators')
api.add_resource(OneBills, '/api/bills/<int:bill_id>')
api.add_resource(OneLeg, '/api/legislators/<int:leg_id>')