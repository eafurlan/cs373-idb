from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from app.models import *
from app import app
import subprocess
import os
import requests

engine = create_engine('mysql+pymysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()


class AllBills(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('limit', type=int, help="limit must be a number")
		args = parser.parse_args()

		limit = args.get('limit')
		bill_list = []
		if limit is None:
			bill_list = session.query(Bill).all()		
		elif limit > 0:
			bill_list = session.query(Bill).limit(limit)
			
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
		parser = reqparse.RequestParser()
		parser.add_argument('limit', type=int, help="limit must be a number")
		args = parser.parse_args()

		limit = args.get('limit')
		leg_list = []
		if limit is None:
			leg_list = session.query(Legislator).all()
		elif limit >0:
			leg_list = session.query(Legislator).limit(limit)

		
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
	
class TestResource(Resource):
	"""docstring for TestResource"""
	def get(self):
		try:
		
			path = os.path.dirname(os.path.realpath(__file__))
			process = subprocess.Popen('coverage3 run --include ' +path+'/models.py '+ path+'/tests.py && coverage3 report -m', shell=True,
						   stdout=subprocess.PIPE, 
						   stderr=subprocess.PIPE)
			# Runs from the flask directory
			
			output_text, err = process.communicate()
			tmpout = output_text.decode('utf-8')
			tmpout = tmpout.replace('\n','<br/>')
			tmperr = err.decode('utf-8')
			tmperr = tmperr.replace('\n','<br/>')
			test_text = tmpout + "<br/>" + tmperr
			return {'test_text': test_text}
		except subprocess.CalledProcessError:
			return {'test_text':'The process returned with an error'}
		except subprocess.TimeoutExpired:
			return {'test_text':'The tests took too long to run. Check the server'}

class Pokemon(Resource):
	def get(self, id):
		url = 'http://swecune.com/api/pokemon/'+str(id)
		api_response = requests.get(url).json()
		result = []
		result.append(api_response)
		for i in range(3):
			url2 = 'http://swecune.com/api/move/'+str(api_response['moves'][i])
			result.append(requests.get(url2).json())


		return result


			
