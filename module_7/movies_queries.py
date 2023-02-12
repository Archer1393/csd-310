# Matthew Archer
# 2/12/2023
# Module 7 Assignment

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#########################################################################
# Query 1
cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio")
movies = cursor.fetchall()

print()

print("-- DISPLAYING Studio RECORDS --")
for studio in movies:
    print("Studio ID: {}".format(studio[0]))
    print("Studio Name: {}\n".format(studio[1]))

#########################################################################
# Query 2
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre")
movies = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")
for genre in movies:
    print("Genre ID: {}".format(genre[0]))
    print("Genre Name: {}\n".format(genre[1]))

#########################################################################
# Query 3
cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film")
movies = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")
for film in movies:
    if film[1] < 120:
        print("Film Name: {}".format((film[0])))
        print("Runtime: {}\n".format(film[1]))

#########################################################################
# Query 4
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film")
movies = cursor.fetchall()

k = 0

print("-- DISPLAYING Director RECORDS in Order --")
for i in movies:
    for j in movies:
        if j[1] < i[1]:
            if k == 1:
                continue
            else:
                print("Film Name: {}".format((j[0])))
                print("Director: {}\n".format((j[1])))
                k += 1

        elif i[1] < j[1]:
            print("Film Name: {}".format((j[0])))
            print("Director: {}\n".format((j[1])))

db.close()
