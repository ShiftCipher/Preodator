import names
import sys
import random
import time
import datetime

for i in range(1, 1001):
    name = "User0" + str(1)
    dni = "000000" + str(random.randrange(1, 300))
    phone = "013" + dni
    email = name.lower() + "@aol.com"
    date = str(datetime.datetime.utcnow())
    print dni + ", " + name + ", " + phone + ", " + email + ", " + date

for i in range(1, 1001):
    dni = "000000" + str(random.randrange(1, 300))
    date = str(datetime.datetime.utcnow())
    print dni + ", " + date

for i in range(1, 251):
    dni = "000000" + str(random.randrange(1, 300))
    reward = str(random.randrange(1, 11))
    date = str(datetime.datetime.utcnow())
    print dni + ", " + reward + ", " + date

for i in range(1, 11):
    name = "Reward0" + str(i)
    date = str(datetime.datetime.utcnow())
    price = str(random.randrange(30000, 200000))
    print name + ", " + price + ", " + date

for i in range(1, 11):
    name = "Venue0" + str(i)
    print name + ", " + date
