from flask import (Flask, render_template, jsonify, request)
import mariadb
# import db_model

app = Flask(__name__)

conn = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='cs340',
    password='collector',
    database='cartridge_collector'
)
cur = conn.cursor()

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/api", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_api_call():
    # JSON response
    if request.method == 'GET':
        # Get requested table/filter
        return jsonify({'game_id': 1, 'email': 'mannijac@oregonstate.edu', 'screen_name': 'mannijac', 'country_code': '001'})
    elif request.method == 'POST':
        # Create new entry based on request body
        return
    elif request.method == 'PUT':
        # Update existing Entry
        return
    elif request.method == 'DELETE':
        # Delete entry
        return

if __name__ == "__main__":
    app.run(port='9191', host='0.0.0.0')
