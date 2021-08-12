#!/usr/bin/python3

""" that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
  host="localhost",
  user="user",
  password="password",
db="database")

mycursor = db.cursor()

mycursor.execute("SELECT * FROM states ORDER by id")

myresult = mycursor.fetchall()
for row in myresult:
    print(states.id, row )
