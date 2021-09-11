#!/usr/bin/python3

""" that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine


if __name__ == '__main__':
    
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
  host="localhost",
        port="3306",
  user="user",
  password="password",
db="database")

x = db.query(states).order_by(states.id)

connection = my_conn.execute(x)
my_data=connection.fetchall()
for row in my_data:
    print(row)
