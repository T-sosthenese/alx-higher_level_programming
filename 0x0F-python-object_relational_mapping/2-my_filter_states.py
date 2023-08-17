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
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (state_name,))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
