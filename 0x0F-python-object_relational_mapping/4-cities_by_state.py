#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <user> <passwd> <database>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              INNER JOIN states ON state_id = states.id")
    mydata = c.fetchall()
    for row in mydata:
        print(row)
    c.close()
    db.close()
