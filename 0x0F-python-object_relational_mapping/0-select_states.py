#!/usr/bin/python3
"""
Lists all states in hbtn_0e_0_usa.
Takes 3 args(mysql username, mysql password, database name).
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
