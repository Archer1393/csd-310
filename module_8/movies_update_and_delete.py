# Matthew Archer
# 2/12/2023
# Module 8 Assignment

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


def show_films(cursor, title):
    # method to execute an inner join on all tables,
        # iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

########################################################################################
# Query 1
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director, genre_id, studio_id FROM film")
movies = cursor.fetchall()

show_films(cursor, "DISPLAYING FILMS")
########################################################################################
# Query 2
cursor = db.cursor()
cursor.execute("INSERT INTO genre (genre_id, genre_name) VALUES (4, 'Action')")
cursor.execute("INSERT INTO studio (studio_id, studio_name) VALUES (4, 'Warner Bros.')")
cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES ('The Dark Knight', 'Christopher Nolan', 4, 4, 2008, 152)")
movies = cursor.fetchall()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
########################################################################################
# Query 3
cursor = db.cursor()
cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
movies = cursor.fetchall()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
########################################################################################
# Query 4
cursor = db.cursor()
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
movies = cursor.fetchall()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()