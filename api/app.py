from flask import Flask, request, jsonify
import pandas as pd
from api.databse import DatabaseHandelr
import json
from datetime import date, datetime
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app) #comment this on deployment
api = Api(app)

# to run flask npm run start-flask 
def ready_data():
    obj = DatabaseHandelr()
    data = obj.select_function()
    return data



@app.route('/', methods=["GET"])
def api():
    data= ready_data()
    
   

    return json_response(data)
def json_response(payload, status=200):
     return (json.dumps(payload,default=str), status, {'content-type': 'application/json'})
def myconverter(o):
    if isinstance(o, datetime.date, datetime.datetime):
        return o.__str__()




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug= False)