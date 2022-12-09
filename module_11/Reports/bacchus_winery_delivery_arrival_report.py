import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "team_indigo",
    "password": "pokemon",
    "host": "127.0.0.1",
    "database": "bacchuswinery",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()


def show_sales(cursor, title):
    cursor.execute("""SELECT CONCAT(MONTHNAME(expected_delivery_dt), " ", year(expected_delivery_dt)) as 'Month',
SUM(-1 * datediff(expected_delivery_dt,actual_delivery_dt)) as 'Total Days Late',
count(*) as 'Number of Orders'
FROM inbound_orders
GROUP BY year(expected_delivery_dt), MONTH;""")

    deliveries = cursor.fetchall()

    print("\n      -- {} --".format(title))

    for delivery in deliveries:
        print("==============================================="
              + "\nMonth:           {}\n# of Orders:     {}\nTotal Days Late: {}".format(delivery[0],
                                                                            delivery[2],
                                                                            delivery[1],
                                                                            ))
    print("===============================================")


show_sales(cursor, " Displaying Delivery Report ")

db.close()
