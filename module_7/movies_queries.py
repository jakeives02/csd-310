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

# Module 7 queries

cursor = db.cursor()

print("===========ALL STUDIO RECORDS============")
cursor.execute("SELECT * FROM studio")
studio = cursor.fetchall()
for rows in studio:
    print("Studio ID: {}\n Studio Name: {}\n".format(rows[0], rows[1]))
print("=========================================\n")


print("===========ALL GENRE RECORDS=============")
cursor.execute("SELECT * FROM genre")
genre = cursor.fetchall()
for rows in genre:
    print("Genre ID: {}\n Genre Name: {}\n".format(rows[0], rows[1]))
print("=========================================\n")


print("===FILMS WITH RUNTIME LESS THAN 2 HOURS===")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
film = cursor.fetchall()
for rows in film:
    print("Film Name: {}\n Runtime: {}\n".format(rows[0], rows[1]))
print("=========================================\n")

print("=====FILMS GROUPED BY DIRECTOR===========")
cursor.execute("SELECT film_name, film_director FROM film order by film_director")
film = cursor.fetchall()
for rows in film:
    print("Film Name: {}\n Director: {}\n".format(rows[0], rows[1]))
print("=========================================\n")

db.close()

