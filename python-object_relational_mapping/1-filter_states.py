#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Terminal arqumentlərini dəyişənlərə mənimsədirik
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına bağlantı qurulur
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Sorğuları icra etmək üçün cursor obyekti yaradılır
    cursor = db.cursor()

    # SQL sorğusu: 'N' ilə başlayanları seçirik (id üzrə artan sıra ilə)
    # Burada 'BINARY' açar sözü 'N' hərfinin böyük olmasına zəmanət verir
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")

    # Bütün nəticələri əldə edirik
    query_rows = cursor.fetchall()

    # Hər bir sətiri çap edirik
    for row in query_rows:
        print(row)

    # Bağlantıları təmiz şəkildə qapadırıq
    cursor.close()
    db.close()
