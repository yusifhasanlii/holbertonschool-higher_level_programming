#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
This script takes 3 arguments: mysql username, mysql password
and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Terminaldan gələn arqumentləri götürürük
    # argv[0] faylın adıdır, buna görə 1, 2 və 3-dən başlayırıq
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Bazaya qoşulma parametrləri
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Sorğu icra etmək üçün cursor yaradırıq
    cursor = db.cursor()

    # SQL sorğusu: Bütün ştatları id üzrə artan sıra ilə seçirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Nəticələri əldə edirik
    query_rows = cursor.fetchall()

    # Hər bir sətiri tələb olunan formatda çap edirik
    for row in query_rows:
        print(row)

    # Bağlantıları təmiz şəkildə qapadırıq
    cursor.close()
    db.close()
