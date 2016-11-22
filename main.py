import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return json.dumps({'Hello': 7, 'World': 7}, sort_keys=True,
    indent=4, separators=(',', ': '))

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
