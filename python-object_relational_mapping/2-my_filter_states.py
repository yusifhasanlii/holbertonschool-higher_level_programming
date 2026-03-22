#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided by the user.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Arqumentləri terminaldan götürürük
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Cursor yaradırıq
    cursor = db.cursor()

    # .format() istifadə edərək SQL sorğusunu qururuq
    # BINARY açar sözü böyük/kiçik hərf həssaslığı (case-sensitive) üçündür
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC".format(state_name)

    # Sorğunu icra edirik
    cursor.execute(query)

    # Nəticələri götürürük
    query_rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in query_rows:
        print(row)

    # Bağlantıları qapadırıq
    cursor.close()
    db.close()
