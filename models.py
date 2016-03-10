import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

from sqlalchemy import Table, ForeignKey, Column, Integer, String

class CosponsorBillAssociation(Base):
	__tablename__ = 'cosponsor_bill_association'
	bill_id = Column(Integer, ForeignKey('bills.id'), primary_key=True)
	leg_id = Column(Integer, ForeignKey('legislators.id'), primary_key=True)

	# Put info unique to each Cosponsor / Bill association here

	# Express associations
	legislator = relationship("Legislator", back_populates="cosponsored_bills")
	bill = relationship("Bill", back_populates="cosponsors")

class Bill(Base):
	__tablename__ = 'bills'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	current_stats = Column(String)
	bill_type = Column(String)
	sponsor = Column(String)

	cosponsors = relationship("CosponsorBillAssociation", back_populates="bill")

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

	cosponsored_bills = relationship("CosponsorBillAssociation", back_populates="legislator")

