"""
Team Indigo
12/3/2022
CSD 310, Milestone 2
Update: bacchus_winery_insert1.4 update: fixed some syntax errors that existed

Concerns: Someone please look into the management INSERT, specifically the management_list[]. I left the end date blank
and do not know what to leave this field as.
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .\n")

    cursor = db.cursor()

    """ ----------------------------------------------- Display Tables ----------------------------------------------"""


    def show_contacts():
        query = "SELECT contact_id, address, city, email, phone, state, zip from contact"
        cursor.execute(query)
        contacts = cursor.fetchall()
        for contact in contacts:
            print("Contact ID: ", contact[0])
            print("Address: ", contact[1])
            print("City: ", contact[2])
            print("Email: ", contact[3])
            print("Phone: ", contact[4])
            print("State: ", contact[5])
            print("Zip: ", contact[6])
            print("  ")


    def show_employees():
        query = "SELECT employee_id, first_name, last_name from employee"
        cursor.execute(query)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee_ID: ", employee[0])
            print("First Name: ", employee[1])
            print("Last Name: ", employee[2])
            print("  ")


    def show_management():
        query = "SELECT mngmt_id, dept_id, employee_id, end_date, start_date from management"
        cursor.execute(query)
        managers = cursor.fetchall()
        for manager in managers:
            print("Management ID: ", manager[0])
            print("Department ID: ", manager[1])
            print("Employee ID: ", manager[2])
            print("End Date: ", manager[2])
            print("Start Date: ", manager[2])
            print("  ")


    def show_work_hours():
        query = "SELECT employee_id, current_week, hours_YTD from work_hours"
        cursor.execute(query)
        hours = cursor.fetchall()
        for hour in hours:
            print("Employee_ID: ", hour[0])
            print("Hours Worked (Current): ", hour[1])
            print("Hours Worked (YTD): ", hour[2])
            print("  ")


    def show_department():
        query = "SELECT dept_id, dept_name, NumOfEmployees from department"
        cursor.execute(query)
        departments = cursor.fetchall()
        for department in departments:
            print("Department_ID: ", department[0])
            print("Department Name: ", department[1])
            print("Number of Employees: ", department[2])
            print("  ")


    def show_payroll():
        query = "SELECT check_no, pay_amount, pay_date, employee_id from payroll"
        cursor.execute(query)
        payrolls = cursor.fetchall()
        for payroll in payrolls:
            print("Check Number: ", payroll[0])
            print("Pay Amount: ", payroll[1])
            print("Pay Date: ", payroll[2])
            print("Employee ID: ", payroll[3])
            print("  ")


    def show_inventory():
        query = "SELECT supply_no, item_no, inventory_qty from inventory"
        cursor.execute(query)
        inventories = cursor.fetchall()
        for inventory in inventories:
            print("Supply Number: ", inventory[0])
            print("Item Number: ", inventory[1])
            print("Inventory Quantity: ", inventory[2])
            print("  ")


    def show_items():
        query = "SELECT item_no, item_name, item_price from item"
        cursor.execute(query)
        items = cursor.fetchall()
        for item in items:
            print("Item Number: ", item[0])
            print("Item Name: ", item[1])
            print("Item Price: ", item[2])
            print("  ")


    def show_supplier():
        query = "SELECT supplier_id, supplier_name, contact_id from supplier"
        cursor.execute(query)
        suppliers = cursor.fetchall()
        for supplier in suppliers:
            print("Supplier ID: ", supplier[0])
            print("Supplier Name: ", supplier[1])
            print("Contact ID: ", supplier[2])
            print("  ")


    def show_inbound_orders():
        query = "SELECT inventory_order_id, supplier_id, expected_delivery_dt, actual_delivery_dt, supply_no, " \
                "quantity from inbound_orders "
        cursor.execute(query)
        inbound_orders = cursor.fetchall()
        for inbound_order in inbound_orders:
            print("Inventory Order ID: ", inbound_order[0])
            print("Supplier ID: ", inbound_order[1])
            print("Expected Delivery Date: ", inbound_order[2])
            print("Actual Delivery Date: ", inbound_order[3])
            print("Supply Number: ", inbound_order[4])
            print("Quantity: ", inbound_order[5])
            print("  ")


    def show_distribution():
        query = "SELECT distributor_id, contact_id, distributor_name from distribution"
        cursor.execute(query)
        distributors = cursor.fetchall()
        for distributor in distributors:
            print("Distributor ID: ", distributor[0])
            print("Contact ID: ", distributor[1])
            print("Distributor Name: ", distributor[2])
            print("  ")


    def show_outbound_orders():
        query = "SELECT order_no, item_count, total_cost, order_date, distributor_id, item_no from outbound_orders"
        cursor.execute(query)
        outbound_orders = cursor.fetchall()
        for outbound_order in outbound_orders:
            print("Order Number: ", outbound_order[0])
            print("Item Count: ", outbound_order[1])
            print("Total Cost: ", outbound_order[2])
            print("Order Date: ", outbound_order[3])
            print("Distributor ID: ", outbound_order[4])
            print("Item Number: ", outbound_order[5])
            print("  ")


    """ ----------------------------------------------- Add Inserts ----------------------------------------------"""

    # CONTACT INSERT
    contact_insert_statement = (
        "INSERT INTO contact(contact_id, address, city, email, phone, state, zip)" "VALUES (%s, %s, %s, "
        "%s, %s, %s, %s) ")
    contact_list = [
        # there are 5 managers, lets assume the winery is in Bellevue
        ('1', '177 Bruin Blvd', 'Bellevue', 'Example1@gmail.com', '5203557676', 'NE', '85742'),
        ('2', '145 Congress St', 'Bellevue', 'Example2@gmail.com', '8853557676', 'NE', '85746'),
        ('3', '104 Hjaalmarch St', 'Bellevue', 'Example3@gmail.com', '7418037478', 'NE', '85732'),
        ('4', '167 Winterhold St', 'Bellevue', 'Example4@gmail.com', '8982389512', 'NE', '29061'),
        ('5', '067 Whiterun St', 'Bellevue', 'Example5@gmail.com', '3613441108', 'NE', '37871'),

        # there are 20 employees under Henry Doyle, lets assume the winery is in Bellevue
        ('6', '307 Haafingar', 'Bellevue', 'Example6@gmail.com', '4225557633', 'NE', '43693'),
        ('7', '375 Solstheim St', 'Bellevue', 'Example7@gmail.com', '4352971561', 'NE', '57627'),
        ('8', '809 Eastmarch Blvd', 'Bellevue', 'Example8@gmail.com', '6272919970', 'NE', '47140'),
        ('9', '789 Falkreath St', 'Bellevue', 'Example9@gmail.com', '8419642257', 'NE', '34840'),
        ('10', '533 High Charity St', 'Bellevue', 'Example10@gmail.com', '2490097122', 'NE', '62129'),
        ('11', '503 Pillar of Autumn', 'Bellevue', 'Example11@gmail.com', '6733355972', 'NE', '34640'),
        ('12', '846 Congress St', 'Bellevue', 'Example12@gmail.com', '2253058727', 'NE', '71092'),
        ('13', '842 In Amber Clad St', 'Bellevue', 'Example13@gmail.com', '6702521058', 'NE', '82855'),
        ('14', '511 Infinity St', 'Bellevue', 'Example14@gmail.com', '4854214609', 'NE', '27785'),
        ('15', '535 Truth St', 'Bellevue', 'Example15@gmail.com', '1096769480', 'NE', '46862'),
        ('16', '786 And Blvd', 'Bellevue', 'Example16@gmail.com', '4067609861', 'NE', '41004'),
        ('17', '588 Reconciliation St', 'Bellevue', 'Example17@gmail.com', '2179771672', 'NE', '39984'),
        ('18', '129 Night City Blvd', 'Bellevue', 'Example18@gmail.com', '7585657424', 'NE', '42597'),
        ('19', '155 Delta St', 'Bellevue', 'Example19@gmail.com', '6100019772', 'NE', '38296'),
        ('20', '515 Minas Tirith', 'Bellevue', 'Example20@gmail.com', '6687689006', 'NE', '84493'),
        ('21', '578 Khazad-Dum', 'Bellevue', 'Example21@gmail.com', '1462155123', 'NE', '22553'),
        ('22', '825 Osgiliath St', 'Bellevue', 'Example22@gmail.com', '3010534777', 'NE', '72412'),
        ('23', '130 Rivendell Blvd', 'Bellevue', 'Example23@gmail.com', '8855232877', 'NE', '17937'),
        ('24', '553 Edoras St', 'Bellevue', 'Example24@gmail.com', '7036976936', 'NE', '88326'),
        ('25', '531 Minas Morgul', 'Bellevue', 'Example25@gmail.com', '1372850391', 'NE', '87782'),
        # 3 different suppliers, so not in bellevue
        ('26', '480 Anor Londo ', 'Denver', 'Example26@gmail.com', '3258343048', 'CO', '34134'),
        ('27', '769 Farron Keep', 'Tucson', 'Example27@gmail.com', '7394502866', 'AZ', '56037'),
        ('28', '168 Undead Burg', 'West Covina', 'Example28@gmail.com', '1847376029', 'CA', '27119'),
        # distributor amount is not specified so lets just create 3
        ('29', '817 Astora', 'Bellevue', 'Example29@gmail.com', '7564512502', 'NE', '46755'),
        ('30', '101 Firelink Shrine', 'Miami', 'Example30@gmail.com', '2338951348', 'FL', '43112'),
        ('31', '693 Undead Parish', 'Tucson', 'Example31@gmail.com', '6628099189', 'AZ', '79525')
    ]

    cursor.executemany(contact_insert_statement, contact_list)
    db.commit()
    print("contact done")

    # Supplier INSERT
    supplier_insert_statement = (
        "INSERT INTO supplier(supplier_id, supplier_name, contact_id)" "VALUES (%s, %s, %s)")
    supplier_list = [
        ('1', 'Cork N Bottles', '26'),
        ('2', 'Labels N Boxes', '27'),
        ('3', 'Vasts N Tubing', '28'),
    ]
    cursor.executemany(supplier_insert_statement, supplier_list)
    db.commit()
    print("supp done")

    # Department INSERT
    department_insert_statement = (
        "INSERT INTO department(dept_id, dept_name, NumOfEmployees)" "VALUES (%s, %s, %s)")
    department_list = [
        # 6 entries on department_list
        ('1', 'Human Resources', '1'),  # employ Janet Collins, who oversees all finances and payroll
        ('2', 'Production Line Manager', '1'),  # Henry Doyle, who manages the production line
        ('3', 'Marketing Manager', '1'),  # Roz Murphy, who heads up the marketing department
        ('4', 'Marketing Ast Manager', '1'),  # she has one assistant, Bob Ulrich, working for her
        ('5', 'Distribution', '1'),  # Maria Costanza, who is in charge of distribution
        ('6', 'Production Line Staff', '20'),  # 20 employees
    ]
    cursor.executemany(department_insert_statement, department_list)
    db.commit()
    print("dep done")

    # Item INSERT
    item_insert_statement = (
        "INSERT INTO item(item_no, item_name, item_price)" "VALUES (%s, %s, %s)")
    item_list = [
        ('1', 'bottles', '100'),
        ('2', 'corks', '50'),
        ('3', 'labels', '100'),
        ('4', 'boxes', '50'),
        ('5', 'vats', '100'),
        ('6', 'tubing', '100'),
        ('7', 'Merlot', '30'),
        ('8', 'Cabernet', '40'),
        ('9', 'Chablis', '10'),
        ('10', 'Chardonnay', '20'),
    ]
    cursor.executemany(item_insert_statement, item_list)
    db.commit()
    print("itm done")

    # Inventory INSERT
    inventory_insert_statement = (
        "INSERT INTO inventory(supply_no, item_no, inventory_qty)" "VALUES (%s, %s, %s)")
    inventory_list = [
        ('1', '1', '350'),
        ('2', '2', '300'),
        ('3', '3', '250'),
        ('4', '4', '200'),
        ('5', '5', '150'),
        ('6', '6', '50'),
        ('7', '7', '120'),
        ('8', '8', '150'),
        ('9', '9', '50'),
        ('10', '10', '50'),
    ]
    cursor.executemany(inventory_insert_statement, inventory_list)
    db.commit()
    print("inv done")

    # Distribution INSERT
    distribution_insert_statement = (
        "INSERT INTO distribution(distributor_id, contact_id, distributor_name)" "VALUES (%s, %s, %s)")
    distributor_list = [
        ('1', '29', 'Distributor 01'),
        ('2', '30', 'Distributor 02'),
        ('3', '31', 'Distributor 03'),
    ]
    cursor.executemany(distribution_insert_statement, distributor_list)
    db.commit()
    print("dist done")

    # EMPLOYEE INSERT
    employee_insert_statement = (
        "INSERT INTO employee(employee_id, first_name, last_name, contact_id, dept_id)" 
        "VALUES (%s, %s, %s, %s, %s)")
    employee_list = [
        # there should be 25 Employees
        # 5 managers
        ('1', 'Janet', 'Collins', '1', '1'),
        ('2', 'Roz', 'Murphy', '2', '3'),
        ('3', 'Bob', 'Ulrich', '3', '4'),
        ('4', 'Henry', 'Doyle', '4', '2'),
        ('5', 'Maria', 'Costanza', '5', '5'),

        # employees under Henry Doyle
        ('6', 'Joel', 'West', '6', '6'),
        ('7', 'Janet', 'Basken', '7', '6'),
        ('8', 'Clint', 'Westwood', '8', '6'),
        ('9', 'Henry', 'Calivli', '9', '6'),
        ('10', 'George', 'Boggles', '10', '6'),
        ('11', 'Flying', 'Fish', '11', '6'),
        ('12', 'Tiny', 'Tina', '12', '6'),
        ('13', 'Artorias', 'Knight', '13', '6'),
        ('14', 'Sif', 'Gray-wolf', '14', '6'),
        ('15', 'Santy', 'Clause', '15', '6'),
        ('16', 'Ham', 'Toro', '16', '6'),
        ('17', 'Biggie', 'Smalls', '17', '6'),
        ('18', 'Kyle', 'Wall-smasher', '18', '6'),
        ('19', 'Mochi', 'Luna', '19', '6'),
        ('20', 'Luke', 'Cloudwalker', '20', '6'),
        ('21', 'Brenda', 'Sang', '21', '6'),
        ('22', 'Biggie', 'Smalls', '22', '6'),
        ('23', 'Kim', 'Carsmashin', '23', '6'),
        ('24', 'Moms', 'Spaghetti', '24', '6'),
        ('25', 'Bob', 'Rose', '25', '6')

    ]

    cursor.executemany(employee_insert_statement, employee_list)
    db.commit()
    print("emp done")

    # Work_Hours INSERT
    workhours_insert_statement = (
        "INSERT INTO work_hours(employee_id, current_week, hours_YTD)" "VALUES (%s, %s, %s)")
    work_hours_list = [
        # there should be 25 Employees
        # 5 managers
        ('1', '60', '2860'),
        ('2', '52', '3110'),
        ('3', '60', '2952'),
        ('4', '60', '2998'),
        ('5', '48', '3121'),

        # employees under Henry Doyle
        ('6', '36', '1800'),
        ('7', '0', '1750'),
        ('8', '36', '1590'),
        ('9', '36', '1810'),
        ('10', '24', '1777'),
        ('11', '36', '1880'),
        ('12', '36', '1774'),
        ('13', '24', '1200'),
        ('14', '36', '1611'),
        ('15', '36', '1011'),
        ('16', '36', '1400'),
        ('17', '36', '1700'),
        ('18', '36', '1960'),
        ('19', '12', '1766'),
        ('20', '36', '1846'),
        ('21', '36', '1666'),
        ('22', '36', '1769'),
        ('23', '36', '1490'),
        ('24', '36', '1774'),
        ('25', '12', '1955')
    ]
    cursor.executemany(workhours_insert_statement, work_hours_list)
    db.commit()
    print("work done")

    # Payroll INSERT
    payroll_insert_statement = (
        "INSERT INTO payroll(check_no, pay_amount, pay_date, employee_id)" "VALUES (%s, %s, %s, %s)")
    payroll_list = [
        # 5 managers
        ('1', '1000.00', '2022-11-27', '1'),
        ('2', '1000.00', '2022-11-27', '2'),
        ('3', '1000.00', '2022-11-27', '3'),
        ('4', '1000.00', '2022-11-27', '4'),
        ('5', '1000.00', '2022-11-27', '5'),
        # 20 Employees
        ('6', '500.00', '2022-11-27', '6'),
        ('7', '600.00', '2022-11-27', '7'),
        ('8', '700.00', '2022-11-27', '8'),
        ('9', '600.00', '2022-11-27', '9'),
        ('10', '500.00', '2022-11-27', '10'),
        ('11', '500.00', '2022-11-27', '11'),
        ('12', '600.00', '2022-11-27', '12'),
        ('13', '700.00', '2022-11-27', '13'),
        ('14', '600.00', '2022-11-27', '14'),
        ('15', '500.00', '2022-11-27', '15'),
        ('16', '500.00', '2022-11-27', '16'),
        ('17', '600.00', '2022-11-27', '17'),
        ('18', '700.00', '2022-11-27', '18'),
        ('19', '600.00', '2022-11-27', '19'),
        ('20', '500.00', '2022-11-27', '20'),
        ('21', '500.00', '2022-11-27', '21'),
        ('22', '600.00', '2022-11-27', '22'),
        ('23', '700.00', '2022-11-27', '23'),
        ('24', '600.00', '2022-11-27', '24'),
        ('25', '500.00', '2022-11-27', '25')
    ]
    cursor.executemany(payroll_insert_statement, payroll_list)
    db.commit()
    print("pay done")

    # Inbound Orders INSERT
    inbound_orders_insert_statement = (
        "INSERT INTO inbound_orders(inventory_order_id, supplier_id, expected_delivery_dt, actual_delivery_dt, "
        "supply_no, quantity)" "VALUES (%s, %s, %s, %s, %s, %s)")
    inbound_orders_list = [
        ('1', '1', '2022-11-27', '2022-11-27', '1', '200'),
        ('2', '2', '2022-11-27', '2022-11-27', '3', '100'),
        ('3', '3', '2022-11-27', '2022-11-28', '5', '300'),
        ('4', '1', '2022-11-28', '2022-11-30', '2', '200'),
        ('5', '2', '2022-11-28', '2022-11-29', '4', '300'),
        ('6', '3', '2022-11-28', '2022-12-01', '6', '200'),
    ]
    cursor.executemany(inbound_orders_insert_statement, inbound_orders_list)
    db.commit()
    print("inb done")

    # Outbound Orders INSERT
    outbound_orders_insert_statement = (
        "INSERT INTO outbound_orders(order_no, item_count, total_cost, order_date, distributor_id, item_no)" "VALUES "
        "(%s, %s, %s, %s, %s, %s)")
    outbound_orders_list = [
        ('1', '2', '50', '2022-11-27', '1', '1'),
        ('2', '4', '100', '2022-11-27', '2', '2'),
        ('3', '6', '200', '2022-11-28', '3', '3'),
        ('4', '8', '300', '2022-11-30', '1', '4'),
        ('5', '10', '400', '2022-11-29', '2', '5'),
        ('6', '12', '500', '2022-12-01', '3', '6'),
    ]
    cursor.executemany(outbound_orders_insert_statement, outbound_orders_list)
    db.commit()
    print("otb done")

    # Management INSERT
    management_insert_statement = (
        "INSERT INTO management(mngmt_id, dept_id, employee_id, start_date)" "VALUES (%s, %s, %s, %s)")
    management_list = [
        ('1', '1', '1', '2022-11-27'),
        ('2', '2', '4', '2022-11-27'),
        ('3', '3', '2', '2022-11-27'),
        ('4', '4', '3', '2022-11-27'),
        ('5', '5', '5', '2022-11-27'),
    ]
    cursor.executemany(management_insert_statement, management_list)
    db.commit()
    print("mgmt done")

    # Display Output
    print("-- Contacts --\n")
    show_contacts()
    print("-- Employees --\n")
    show_employees()
    print("-- Work Hours --\n")
    show_work_hours()
    print("-- Department --\n")
    show_department()
    print("-- Payroll --\n")
    show_payroll()
    print("-- Inventory --\n")
    show_inventory()
    print("-- Items --\n")
    show_items()
    print("-- Suppliers --\n")
    show_supplier()
    print("-- Inbound Orders --\n")
    show_inbound_orders()
    print("-- Outbound Orders --\n")
    show_outbound_orders()
    print("-- Distribution --\n")
    show_distribution()
    print("-- Management --\n")
    show_management()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
