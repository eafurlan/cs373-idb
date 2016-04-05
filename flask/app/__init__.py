from flask import Flask
import subprocess
import os
from flask_restful import Api, Resource


app = Flask(__name__)
from app import views
from app.api import *
api = Api(app)

class TestResource(Resource):
    def get(self):
        try:
            output_text = subprocess.check_output('python3 ./../tests.py',
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                
                shell=True)
            # Runs from the flask directory
            return {'test_text\n': str(output_text)}
        except subprocess.CalledProcessError:
            return {'test_text':'The process returned with an error'}
        except subprocess.TimeoutExpired:
            return {'test_text':'The tests took too long to run. Check the server'}
        #except:
        #    return {'test_text':'something unkown went wrong trying to run the tests'}

api.add_resource(TestResource,'/test')

api.add_resource(AllBills, '/api/bills', '/api/bills/')
api.add_resource(AllLeg, '/api/legislators', '/api/legislators/')
api.add_resource(OneBill, '/api/bills/<int:bill_id>', '/api/bills/<int:bill_id>/')
api.add_resource(OneLeg, '/api/legislators/<int:leg_id>', '/api/legislators/<int:leg_id>/')

    
