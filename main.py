import os
import json
import pandas
import getpass
import datetime
import psycopg2
from flask import Flask, request, Response

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

@app.route("/login", methods=['POST'])
def login():
    print request.method
    print request.form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print email
        print password
        user = cur.execute("SELECT * FROM admins WHERE data->>'email' = %s AND data->>'password' = %s",
        (email, password))
        user = cur.fetchone()
        user = json.dumps(user, default=datetime_handler)
        return user

@app.route("/users")
def users_all():
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    users = json.dumps(users, default=datetime_handler)
    return users

@app.route("/campaigns", method=['GET'])
def campaigns_all():
    cur.execute("SELECT * FROM campaigns;")
    campaings = cur.fetchall()
    campaings = json.dumps(campaings, default=datetime_handler)
    return campaings

@app.route("/receipts")
def receipts_all():
    receipts = cur.execute("SELECT * FROM receipts;")
    receipts = cur.fetchall()
    receipts = json.dumps(receipts, default=datetime_handler)
    return receipts

@app.route("/redemptions")
def redemptions_all():
    cur.execute("SELECT * FROM redemptions;")
    redemptions = cur.fetchall()
    redemptions = json.dumps(redemptions, default=datetime_handler)
    return str(redemptions)

@app.route("/rewards")
def rewards_all():
    cur.execute("SELECT data FROM rewards;")
    rewards = cur.fetchall()
    rewards = json.dumps(rewards, default=datetime_handler)
    return rewards

@app.route("/venues")
def venues_all():
    cur.execute("SELECT data FROM venues;")
    venues = cur.fetchall()
    venues = json.dumps(venues, default=datetime_handler)
    return venues

if __name__ == "__main__":
    app.run()
