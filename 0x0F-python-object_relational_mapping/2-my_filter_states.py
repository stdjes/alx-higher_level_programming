#!/usr/bin/python3
"""
Module for displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    code = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cur.execute(code.format(argv[4]))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
