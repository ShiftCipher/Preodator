import os
import psycopg2
from flask import Flask

pg = psycopg2.connect("dbname=preodator user=preo")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/users")
def users_all():
    return "Users"

@app.route("/receipts")
def receipts_all():
    return "Receipts"

@app.route("/redemptions")
def redemptions_all():
    return "Redemptions"

@app.route("/rewards")
def rewards_all():
    return "Rewards"

@app.route("/venues")
def venues_all():
    return "Venues"

if __name__ == "__main__":
    app.run()
