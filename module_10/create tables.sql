DROP DATABASE IF EXISTS bacchus;
create database bacchus;
use bacchus; 

DROP TABLE IF EXISTS Inbound_orders;
DROP TABLE IF EXISTS Outbound_orders;
DROP TABLE IF EXISTS Management;
DROP TABLE IF EXISTS Payroll;
DROP TABLE IF EXISTS Work_Hours;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Distribution;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Supplier;
DROP TABLE IF EXISTS Contact;


CREATE TABLE `Inventory` (
	`supply_no` INT NOT NULL,
	`item_no` INT NOT NULL,
	`inventory_qty` INT NOT NULL,
	PRIMARY KEY (`supply_no`)
);

CREATE TABLE `Item` (
	`item_no` INT NOT NULL,
	`item_name` VARCHAR(20) NOT NULL,
	`item_price` DECIMAL(6,2) NOT NULL,
	PRIMARY KEY (`item_no`)
);

CREATE TABLE `Supplier` (
	`supplier_id` INT NOT NULL,
	`supplier_name` VARCHAR(20) NOT NULL,
	`contact_id` INT NOT NULL,
	PRIMARY KEY (`supplier_id`)
);

CREATE TABLE `Inbound_orders` (
	`inventory_order_id` INT NOT NULL,
	`supplier_id` INT NOT NULL,
	`expected_delivery_dt` DATE,
	`actual_delivery_dt` DATE,
	`supply_no` INT NOT NULL,
	`quantity` INT NOT NULL,
	PRIMARY KEY (`inventory_order_id`)
);

CREATE TABLE `Outbound_orders` (
	`order_no` INT NOT NULL,
	`item_count` INT NOT NULL,
	`total_cost` DECIMAL(6,2) NOT NULL,
	`item_no` INT NOT NULL,
	`distributor_id` INT NOT NULL,
	`order_date` DATE NOT NULL,
	PRIMARY KEY (`order_no`)
);

CREATE TABLE `Distribution` (
	`distributor_id` INT NOT NULL,
	`distributor_name` VARCHAR(20) NOT NULL,
	`contact_id` INT NOT NULL,
	PRIMARY KEY (`distributor_id`)
);

CREATE TABLE `Contact` (
	`contact_id` INT NOT NULL,
	`address` VARCHAR(50),
	`city` VARCHAR(20),
	`state` VARCHAR(20),
	`zip` VARCHAR(20),
	`phone` VARCHAR(20),
	`email` VARCHAR(20),
	PRIMARY KEY (`contact_id`)
);

CREATE TABLE `Department` (
	`dept_id` INT NOT NULL,
	`dept_name` VARCHAR(50),
	`NumOfEmployees` INT,
	PRIMARY KEY (`dept_id`)
);

CREATE TABLE `Payroll` (
	`check_no` INT NOT NULL,
	`pay_amount` DECIMAL(6,2) NOT NULL,
	`pay_date` DATE NOT NULL,
	`employee_id` INT NOT NULL,
	PRIMARY KEY (`check_no`)
);

CREATE TABLE `Employee` (
	`employee_id` INT NOT NULL,
	`first_name` VARCHAR(20) NOT NULL,
	`last_name` VARCHAR(20) NOT NULL,
	`contact_id` INT NOT NULL,
	`dept_id` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Management` (
	`mngmt_id` INT NOT NULL,
	`employee_id` INT NOT NULL,
	`dept_id` INT NOT NULL,
	`start_date` DATE,
	`end_date` DATE,
	PRIMARY KEY (`mngmt_id`)
);

CREATE TABLE `Work_hours` (
	`hours_YTD` DECIMAL(9) NOT NULL,
	`current_week` INT NOT NULL,
	`employee_id` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

ALTER TABLE Inventory
ADD CONSTRAINT FK_inventory
FOREIGN KEY (item_no) REFERENCES Item(item_no);

ALTER TABLE Supplier
ADD CONSTRAINT FK_supplier
FOREIGN KEY (contact_id) REFERENCES Contact(contact_id);

ALTER TABLE Inbound_orders
ADD CONSTRAINT FK_inb_supplier
FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id);

ALTER TABLE Inbound_orders
ADD CONSTRAINT FK_inb_supply_no
FOREIGN KEY (supply_no) REFERENCES Inventory(supply_no);

ALTER TABLE Outbound_orders
ADD CONSTRAINT FK_otb_distributor
FOREIGN KEY (distributor_id) REFERENCES Distribution(distributor_id);

ALTER TABLE Outbound_orders
ADD CONSTRAINT FK_otb_item
FOREIGN KEY (item_no) REFERENCES Item(item_no);

ALTER TABLE Distribution
ADD CONSTRAINT FK_dist_contact
FOREIGN KEY (contact_id) REFERENCES Contact(contact_id);

ALTER TABLE Management
ADD CONSTRAINT FK_mgmt_dpt
FOREIGN KEY (dept_id) REFERENCES Department(dept_id);

ALTER TABLE Management
ADD CONSTRAINT FK_mgmt_emp
FOREIGN KEY (employee_id) REFERENCES Employee(employee_id);

ALTER TABLE Employee
ADD CONSTRAINT FK_emp_contact
FOREIGN KEY (contact_id) REFERENCES Contact(contact_id);

ALTER TABLE Employee
ADD CONSTRAINT FK_emp_dept
FOREIGN KEY (dept_id) REFERENCES Department(dept_id);

ALTER TABLE Payroll
ADD CONSTRAINT FK_pay_emp
FOREIGN KEY (employee_id) REFERENCES Employee(employee_id);

ALTER TABLE Work_hours
ADD CONSTRAINT FK_work_emp
FOREIGN KEY (employee_id) REFERENCES Employee(employee_id);

