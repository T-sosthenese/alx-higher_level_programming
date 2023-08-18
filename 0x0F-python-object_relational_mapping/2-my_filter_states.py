#!/usr/bin/python3
"""
Displays all values in the states table of database hbtn_0e_0_usa
where the name matches the provided argument.
Usage: ./2-my_filter_states.py <mysql username>
                               <mysql password>
                               <database name>
                               <state name searched>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:S}' ORDER BY id ASC".
                format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
