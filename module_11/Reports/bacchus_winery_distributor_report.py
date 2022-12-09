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
    
def show_sellers(cursor, title):	
	
    cursor.execute("""SELECT distribution.distributor_name AS Distributor, item.item_name AS "Type of Wine" 
                    FROM outbound_orders 
                    INNER JOIN item ON outbound_orders.item_no = item.item_no 
                    INNER JOIN distribution ON outbound_orders.distributor_id = distribution.distributor_id 
                    GROUP BY distributor_name, item_name;""")

    sellers = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for seller in sellers:
        print("Distributor: {}\nTypes of Wine YTD: {}\n".format(seller[0], seller[1]))
show_sellers(cursor, "--Displaying Sellers Report--")

db.close()