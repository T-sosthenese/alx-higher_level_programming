#!/usr/bin/python3
"""
Lists all states from hbtn_0e_0_usa database starting with N.
Usage: ./1-filter_states.py <mysql username>\
                            <mysql password>\
                            <database name>
"""

import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],\
                         host='localhost', port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cur.execute(query)
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
