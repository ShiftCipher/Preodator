import names
import sys
import random
import time
import datetime
import psycopg2

def factory_users():
    # Users Factory
    for i in range(1, 1001):
        name = 'User' + str(i)
        dni = '000000' + str(random.randrange(1, 300))
        phone = '013' + dni
        email = name.lower() + '@aol.com'
        db.execute("INSERT INTO users (dni, name, phone, email) VALUES (%s, %s, %s, %s)",
        (dni, name, phone, email))

def factory_receipts():
    # Receipt Factory
    for i in range(1, 1001):
        user_id = str(random.randrange(100, 250))
        db.execute("INSERT INTO receipts (user_id) VALUES (%s)",(user_id,))

def factory_redemptions():
    # Redemption Factory
    for i in range(1, 251):
        user_id = random.randrange(1, 1000)
        reward_id = random.randrange(1, 11)
        db.execute("INSERT INTO redemptions (user_id, reward_id) VALUES (%s, %s)",
        (user_id, reward_id))

def factory_rewards():
    # Rewards Factory
    for i in range(1, 11):
        name = "Reward0" + str(i)
        price = random.randrange(30000, 200000)
        db.execute("INSERT INTO rewards (name, price) VALUES (%s, %s)",
        (name, price))

def factory_venues():
    # Rewards Venues
    for i in range(1, 11):
        name = "Venue0" + str(i)
        db.execute("INSERT INTO venues (name) VALUES (%s)",
        (name,))

con = psycopg2.connect("dbname=preodator user=imac")
db = con.cursor()
factory_users()
factory_receipts()
factory_venues()
factory_rewards()
factory_redemptions()

con.commit()
con.close()
