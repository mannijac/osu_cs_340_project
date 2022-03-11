from flask import (Flask, render_template, jsonify, request)
import mariadb
from DBModel import *

app = Flask(__name__)
db_model = DBModel()

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/api", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_api_call():
    # JSON response
    print(request.json)
    table_attributes = {}
    # Store and preprocess strings with quotations for SQL insertion
    # Add input sanitation code here to prevent sql injections
    for att in request.json:
        if att != 'table_name':
            table_attributes[att] = '"' + request.json[att] + '"'
    
    # Handle requests
    if request.method == 'GET':
        # Get requested table/filter
        if request.args.get('table_name') != None:
             return jsonify(db_model.read(request.args.get('table_name'))
             
    elif request.method == 'POST':
        # Create new entry based on request body
        table_name = request.json['table_name']
        return jsonify(db_model.create(table_name, table_attributes.keys(), table_attributes.values()))
    elif request.method == 'PUT':
        # Update existing Entry
        return
    elif request.method == 'DELETE':
        # Delete entry
        return

if __name__ == "__main__":
    app.run(port='9111', host='0.0.0.0')
