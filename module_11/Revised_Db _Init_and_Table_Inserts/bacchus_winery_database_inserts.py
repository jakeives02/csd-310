"""
Team Indigo
12/4/2022
CSD 310, Milestone 2 Insert .py file
Description: This .py file inserts data into the tables created by the file Bacchus_Winery_Table_Inserts.sql
After the data has been successfully inserted into the 12 tables, the 12 tables values are then displayed.
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "bacchuswinery",
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
        query = "SELECT employee_id, first_name, last_name, job_title from employee"
        cursor.execute(query)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee_ID: ", employee[0])
            print("First Name: ", employee[1])
            print("Last Name: ", employee[2])
            print("Job Title: ", employee[3])
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

    # EMPLOYEE INSERT
    employee_insert_statement = (
        "INSERT INTO employee(employee_id, first_name, last_name, job_title, contact_id, dept_id)" 
        "VALUES (%s, %s, %s, %s, %s, %s)")
    employee_list = [
        # there should be 25 Employees
        # 5 managers
        ('1',  'Janet', 'Collins',  'Finance Manager',              '1',  '1'),
        ('2',  'Roz',   'Murphy',   'Marketing Manager',            '2',  '3'),
        ('3',  'Bob',   'Ulrich',   'Assistant Marketing Manager',  '3',  '4'),
        ('4',  'Henry', 'Doyle',    'Production Manager',           '4',  '2'),
        ('5',  'Maria', 'Costanza', 'Distribution Manager',         '5',  '5'),

        # employees under Henry Doyle
        ('6',  'Joel',     'West',         'Material Handler',      '6',  '6'),
        ('7',  'Janet',    'Basken',       'Winemaker',             '7',  '6'),
        ('8',  'Clint',    'Westwood',     'Vineyard Worker',       '8',  '6'),
        ('9',  'Henry',    'Calivli',      'Material Handler',      '9',  '6'),
        ('10', 'George',   'Boggles',      'Winemaker',             '10', '6'),
        ('11', 'Flying',   'Fish',         'Vineyard Worker',       '11', '6'),
        ('12', 'Tiny',     'Tina',         'Cellar Worker',         '12', '6'),
        ('13', 'Artorias', 'Knight',       'Material Handler',      '13', '6'),
        ('14', 'Sif',      'Gray-wolf',    'Assistant Winemaker',   '14', '6'),
        ('15', 'Santy',    'Clause',       'Vineyard Worker',       '15', '6'),
        ('16', 'Ham',      'Toro',         'Material Handler',      '16', '6'),
        ('17', 'Biggie',   'Smalls',       'Vineyard Worker',       '17', '6'),
        ('18', 'Kyle',     'Wall-smasher', 'Material Handler',      '18', '6'),
        ('19', 'Mochi',    'Luna',         'Assistant Winemaker',   '19', '6'),
        ('20', 'Luke',     'Cloudwalker',  'Cellar Worker',         '20', '6'),
        ('21', 'Brenda',   'Sang',         'Laboratory Technician', '21', '6'),
        ('22', 'Tupac',    'Shakur',       'Cellar Worker',         '22', '6'),
        ('23', 'Kim',      'Carsmashin',   'Material Handler',      '23', '6'),
        ('24', 'Moms',     'Spaghetti',    'Vineyard Worker',       '24', '6'),
        ('25', 'Bob',      'Rose',         'Vineyard Worker',       '25', '6')

    ]

    cursor.executemany(employee_insert_statement, employee_list)
    db.commit()

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

    # Inbound Orders INSERT
    inbound_orders_insert_statement = (
        "INSERT INTO inbound_orders(inventory_order_id, supplier_id, expected_delivery_dt, actual_delivery_dt, "
        "supply_no, quantity)" "VALUES (%s, %s, %s, %s, %s, %s)")
    inbound_orders_list = [
        ('1', '1', '2022-01-27', '2022-01-27', '1', '200'),
        ('13', '1', '2022-01-26', '2022-01-27', '4', '300'),
        ('2', '2', '2022-02-11', '2022-02-12', '3', '100'),
        ('3', '3', '2022-03-27', '2022-03-28', '5', '300'),
        ('4', '1', '2022-04-28', '2022-05-28', '2', '200'),
        ('5', '2', '2022-05-30', '2022-06-04', '4', '300'),
        ('6', '3', '2022-06-28', '2022-07-01', '6', '200'),
        ('7', '1', '2022-07-27', '2022-07-28', '1', '200'),
        ('8', '2', '2022-08-11', '2022-08-12', '3', '100'),
        ('9', '3', '2022-09-27', '2022-12-28', '5', '300'),
        ('10', '1', '2022-10-28', '2022-10-28', '2', '200'),
        ('11', '2', '2022-11-30', '2022-11-30', '4', '300'),
        ('12', '3', '2022-12-28', '2022-12-30', '6', '200'),
        ('14', '1', '2023-02-26', '2023-02-27', '4', '300'),
    ]
    cursor.executemany(inbound_orders_insert_statement, inbound_orders_list)
    db.commit()

    # Outbound Orders INSERT
    outbound_orders_insert_statement = (
        "INSERT INTO outbound_orders(order_no, item_count, total_cost, order_date, distributor_id, item_no)" "VALUES "
        "(%s, %s, %s, %s, %s, %s)")
    outbound_orders_list = [
        ('1',    '2',  '80.00',  '2022-01-03', '1', '8'),
        ('2',    '4',  '120.00', '2022-01-06', '2', '7'),
        ('3',    '6',  '120.00', '2022-01-06', '3', '10'),
        ('4',    '8',  '160.00', '2022-01-06', '1', '10'),
        ('5',    '10', '100.00', '2022-01-06', '2', '9'),
        ('6',    '12', '480.00', '2022-01-07', '3', '8'),
		('7',    '2',  '80.00',  '2022-01-09', '1', '8'),
        ('8',    '4',  '160.00', '2022-01-11', '2', '8'),
        ('9',    '6',  '180.00', '2022-01-12', '3', '7'),
        ('10',   '8',  '320.00', '2022-01-14', '1', '8'),
        ('11',   '10', '100.00', '2022-01-15', '2', '9'),
        ('12',   '12', '360.00', '2022-01-17', '3', '7'),
        ('13',   '4',  '120.00', '2022-01-17', '2', '7'),
        ('14',   '6',  '180.00', '2022-01-19', '3', '7'),
        ('15',   '8',  '320.00', '2022-01-20', '1', '8'),
        ('16',   '10', '100.00', '2022-01-20', '2', '9'),
        ('17',   '12', '120.00', '2022-01-24', '3', '9'),
		('18',   '2',  '60.00',  '2022-01-25', '1', '7'),
        ('19',   '4',  '40.00',  '2022-01-27', '2', '9'),
        ('20',   '6',  '120.00', '2022-01-28', '3', '10'),
        ('21',   '8',  '320.00', '2022-01-29', '1', '8'),
        ('22',   '10', '200.00', '2022-01-30', '2', '10'),
        ('23',   '4',  '160.00', '2022-01-31', '2', '8'),
        ('24',   '6',  '120.00', '2022-01-31', '3', '10'),
        ('25',   '8',  '80.00',  '2022-02-04', '1', '9'),
        ('26',   '10', '300.00', '2022-02-04', '2', '7'),
        ('27',   '12', '240.00', '2022-02-05', '3', '10'),
		('28',   '2',  '60.00',  '2022-02-07', '1', '7'),
        ('29',   '4',  '80.00',  '2022-02-09', '2', '10'),
        ('30',   '6',  '240.00', '2022-02-10', '3', '8'),
        ('31',   '8',  '240.00', '2022-02-10', '1', '7'),
        ('32',   '10', '300.00', '2022-02-12', '2', '7'),
        ('33',   '4',  '160.00', '2022-02-12', '2', '8'),
        ('34',   '6',  '60.00',  '2022-02-13', '3', '9'),
        ('35',   '8',  '240.00', '2022-02-15', '1', '7'),
        ('36',   '10', '300.00', '2022-02-18', '2', '7'),
        ('37',   '12', '480.00', '2022-02-20', '3', '8'),
		('38',   '2',  '60.00',  '2022-02-20', '1', '7'),
        ('39',   '4',  '80.00',  '2022-02-21', '2', '10'),
        ('40',   '6',  '180.00', '2022-02-25', '3', '7'),
        ('41',   '8',  '80.00',  '2022-02-26', '1', '9'),
        ('42',   '10', '400.00', '2022-03-02', '2', '8'),
        ('43',   '4',  '120.00', '2022-03-03', '2', '7'),
        ('44',   '6',  '60.00',  '2022-03-03', '3', '9'),
        ('45',   '8',  '320.00', '2022-03-06', '1', '8'),
        ('46',   '10', '100.00', '2022-03-08', '2', '9'),
        ('47',   '12', '240.00', '2022-03-08', '3', '10'),
		('48',   '2',  '40.00',  '2022-03-11', '1', '10'),
        ('49',   '4',  '160.00', '2022-03-12', '2', '8'),
        ('50',   '6',  '60.00',  '2022-03-12', '3', '9'),
        ('51',   '8',  '80.00',  '2022-03-13', '1', '9'),
        ('52',   '10', '300.00', '2022-03-13', '2', '7'),
        ('53',   '4',  '80.00',  '2022-03-15', '2', '10'),
        ('54',   '6',  '60.00',  '2022-03-15', '3', '9'),
        ('55',   '8',  '320.00', '2022-03-17', '1', '8'),
        ('56',   '10', '100.00', '2022-03-20', '2', '9'),
        ('57',   '12', '240.00', '2022-03-22', '3', '10'),
		('58',   '2',  '60.00',  '2022-03-23', '1', '7'),
        ('59',   '4',  '80.00',  '2022-03-23', '2', '10'),
        ('60',   '6',  '240.00', '2022-03-25', '3', '8'),
        ('61',   '8',  '240.00', '2022-03-25', '1', '7'),
        ('62',   '10', '200.00', '2022-03-26', '2', '10'),
        ('63',   '4',  '40.00',  '2022-03-28', '2', '9'),
        ('64',   '6',  '180.00', '2022-03-28', '3', '7'),
        ('65',   '8',  '160.00', '2022-03-29', '1', '10'),
        ('66',   '10', '400.00', '2022-03-30', '2', '8'),
        ('67',   '12', '240.00', '2022-03-30', '3', '10'),
		('68',   '2',  '80.00',  '2022-04-03', '1', '8'),
        ('69',   '4',  '80.00',  '2022-04-04', '2', '10'),
        ('70',   '6',  '120.00', '2022-04-05', '3', '10'),
        ('71',   '8',  '160.00', '2022-04-05', '1', '10'),
        ('72',   '10', '300.00', '2022-04-09', '2', '7'),
        ('73',   '4',  '40.00',  '2022-04-12', '2', '9'),
        ('74',   '6',  '180.00', '2022-04-13', '3', '7'),
        ('75',   '8',  '240.00', '2022-04-15', '1', '7'),
        ('76',   '10', '200.00', '2022-04-18', '2', '10'),
        ('77',   '12', '120.00', '2022-04-18', '3', '9'),
		('78',   '2',  '80.00',  '2022-04-20', '1', '8'),
        ('79',   '4',  '120.00', '2022-04-20', '2', '7'),
        ('80',   '6',  '240.00', '2022-04-21', '3', '8'),
        ('81',   '8',  '160.00', '2022-04-22', '1', '10'),
        ('82',   '10', '300.00', '2022-04-23', '2', '7'),
        ('83',   '4',  '40.00',  '2022-04-25', '2', '9'),
        ('84',   '6',  '180.00', '2022-04-25', '3', '7'),
        ('85',   '8',  '160.00', '2022-04-25', '1', '10'),
        ('86',   '10', '300.00', '2022-04-29', '2', '7'),
        ('87',   '12', '360.00', '2022-04-30', '3', '7'),
		('88',   '2',  '20.00',  '2022-04-30', '1', '9'),
        ('89',   '4',  '80.00',  '2022-04-30', '2', '10'),
        ('90',   '6',  '120.00', '2022-05-01', '3', '10'),
        ('91',   '8',  '160.00', '2022-05-02', '1', '10'),
        ('92',   '10', '100.00', '2022-05-03', '2', '9'),
        ('93',   '4',  '160.00', '2022-05-04', '2', '8'),
        ('94',   '6',  '180.00', '2022-05-04', '3', '7'),
        ('95',   '8',  '80.00',  '2022-05-08', '1', '9'),
        ('96',   '10', '300.00', '2022-05-09', '2', '7'),
        ('97',   '12', '360.00', '2022-05-10', '3', '7'),
		('98',   '2',  '20.00',  '2022-05-14', '1', '9'),
        ('99',   '4',  '40.00',  '2022-05-14', '2', '9'),
        ('100',  '6',  '240.00', '2022-05-15', '3', '8'),
        ('101',  '8',  '80.00',  '2022-05-17', '1', '9'),
        ('102',  '10', '300.00', '2022-05-17', '2', '7'),
        ('103',  '4',  '160.00', '2022-05-18', '2', '8'),
        ('104',  '6',  '60.00',  '2022-05-18', '3', '9'),
        ('105',  '8',  '160.00', '2022-05-18', '1', '10'),
        ('106',  '10', '200.00', '2022-05-19', '2', '10'),
        ('107',  '12', '360.00', '2022-05-20', '3', '7'),
		('108',  '2',  '20.00',  '2022-05-21', '1', '9'),
        ('109',  '4',  '40.00',  '2022-05-24', '2', '9'),
        ('110',  '6',  '240.00', '2022-05-25', '3', '8'),
        ('111',  '8',  '80.00',  '2022-05-31', '1', '9'),
        ('112',  '10', '100.00', '2022-06-01', '2', '9'),
        ('113',  '4',  '40.00',  '2022-06-02', '2', '9'),
        ('114',  '6',  '120.00', '2022-06-03', '3', '10'),
        ('115',  '8',  '240.00', '2022-06-04', '1', '7'),
        ('116',  '10', '400.00', '2022-06-05', '2', '8'),
        ('117',  '12', '360.00', '2022-06-05', '3', '7'),
		('118',  '2',  '40.00',  '2022-06-05', '1', '10'),
        ('119',  '4',  '160.00', '2022-06-06', '2', '8'),
        ('120',  '6',  '180.00', '2022-06-07', '3', '7'),
        ('121',  '8',  '160.00', '2022-06-08', '1', '10'),
        ('122',  '10', '300.00', '2022-06-10', '2', '7'),
        ('123',  '4',  '160.00', '2022-06-14', '2', '8'),
        ('124',  '6',  '180.00', '2022-06-14', '3', '7'),
        ('125',  '8',  '240.00', '2022-06-14', '1', '7'),
        ('126',  '10', '100.00', '2022-06-14', '2', '9'),
        ('127',  '12', '360.00', '2022-06-15', '3', '7'),
		('128',  '2',  '20.00',  '2022-06-15', '1', '9'),
        ('129',  '4',  '120.00', '2022-06-16', '2', '7'),
        ('130',  '6',  '180.00', '2022-06-16', '3', '7'),
        ('131',  '8',  '80.00',  '2022-06-16', '1', '9'),
        ('132',  '10', '400.00', '2022-06-16', '2', '8'),
        ('133',  '4',  '120.00', '2022-06-17', '2', '7'),
        ('134',  '6',  '60.00',  '2022-06-17', '3', '9'),
        ('135',  '8',  '240.00', '2022-06-20', '1', '7'),
        ('136',  '10', '200.00', '2022-06-21', '2', '10'),
        ('137',  '12', '240.00', '2022-06-21', '3', '10'),
		('138',  '2',  '40.00',  '2022-06-24', '1', '10'),
        ('139',  '4',  '120.00', '2022-06-24', '2', '7'),
        ('140',  '6',  '120.00', '2022-06-24', '3', '10'),
        ('141',  '8',  '160.00', '2022-06-27', '1', '10'),
        ('142',  '10', '200.00', '2022-06-27', '2', '10'),
        ('143',  '4',  '40.00',  '2022-06-27', '2', '9'),
        ('144',  '6',  '180.00', '2022-06-29', '3', '7'),
        ('145',  '8',  '320.00', '2022-06-30', '1', '8'),
        ('146',  '10', '200.00', '2022-07-01', '2', '10'),
        ('147',  '12', '480.00', '2022-07-01', '3', '8'),
		('148',  '2',  '60.00',  '2022-07-01', '1', '7'),
        ('149',  '4',  '40.00',  '2022-07-02', '2', '9'),
        ('150',  '8',  '80.00',  '2022-07-03', '1', '9'),
        ('151',  '10', '300.00', '2022-07-04', '2', '7'),
        ('152',  '4',  '80.00',  '2022-07-04', '2', '10'),
        ('153',  '6',  '240.00', '2022-07-04', '3', '8'),
        ('154',  '8',  '80.00',  '2022-07-07', '1', '9'),
        ('155',  '10', '400.00', '2022-07-09', '2', '8'),
        ('156',  '12', '360.00', '2022-07-10', '3', '7'),
 		('157',  '2',  '60.00',  '2022-07-12', '1', '7'),
        ('158',  '4',  '80.00',  '2022-07-18', '2', '10'),
        ('159',  '6',  '180.00', '2022-07-18', '3', '7'),
        ('160',  '8',  '320.00', '2022-07-21', '1', '8'),
        ('161',  '10', '100.00', '2022-07-21', '2', '9'),
        ('162',  '4',  '160.00', '2022-07-22', '2', '8'),
        ('163',  '6',  '240.00', '2022-07-23', '3', '8'),
        ('164',  '8',  '160.00', '2022-07-27', '1', '10'),
        ('165',  '10', '100.00', '2022-07-28', '2', '9'),
        ('166',  '12', '120.00', '2022-08-01', '3', '9'),
 		('167',  '2',  '80.00',  '2022-08-01', '1', '8'),
        ('168',  '4',  '120.00', '2022-08-02', '2', '7'),
        ('169',  '6',  '120.00', '2022-08-04', '3', '10'),
        ('170',  '8',  '80.00',  '2022-08-06', '1', '9'),
        ('171',  '10', '200.00', '2022-08-06', '2', '10'),
        ('172',  '4',  '80.00',  '2022-08-06', '2', '10'),
        ('173',  '6',  '60.00',  '2022-08-08', '3', '9'),
        ('174',  '8',  '240.00', '2022-08-09', '1', '7'),
        ('175',  '10', '100.00', '2022-08-10', '2', '9'),
        ('176',  '12', '120.00', '2022-08-10', '3', '9'),
 		('177',  '2',  '60.00',  '2022-08-10', '1', '7'),
        ('178',  '4',  '80.00',  '2022-08-11', '2', '10'),
        ('179',  '6',  '60.00',  '2022-08-12', '3', '9'),
        ('180',  '8',  '240.00', '2022-08-12', '1', '7'),
        ('181',  '10', '300.00', '2022-08-14', '2', '7'),
        ('182',  '4',  '80.00',  '2022-08-15', '2', '10'),
        ('183',  '6',  '120.00', '2022-08-15', '3', '10'),
        ('184',  '8',  '160.00', '2022-08-15', '1', '10'),
        ('185',  '10', '200.00', '2022-08-16', '2', '10'),
        ('186',  '12', '240.00', '2022-08-16', '3', '10'),
 		('187',  '2',  '80.00',  '2022-08-17', '1', '8'),
        ('188',  '4',  '80.00',  '2022-08-17', '2', '10'),
        ('189',  '6',  '120.00', '2022-08-17', '3', '10'),
        ('190',  '8',  '160.00', '2022-08-18', '1', '10'),
        ('191',  '10', '200.00', '2022-08-18', '2', '10'),
        ('192',  '4',  '120.00', '2022-08-19', '2', '7'),
        ('193',  '6',  '180.00', '2022-08-20', '3', '7'),
        ('194',  '8',  '160.00', '2022-08-20', '1', '10'),
        ('195',  '10', '400.00', '2022-08-21', '2', '8'),
        ('196',  '12', '360.00', '2022-08-24', '3', '7'),
 		('197',  '2',  '60.00',  '2022-08-25', '1', '7'),
        ('198',  '4',  '120.00', '2022-08-26', '2', '7'),
        ('199',  '6',  '60.00',  '2022-08-29', '3', '9'),
        ('200',  '8',  '80.00',  '2022-08-29', '1', '9'),
        ('201',  '10', '100.00', '2022-09-01', '2', '9'),
        ('202',  '4',  '160.00', '2022-09-01', '2', '8'),
        ('203',  '6',  '120.00', '2022-09-02', '3', '10'),
        ('204',  '8',  '80.00',  '2022-09-04', '1', '9'),
        ('205',  '10', '400.00', '2022-09-07', '2', '8'),
        ('206',  '12', '360.00', '2022-09-07', '3', '7'),
 		('207',  '2',  '20.00',  '2022-09-08', '1', '9'),
        ('208',  '4',  '160.00', '2022-09-10', '2', '8'),
        ('209',  '6',  '180.00', '2022-09-10', '3', '7'),
        ('210',  '8',  '320.00', '2022-09-12', '1', '8'),
        ('211',  '10', '300.00', '2022-09-13', '2', '7'),
        ('212',  '4',  '80.00',  '2022-09-13', '2', '10'),
        ('213',  '6',  '120.00', '2022-09-15', '3', '10'),
        ('214',  '8',  '160.00', '2022-09-17', '1', '10'),
        ('215',  '10', '400.00', '2022-09-17', '2', '8'),
        ('216',  '12', '120.00', '2022-09-19', '3', '9'),
 		('217',  '2',  '80.00',  '2022-09-20', '1', '8'),
        ('218',  '4',  '80.00',  '2022-09-21', '2', '10'),
        ('219',  '6',  '180.00', '2022-09-23', '3', '7'),
        ('220',  '8',  '320.00', '2022-09-23', '1', '8'),
        ('221',  '10', '400.00', '2022-09-25', '2', '8'),
        ('222',  '4',  '160.00', '2022-09-25', '2', '8'),
        ('223',  '6',  '120.00', '2022-09-26', '3', '10'),
        ('224',  '8',  '160.00', '2022-09-26', '1', '10'),
        ('225',  '10', '300.00', '2022-09-28', '2', '7'),
        ('226',  '12', '120.00', '2022-09-28', '3', '9'),
 		('227',  '2',  '20.00',  '2022-09-28', '1', '9'),
        ('228',  '4',  '160.00', '2022-10-01', '2', '8'),
        ('229',  '6',  '240.00', '2022-10-02', '3', '8'),
        ('230',  '8',  '80.00',  '2022-10-04', '1', '9'),
        ('231',  '10', '300.00', '2022-10-05', '2', '7'),
        ('232',  '4',  '120.00', '2022-10-09', '2', '7'),
        ('233',  '6',  '180.00', '2022-10-10', '3', '7'),
        ('234',  '8',  '160.00', '2022-10-11', '1', '10'),
        ('235',  '10', '100.00', '2022-10-12', '2', '9'),
        ('236',  '12', '360.00', '2022-10-15', '3', '7'),
 		('237',  '2',  '80.00',  '2022-10-15', '1', '8'),
        ('238',  '4',  '40.00',  '2022-10-18', '2', '9'),
        ('239',  '8',  '320.00', '2022-10-18', '1', '8'),
        ('240',  '10', '200.00', '2022-10-19', '2', '10'),
        ('241',  '4',  '80.00',  '2022-10-21', '2', '10'),
        ('242',  '6',  '120.00', '2022-10-21', '3', '10'),
        ('243',  '8',  '160.00', '2022-10-25', '1', '10'),
        ('244',  '10', '400.00', '2022-10-25', '2', '8'),
        ('245',  '12', '240.00', '2022-10-27', '3', '10'),
 		('246',  '2',  '20.00',  '2022-10-28', '1', '9'),
        ('247',  '4',  '40.00',  '2022-10-28', '2', '9'),
        ('248',  '6',  '60.00',  '2022-10-28', '3', '9'),
        ('249',  '8',  '320.00', '2022-10-28', '1', '8'),
        ('250',  '10', '400.00', '2022-10-29', '2', '8'),
        ('251',  '4',  '40.00',  '2022-10-29', '2', '9'),
        ('252',  '6',  '180.00', '2022-10-31', '3', '7'),
        ('253',  '8',  '80.00',  '2022-10-31', '1', '9'),
        ('254',  '10', '200.00', '2022-10-31', '2', '10'),
        ('255',  '12', '360.00', '2022-10-31', '3', '7'),
 		('256',  '2',  '40.00',  '2022-11-01', '1', '10'),
        ('257',  '4',  '160.00', '2022-11-01', '2', '8'),
        ('258',  '6',  '180.00', '2022-11-02', '3', '7'),
        ('259',  '8',  '240.00', '2022-11-02', '1', '7'),
        ('260',  '10', '300.00', '2022-11-04', '2', '7'),
        ('261',  '4',  '80.00',  '2022-11-05', '2', '10'),
        ('262',  '6',  '240.00', '2022-11-05', '3', '8'),
        ('263',  '8',  '80.00',  '2022-11-05', '1', '9'),
        ('264',  '10', '100.00', '2022-11-06', '2', '9'),
        ('265',  '12', '360.00', '2022-11-06', '3', '7'),
 		('266',  '2',  '60.00',  '2022-11-11', '1', '7'),
        ('267',  '4',  '120.00', '2022-11-11', '2', '7'),
        ('268',  '6',  '60.00',  '2022-11-12', '3', '9'),
        ('269',  '8',  '240.00', '2022-11-14', '1', '7'),
        ('270',  '10', '300.00', '2022-11-16', '2', '7'),
        ('271',  '4',  '160.00', '2022-11-18', '2', '8'),
        ('272',  '6',  '120.00', '2022-11-18', '3', '10'),
        ('273',  '8',  '320.00', '2022-11-19', '1', '8'),
        ('274',  '10', '100.00', '2022-11-20', '2', '9'),
        ('275',  '12', '120.00', '2022-11-21', '3', '9'),
 		('276',  '2',  '20.00',  '2022-11-21', '1', '9'),
        ('277',  '4',  '160.00', '2022-11-22', '2', '8'),
        ('278',  '6',  '180.00', '2022-11-24', '3', '7'),
        ('279',  '8',  '240.00', '2022-11-26', '1', '7'),
        ('280',  '10', '300.00', '2022-11-27', '2', '7'),
        ('281',  '4',  '80.00',  '2022-11-29', '2', '10'),
        ('282',  '6',  '120.00', '2022-12-05', '3', '10'),
        ('283',  '8',  '240.00', '2022-12-05', '1', '7'),
    ]
    cursor.executemany(outbound_orders_insert_statement, outbound_orders_list)
    db.commit()


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

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
