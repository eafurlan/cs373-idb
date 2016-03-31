from flask import Flask

from flask_restful import Api, Resource

app = Flask(__name__)
from app import views

api = Api(app)

class TestResource(Resource):
    def get(self):
        return {'test_text':'HELLO LIZ! THE API WORKS'}

api.add_resource(TestResource,'/test')

    
