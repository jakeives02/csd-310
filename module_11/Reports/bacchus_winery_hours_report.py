"""
Team Indigo
12/07/2022
CSD 310, Milestone 3 1/3 reports
Description: This .py is 1/3 reports that displays information relevant to our case study. This is the employee hours
report that displays each employee with their current hours and hours for the four quarters, or hours for the year.
Each employee is displayed with the least hours to the greatest.
"""
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "team_indigo",
    "password": "pokemon",
    "host": "127.0.0.1",
    "database": "BacchusWinery",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .")
    query = "SELECT first_name As first, last_name As last, current_week AS Current_Hours, hours_YTD AS Hours_YTD " \
            "from employee INNER JOIN work_hours USING(employee_id) ORDER BY hours_YTD; "

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    print("--DISPLAYING EMPLOYEE HOURS REPORT--")
    for row in result:
        print("First Name:", row[0])
        print("Last Name:", row[1])
        print("Current Week Hours:", row[2])
        print("Hours YTD:", row[3])
        print(" ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
