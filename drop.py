import os
import getpass

user = str(getpass.getuser())
drop = "'-c drop database preodator'"
create = "'-c create database preodator'"
postgres = "'/Applications/Postgres.app/Contents/Versions/9.6/bin'/psql -p5432 "

os.system(postgres + drop)
os.system(postgres + create)
os.system("psql -U " + user + " -d preodator -a -f db.sql")
os.system("python gen.py")
os.system(postgres)
