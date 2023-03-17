#!/usr/bin/python3
""" Script thak takes in an argument and displays all values in the states
    table of 'hbtn_0e_0_usa' where name matches the argument. """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Code that takes an argument and displays all values in the states """
    db = MySQLdb.connect(host="localhost",  # your host
                         user=argv[1],       # username
                         passwd=argv[2],     # password
                         db=argv[3],
                         port=3306)   # name of the database
    cur = db.cursor()

    cur.execute("""SELECT cities.name
                   FROM cities INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC;""", (argv[4],))

    cities = cur.fetchall()
    print(", ".join(row[0] for row in cities))

    cur.close()
