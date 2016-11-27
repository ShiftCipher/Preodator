import os
import getpass
import json
import datetime
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
user = str(getpass.getuser())
con = "dbname=preodator user=" + user

con = psycopg2.connect(con)
cur = con.cursor()

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

@app.route("/")
def hello():
    return "Preodator"

@app.route("/users")
def users_all():
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    users = json.dumps(users, default=datetime_handler)
    return jsonify(str(users))

@app.route("/receipts")
def receipts_all():
    receipts = cur.execute("SELECT * FROM receipts;")
    receipts = cur.fetchall()
    return str(receipts)

@app.route("/redemptions")
def redemptions_all():
    cur.execute("SELECT * FROM redemptions;")
    redemptions = cur.fetchall()
    return str(redemptions)

@app.route("/rewards")
def rewards_all():
    cur.execute("SELECT * FROM rewards;")
    rewards = cur.fetchall()
    return str(rewards)

@app.route("/venues")
def venues_all():
    cur.execute("SELECT * FROM venues;")
    venues = cur.fetchall()
    return str(venues)

if __name__ == "__main__":
    app.run()
