#!/usr/bin/python3
"""Module For list all states from database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    code = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(code)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
