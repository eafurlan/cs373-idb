from flask import render_template
from app import app


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
