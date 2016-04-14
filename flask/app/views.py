from app.models import *
from flask import render_template, jsonify
from app import app
from flask import make_response
from flask_restful import Resource, Api
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+pymysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
@app.route('/index/')
@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/legislators/')
@app.route('/legislators.html')
def people_page():

	return render_template("legislators.html")

@app.route('/about/')
@app.route('/about.html')
def about():
	data = open('about.txt').read()
	group = json.loads(data)
	return render_template("about.html", group = group)


@app.route('/bills/')
@app.route('/bills.html')
def bills_page():

	return render_template("bills.html")

@app.route('/pokemon/')
@app.route('/pokemon.html')
def pokemon_page():

	return render_template("pokemon.html")

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
	# assoc_query = session.query(Legislator, SponsorBillAssociation).join(SponsorBillAssociation).filter(Legislator.id == person_id)

	# the sponsor bill association is the second tuple.
	# assoc_obj = assoc_query.first()[1]
	# assoc_obj_dict = assoc_obj.__dict__
	# assoc_dict = assoc_result.__dict__
	# print(type(leg_obj))
	# print(type(assoc_obj))


	spon_query = session.query(SponsorBillAssociation).filter_by(leg_id=person_id).filter_by(type_of_sponsorship='sponsor')
	spon_dict_list = [x.__dict__ for x in spon_query]

	# TODO: query db for cosponsored bills
	cospon_query = session.query(SponsorBillAssociation).filter_by(leg_id=person_id).filter_by(type_of_sponsorship='cosponsor')
	cospon = [x.__dict__ for x in cospon_query]
	return render_template('legislators_template.html', person = leg_dict, sponsored_bill_association = spon_dict_list,cosponsored_bill_association=cospon)
	# return render_template('legislators_template.html', person = leg_dict, sponsored_bill_association = assoc_obj_dict)


@app.route('/bills/<bill_id>')
def render_bill(bill_id):
	bill_obj = session.query(Bill).filter_by(id=bill_id).first()
	bill_dict = bill_obj.__dict__

	# logic to create tooltip to define what the current status of the bill is 
	if bill_dict['current_status'] == 'referred':
		bill_dict['status_info'] = 'This bill has been passed to committe to debate, research, or amend this bill.'
	elif bill_dict['current_status'] == 'enacted_signed':
		bill_dict['status_info'] = 'This bill is part of the law'
	elif bill_dict['current_status'] == 'pass_over_house':
		bill_dict['status_info'] = 'This bill has been passed in the House.'
	elif bill_dict['current_status'] == 'reported':
		bill_dict['status_info'] = 'A committee has formally submitted this bill to its parent chamber/comittee.'
	elif bill_dict['current_status'] == 'pass_over_senate':
		bill_dict['status_info'] = 'This bill has been passed in the Senate.'
	elif bill_dict['current_status'] == 'passed_simpleres':
		bill_dict['status_info'] = 'This resolution does not have the force of the law and affects just the chamber of Congress.'
	elif bill_dict['current_status'] == 'passed_concurrentres':
		bill_dict['status_info'] = 'This resolution does not have the force of the law and affects both the House and the Senate. It is used for matters that affect the rules of Congress or to express the sentiment of Congress.'


	bill_dict['current_status'] = bill_dict['current_status'].replace('_', ' ')

	# querying for a sponsor
	spon_query = session.query(Legislator, SponsorBillAssociation).join(SponsorBillAssociation).filter(SponsorBillAssociation.bill_id==bill_id).filter(SponsorBillAssociation.type_of_sponsorship=='sponsor').first()

	if spon_query:
		spon_dict = spon_query[1].__dict__
		spon_query_name_dict = spon_query[0].__dict__
		name = spon_query_name_dict['firstname'] + " " + spon_query_name_dict['lastname']
		bill_dict['sponsor'] = {'id': spon_dict['leg_id'] , 'name':name}
	else :
		bill_dict['sponsor'] = None

	cospon_query = session.query(Legislator, SponsorBillAssociation).join(SponsorBillAssociation).filter(SponsorBillAssociation.bill_id==bill_id).filter(SponsorBillAssociation.type_of_sponsorship=='cosponsor').all()
	if cospon_query:
		cospon_dict_list = [x[0].__dict__ for x in cospon_query]

		cospon_dict_list_abbr = [{"name" : x["firstname"] +" " +x["lastname"], 'id':x["id"]} for x in cospon_dict_list]
		bill_dict['cosponsor'] = cospon_dict_list_abbr
	else:
		bill_dict['cosponsor'] = None

	return render_template('bills_template.html', bill = bill_dict)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html')
