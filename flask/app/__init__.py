from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
from app import views
from app.api import *
api = Api(app)


api.add_resource(AllBills, '/api/bills', '/api/bills/')
api.add_resource(AllLeg, '/api/legislators', '/api/legislators/')
api.add_resource(OneBill, '/api/bills/<int:bill_id>', '/api/bills/<int:bill_id>/')
api.add_resource(OneLeg, '/api/legislators/<int:leg_id>', '/api/legislators/<int:leg_id>/')
api.add_resource(TestResource, '/test')
api.add_resource(Pokemon, '/api/pokemon/<int:id>')
