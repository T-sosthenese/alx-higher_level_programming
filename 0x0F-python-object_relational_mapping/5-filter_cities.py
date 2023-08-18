#!/usr/bin/python3
"""
Lists all cities based on the statename argument.
Usage: <program name> <user> <password> <db> <state to be searched>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    state_names = sys.argv[4]
    c = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON\
             state_id = states.id WHERE states.name = %s"
    c.execute(query, (state_names,))
    mydata = c.fetchall()
    my_cities = ", ".join(my_cities[0] for my_cities in mydata)
    print(my_cities)
    c.close()
    db.close()
