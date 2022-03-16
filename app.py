import re
from flask import (Flask, render_template, jsonify, request)
import mariadb
from DBModel import *
from TableData import table_data as table_data

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
    if request.json is not None:
        for att in request.json:
            if att != 'table_name':
                table_attributes[att] = '"' + str(request.json[att]) + '"'
        
    # Handle requests
    if request.method == 'GET':
        # Get requested table/filter
        if request.args.get('table_name') is not None:
             return jsonify(db_model.read(request.args.get('table_name')))
    elif request.method == 'POST':
        # Create new entry based on request body
        table_name = request.json['table_name']
        return jsonify(db_model.create(table_name, table_attributes.keys(), table_attributes.values()))
    elif request.method == 'PUT':
        # Update existing Entry
        return jsonify(db_model.update(table_name, table_attributes.keys(), table_attributes.values()))
    elif request.method == 'DELETE':
        # Delete entry
        print(table_attributes[])
        if request.json.get('table_name') is None:
            return jsonify({'error': 'table_name is none!' }) 

        table_name = request.json['table_name']
        
        filter = {}
        print(table_name)

        print(table_data[table_name])
        filter_keys = table_data[table_name]['primary_key']
        filter_values = [request.args.get('id')]
                
        for n in range(0, len(filter_keys)):
            filter[filter_keys[n]] = filter_values[n]
        
        return jsonify(db_model.delete(table_name, filter))


if __name__ == "__main__":
    app.run(port='9111', host='0.0.0.0')
