from flask import render_template
from app import app
import json

data = open('../people.txt').read()
people = json.loads(data)

data = open('../bills.txt').read()
bills = json.loads(data)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    
    return render_template("index.html")

@app.route('/people')
@app.route('/people.html')
def bills():
    
    return render_template("people.html")

@app.route('/about')
@app.route('/about.html')
def about():
    
    return render_template("about.html")

@app.route('/people/400034')
def render_person1():
    return render_template('people_template.html', person=people[0])

@app.route('/people/400040')
def render_person2():
    return render_template('people_template.html', person=people[1])

@app.route('/people/400054')
def render_person3():
    return render_template('people_template.html', person=people[2])

@app.route('/bills/127131')
def render_bill1():
	return render_template('bills_template.html', bill=bills[0])

@app.route('/bills/127130')
def render_bill2():
	return render_template('bills_template.html', bill=bills[1])

@app.route('/bills/127129')
def render_bill3():
	return render_template('bills_template.html', bill=bills[2])

