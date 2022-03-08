from flask import (Flask, render_template, jsonify, request)
import mariadb
import models

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/api", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_api_call():
    # JSON response
    print (request.form)
    table_name = request.form['table_name']
    table_keys = request.form['table_keys']
    table_values = request.form['table_values']

    if request.method == 'GET':
        # Get requested table/filter
        return 
    elif request.method == 'POST':
        # Create new entry based on request body
        models.insert(table_name, table_keys, table_values)
        return
    elif request.method == 'PUT':
        # Update existing Entry
        return
    elif request.method == 'DELETE':
        # Delete entry
        return

if __name__ == "__main__":
    app.run(port='9191', host='0.0.0.0')
