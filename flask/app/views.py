from app.models import Bill, Legislator
from flask import render_template, jsonify
from app import app

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


data = open('people.txt').read()
people = json.loads(data)

data1 = open('bills.txt').read()
bills = json.loads(data1)

engine = create_engine('mysql://dev1:swesquad@172.99.70.111:3306/ildb_prod')
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
@app.route('/index/')
@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/people/')
@app.route('/people.html')
def people_page():
	
	return render_template("people.html")

@app.route('/about/')
@app.route('/about.html')
def about():
	
	return render_template("about.html")

@app.route('/bills/')
@app.route('/bills.html')
def bills_page():
	
	return render_template("bills.html")

@app.route('/people/<person_id>')
def render_person(person_id):
	leg_obj = session.query(Legislator).filter_by(id=person_id).first()
	leg_dict = leg_obj.__dict__
	return render_template('people_template.html', person = leg_dict)

@app.route('/bills/<bill_id>')
def render_bill(bill_id):
	bill_obj = session.query(Bill).filter_by(id=bill_id).first()
	bill_dict = bill_obj.__dict__
	return render_template('bills_template.html', bill = bill_dict)

# @app.route('/bills/343921')
# def render_bill1():
#   return render_template('bills_template.html', bill=bills[0])

# @app.route('/bills/336967')
# def render_bill2():
#   return render_template('bills_template.html', bill=bills[1])

# @app.route('/bills/343960')
# def render_bill3():
#   return render_template('bills_template.html', bill=bills[2])

