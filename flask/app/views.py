from flask import render_template
from app import app
import json

data = open('../people.txt').read()
people = json.loads(data)

data1 = open('../bills.txt').read()
bills = json.loads(data1)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/people')
@app.route('/people.html')
def people_page():
    
    return render_template("people.html")

@app.route('/about')
@app.route('/about.html')
def about():
    
    return render_template("about.html")

@app.route('/bills')
@app.route('/bills.html')
def bills_page():
    
    return render_template("bills.html")

@app.route('/people/412378')
def render_person1():
    return render_template('people_template.html', person=people[0])

@app.route('/people/412542')
def render_person2():
    return render_template('people_template.html', person=people[1])

@app.route('/people/412493')
def render_person3():
    return render_template('people_template.html', person=people[2])

@app.route('/bills/334618')
def render_bill1():
	return render_template('bills_template.html', bill=bills[0])

@app.route('/bills/336967')
def render_bill2():
	return render_template('bills_template.html', bill=bills[1])

@app.route('/bills/13153')
def render_bill3():
	return render_template('bills_template.html', bill=bills[2])

