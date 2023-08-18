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
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
