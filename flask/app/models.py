import sqlalchemy
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#from sawhoosh.model import Base, new_uuid
from flask_sqlalchemy import SQLAlchemy

import flask.ext.whooshalchemy

#from app import app

db = SQLAlchemy()

#Base = declarative_base()

#from sqlalchemy import Table, db.ForeignKey, db.Column, db.Integer, db.String, db.Date

#Boom boom boom boom, boom boom boom boom, baby got that...
class SuperBase(object):

    def model_repr(yourself):
            """
                    model_repr automatically generates the body of __repr__ methods for a class
                    yourself
            """
            val = "%s:\n" % (yourself.__class__)
            def decoration(you):
                    for attr, value in yourself.__dict__.items():
                            yield attr, value
            val =  "".join([str((a,b)) for a,b in stupid(yourself) if not a.startswith('__') and not callable(getattr(yourself,a))])
            val = val + "\n%s\n" % (str (('__tablename__',yourself.__tablename__)) )
            return val

            def __repr__(self):
                return model_repr(self)

class SponsorBillAssociation(db.Model,SuperBase):
	"""
		SponsorBillAssociation object expresses the many-to-many relationship between Bills and Legislators.
		Expresses sponsorship or co-sponsorship as an attribute of each relationship.
	"""
	__tablename__ = 'sponsor_bill_association'
	bill_id = db.Column(db.Integer, db.ForeignKey('bills.id'), primary_key=True)
	leg_id = db.Column(db.Integer, db.ForeignKey('legislators.id'), primary_key=True)

	# Put info unique to each Cosponsor / Bill association here

	# Type_of_sponsorship is either "Sponsor" or "Cosponsor"
	type_of_sponsorship = db.Column(db.String(255))

	# Express associations
	legislator = db.relationship("Legislator", backref=db.backref('sponsored_bills',lazy='dynamic'))
	bill = db.relationship("Bill", backref=db.backref("sponsors",lazy='dynamic'))
        #TODO - add a couple of 

class Bill(db.Model,SuperBase):
	"""
		Bill object represents a bill in the legislative system.
		Has associated attributes, such as name and status.
		Contains 'sponsors' which is a list of Legislator objects.
	"""
	__tablename__ = 'bills'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	current_status = db.Column(db.String(255))
	bill_type = db.Column(db.String(255))
	date = db.Column(db.String(255))
	link = db.Column(db.String(255))

	#sponsors = db.relationship("SponsorBillAssociation", backref=db.backref("bill"))

	def __init__(self, id=None, name=None, current_status=None, bill_type=None, date =None, link=None, sponsors=[]):
		self.id = id
		self.name = name
		self.current_status = current_status
		self.bill_type = bill_type
		self.sponsors = sponsors
		self.date = db.Date
		self.link = link


class Legislator(db.Model,SuperBase):
    """
            Legislator object represents a legislator in the legislative system.
            Has associated attributes, such as name, party, and role.
            Contains 'sponsored_bills' which is a list of Bill objects.
    """

    __tablename__ = 'legislators'
    __searchable__ = ['firstname','lastname']

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    party = db.Column(db.String(255))
    description = db.Column(db.String(255))
    title = db.Column(db.String(255))
    state = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    youtube = db.Column(db.String(255))
    startdate = db.Column(db.String(255))
    website = db.Column(db.String(255))
    photo_link = db.Column(db.String(255))
    bioguide_id = db.Column(db.String(255))

    #sponsored_bills = db.relationship("SponsorBillAssociation", backref=db.backref("legislator"))

    def __init__(self, id=None, firstname=None, lastname=None, party=None, description=None, title=None, state=None, birthday=None, twitter=None, youtube=None, startdate=None, website=None, photo_link = None, sponsored_bills=[], bioguide_id = None):
            self.id = id
            self.firstname = firstname
            self.lastname = lastname
            self.party = party
            self.description = description
            self.title = title
            self.state = state
            self.birthday = birthday
            self.twitter = twitter
            self.youtube = youtube
            self.startdate = startdate
            self.website = website
            self.sponsored_bills = sponsored_bills
            self.photo_link = photo_link
            self.bioguide_id = bioguide_id

