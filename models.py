import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

from sqlalchemy import Table, ForeignKey, Column, Integer, String

class SponsorBillAssociation(Base):
	__tablename__ = 'sponsor_bill_association'
	bill_id = Column(Integer, ForeignKey('bills.id'), primary_key=True)
	leg_id = Column(Integer, ForeignKey('legislators.id'), primary_key=True)

	# Put info unique to each Cosponsor / Bill association here

	# type_of_sponsorship is either "Sponsor" or "Cosponsor"
	type_of_sponsorship = Column(String)

	# Express associations
	legislator = relationship("Legislator", back_populates="sponsored_bills")
	bill = relationship("Bill", back_populates="sponsors")

class Bill(Base):
	__tablename__ = 'bills'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	current_stats = Column(String)
	bill_type = Column(String)

	sponsors = relationship("SponsorBillAssociation", back_populates="bill")

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

