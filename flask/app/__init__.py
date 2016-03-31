from flask import Flask
import subprocess
import os
from flask_restful import Api, Resource

app = Flask(__name__)
from app import views

api = Api(app)

class TestResource(Resource):
    def get(self):
        try:
            output_text = subprocess.check_output('python3 ./../tests.py',
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                
                shell=True)
            # Runs from the flask directory
            return {'test_text': str(output_text)}
        except subprocess.CalledProcessError:
            return {'test_text':'The process returned with an error'}
        except subprocess.TimeoutExpired:
            return {'test_text':'The tests took too long to run. Check the server'}
        #except:
        #    return {'test_text':'something unkown went wrong trying to run the tests'}

api.add_resource(TestResource,'/test')

    
