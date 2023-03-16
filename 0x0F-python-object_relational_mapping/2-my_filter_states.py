#!/usr/bin/python3
""" Script thak takes in an argument and displays all values in the states
    table of 'hbtn_0e_0_usa' where name matches the argument. """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Code that takes in an argument and displays all values in the states
        table of 'hbtn_0e_0_usa' where name matches the argument """
    db = MySQLdb.connect(host="localhost",  # your host
                         user=argv[1],       # username
                         passwd=argv[2],     # password
                         db=argv[3],
                         port=3306)   # name of the database
    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY id ASC;""".format(argv[4]))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
