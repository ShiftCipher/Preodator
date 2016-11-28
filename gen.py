import names
import sys
import getpass
import random
import time
import json
import datetime
import psycopg2


# Admins Factory
def factory_admins():
    for i in range(1, 5):
        name = "admin" + str(i)
        dni = "000000" + str(random.randrange(1, 300))
        phone = "013" + dni
        email = name.lower() + '@aol.com'
        password = "123456"
        data = {
        "name" : name,
        "dni" : dni,
        "phone" : phone,
        "email" : email,
        "password" : password
        }
        data = json.dumps(data)
        db.execute("INSERT INTO admins (data) VALUES (%s)",
        (data,))

# Users Factory
def factory_users():
    for i in range(1, 1001):
        name = "user" + str(i)
        dni = "000000" + str(random.randrange(1, 300))
        phone = "013" + dni
        email = name.lower() + '@aol.com'
        password = "123456"
        data = {
        "name" : name,
        "dni" : dni,
        "phone" : phone,
        "email" : email,
        "password" : password
        }
        data = json.dumps(data)
        db.execute("INSERT INTO users (data) VALUES (%s)",
        (data,))

# Receipt Factory
def factory_receipts():
    for i in range(1, 1001):
        user_id = random.randrange(100, 250)
        db.execute("INSERT INTO receipts (user_id) VALUES (%s)",
        (user_id,))

# Redemption Factory
def factory_redemptions():
    for i in range(1, 251):
        user_id = random.randrange(1, 1000)
        reward_id = random.randrange(1, 11)
        position = {
        "latitude" : "-71.060316",
        "longitude" : "48.432044"
        }
        position = json.dumps(position)
        db.execute("INSERT INTO redemptions (user_id, reward_id, position) VALUES (%s, %s, %s)",
        (user_id, reward_id, position))

# Rewards Factory
def factory_rewards():
    for i in range(1, 11):
        data = {
        "name" : "reward0" + str(i),
        "price" : random.randrange(30000, 200000)
        }
        data = json.dumps(data)
        db.execute("INSERT INTO rewards (data) VALUES (%s)",
        (data,))

# Rewards Venues
def factory_venues():
    for i in range(1, 11):
        data = {
        "name" : "venue0" + str(i)
        }
        data = json.dumps(data)
        db.execute("INSERT INTO venues (data) VALUES (%s)",
        (data,))

# Rewards Venues
def factory_campaigns():
    for i in range(1, 10):
        data = {
        "name" : "campaign0" + str(i)
        }
        data = json.dumps(data)
        db.execute("INSERT INTO campaigns (data) VALUES (%s)",
        (data,))

user = str(getpass.getuser())
con = "dbname=preodator user=" + user
con = psycopg2.connect(con)
db = con.cursor()
factory_users()
factory_admins()
factory_receipts()
factory_venues()
factory_rewards()
factory_redemptions()
factory_campaigns()

con.commit()
con.close()
