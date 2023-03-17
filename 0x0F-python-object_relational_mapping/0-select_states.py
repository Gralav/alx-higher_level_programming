#!/usr/bin/python3
""" Script that lists all 'states' from the database hbtn_0e_0_usa
     Results is showed in ascending order by states.id """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Script that liss all states from the database"""
    db = MySQLdb.connect(host="localhost",  # your host
                         user=argv[1],       # username
                         passwd=argv[2],     # password
                         db=argv[3],
                         port=3306)   # name of the database
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
