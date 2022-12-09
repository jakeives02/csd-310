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
	
    cursor.execute("""SELECT item.item_name AS "Type of Wine", SUM(outbound_orders.item_count) AS "Bottles Sold YTD" 
                    FROM outbound_orders INNER JOIN item ON outbound_orders.item_no = item.item_no 
                    GROUP BY item_name;""")

    sales = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for sale in sales:
        print("Type of Wine: {}\nBottles Sold YTD: {}\n".format(sale[0], sale[1]))
show_sales(cursor, "--Displaying Wines Sold Report--")

db.close()