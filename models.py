import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

from sqlalchemy import Table, ForeignKey, Column, Integer, String

def model_repr(yourself):
	val = "%s:\n" % (yourself.__class__)
	def stupid(you):
		for attr, value in yourself.__dict__.items():
			yield attr, value
	val =  "".join([str((a,b)) for a,b in stupid(yourself) if not a.startswith('__') and not callable(getattr(yourself,a))])
	val = val + "\n%s\n" % (str (('__tablename__',yourself.__tablename__)) )
	return val


'''
SponsorBillAssociation object expresses the many-to-many relationship between Bills and Legislators.
Expresses sponsorship or co-sponsorship as an attribute of each relationship.
'''

class SponsorBillAssociation(Base):
	__tablename__ = 'sponsor_bill_association'
	bill_id = Column(Integer, ForeignKey('bills.id'), primary_key=True)
	leg_id = Column(Integer, ForeignKey('legislators.id'), primary_key=True)

	# Put info unique to each Cosponsor / Bill association here

	# Type_of_sponsorship is either "Sponsor" or "Cosponsor"
	type_of_sponsorship = Column(String)

	# Express associations
	legislator = relationship("Legislator", back_populates="sponsored_bills")
	bill = relationship("Bill", back_populates="sponsors")

	def __repr__(self):
		return model_repr(self)

'''
Bill object represents a bill in the legislative system.
Has associated attributes, such as name and status.
Contains 'sponsors' which is a list of Legislator objects.
'''
class Bill(Base):
	__tablename__ = 'bills'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	current_status = Column(String)
	bill_type = Column(String)

	sponsors = relationship("SponsorBillAssociation", back_populates="bill")

	def __init__(self, id=None, name=None, current_status=None, bill_type=None, sponsors=[]):
		self.id = id
		self.name = name
		self.current_status = current_status
		self.bill_type = bill_type
		self.sponsors = sponsors

	def __repr__(self):
		return model_repr(self)

'''
Legislator object represents a legislator in the legislative system.
Has associated attributes, such as name, party, and role.
Contains 'sponsored_bills' which is a list of Bill objects.
'''
class Legislator(Base):
	__tablename__ = 'legislators'

	id = Column(Integer, primary_key=True)
	firstname = Column(String)
	lastname = Column(String)
	party = Column(String)
	description = Column(String)
	title = Column(String)
	state = Column(String)
	birthday = Column(String)
	twitter = Column(String)
	youtube = Column(String)
	start_date = Column(String)
	website = Column(String)

	sponsored_bills = relationship("SponsorBillAssociation", back_populates="legislator")

	def __init__(self, id=None, firstname=None, lastname=None, party=None, description=None, title=None, state=None, birthday=None, twitter=None, youtube=None, start_date=None, website=None, sponsored_bills=[]):
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
		self.start_date = start_date
		self.website = website
		self.sponsored_bills = sponsored_bills

	def __repr__(self):
		return model_repr(self)
