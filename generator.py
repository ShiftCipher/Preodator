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
        cur.execute("INSERT INTO users (dni, name, phone, email) VALUES (%s, %s, %s, %s)",
        (dni, name, phone, email))

def factory_receipts():
    # Receipt Factory
    for i in range(1, 1001):
        userID = str(random.randrange(1, 1000))
        cur.execute("INSERT INTO receipts (userID) VALUES (%s)",(userID,))

def factory_redemptions():
    # Redemption Factory
    for i in range(1, 251):
        userID = random.randrange(1, 1000)
        rewardID = random.randrange(1, 11)
        cur.execute("INSERT INTO redemptions (userID, rewardID) VALUES (%i, %i)",
        (userID, rewardID))

def factory_rewards():
    # Rewards Factory
    for i in range(1, 11):
        name = "Reward0" + str(i)
        price = random.randrange(30000, 200000)
        cur.execute("INSERT INTO rewards (name, price) VALUES (%s, %i)",
        (name, price))

def factory_venues():
    # Rewards Venues
    for i in range(1, 11):
        name = "Venue0" + str(i)
        cur.execute("INSERT INTO venues (name) VALUES (%s)",
        (name))

conn = psycopg2.connect("dbname=preodator user=imac")
cur = conn.cursor()
factory_users()
factory_receipts()
factory_redemptions()
factory_rewards()
factory_venues()
conn.commit()
cur.close()
conn.close()
