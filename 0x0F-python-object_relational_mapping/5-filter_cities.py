#!/usr/bin/python3
"""
Module for lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    code = """SELECT cities.name FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
    cur.execute(code, (argv[4], ))
    results = cur.fetchall()
    resultlist = list(ele[0] for ele in results)
    print(*resultlist, sep=", ")
    cur.close()
    conn.close()
