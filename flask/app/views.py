from app.models import *
from flask import render_template, jsonify
from app import app
from flask import make_response
import subprocess
import os

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+pymysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()

data = open('about.txt').read()
group = json.loads(data)

@app.route('/')
@app.route('/index/')
@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/legislators/')
@app.route('/legislators.html')
def people_page():
	
	return render_template("people.html")

@app.route('/about/')
@app.route('/about.html')
def about():
	
	return render_template("about.html", group = group, output_text = runTests())

def runTests():
	try:
		
		path = os.path.dirname(os.path.realpath(__file__))
		process = subprocess.Popen('python3 ' +path+'/tests.py', shell=True,
					   stdout=subprocess.PIPE, 
					   stderr=subprocess.PIPE)
		# Runs from the flask directory
		output_text, err = process.communicate()
	  	
		output = {'results': err.decode('utf-8'), 'output': output_text.decode('utf-8')}

		return output
	except subprocess.CalledProcessError:
		return {'results':'The process returned with an error'}
	except subprocess.TimeoutExpired:
		return {'results':'The tests took too long to run. Check the server'}

@app.route('/bills/')
@app.route('/bills.html')
def bills_page():
	
	return render_template("bills.html")

@app.route('/legislators/<person_id>')
def render_person(person_id):
	leg_query = session.query(Legislator).filter_by(id=person_id)
	leg_obj = leg_query.first()
	leg_dict = leg_obj.__dict__

	#IGNORE THIS STUFFz
	# query_assoc = session.query(Legislator, SponsorBillAssociation).join(SponsorBillAssociation)
	# first_tuple = query_assoc.first()
	# print(first_tuple)
	# print(type(leg_obj))
	# print(type(query_assoc))

	# this would find the id of first bill that this leg sponsord
	assoc_query = session.query(Legislator, SponsorBillAssociation).join(SponsorBillAssociation).filter(Legislator.id == person_id)
	
	# the sponsor bill association is the second tuple.
	assoc_obj = assoc_query.first()[1]
	assoc_obj_dict = assoc_obj.__dict__
	# assoc_dict = assoc_result.__dict__
	# print(type(leg_obj))
	# print(type(assoc_obj))



	return render_template('people_template.html', person = leg_dict, sponsored_bill_association = assoc_obj_dict)

@app.route('/bills/<bill_id>')
def render_bill(bill_id):
	bill_obj = session.query(Bill).filter_by(id=bill_id).first()
	bill_dict = bill_obj.__dict__
	print(str(bill_dict))
	return render_template('bills_template.html', bill = bill_dict)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html')
