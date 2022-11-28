import mysql.connector
from mysql.connector import errorcode
# Jacob Ives 11/27/2022 - Run queries using Python
config = {
    "user": "Jake",
    "password": "root",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL host {} with database {}".format(config["user"], config["host"],
                                                                                   config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


def show_films(cursor, title):
    cursor.execute("SELECT film_name as 'Name', film_director as 'Director', genre_name as 'Genre', "
                   "studio_name as 'Studio' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id "
                   "INNER JOIN studio on film.studio_id = studio.studio_id")
    films = cursor.fetchall()
    print("\n  -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}"
              "\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


def insert_film():
    cursor.execute("INSERT INTO film(film_name, film_releaseDate, " +
                   "film_runtime, film_director, studio_id, genre_id) " +
                   " VALUES('Minions', '2015', '91', 'Pierre Coffin', 3, 3 )")


def update_film():
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")


def delete_film():
    cursor.execute("DELETE FROM film where film_name = 'Gladiator'")


cursor = db.cursor()
show_films(cursor, "DISPLAYING FILMS ORIGINAL")
insert_film()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
update_film()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")
delete_film()
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
db.close()
