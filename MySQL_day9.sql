Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 23
Server version: 8.0.41 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE company_db;
Query OK, 1 row affected (0.01 sec)

mysql> USE company_db;
Database changed
mysql> -- Create the departments Table
mysql> CREATE TABLE departments (department_id INT PRIMARY KEY,department_name VARCHAR(100) NOT NULL);
Query OK, 0 rows affected (0.03 sec)

mysql> -- Create the employees Table
mysql> CREATE TABLE employees (employee_id INT PRIMARY KEY,employee_name VARCHAR(100) NOT NULL,department_id INT,FOREIGN KEY (department_id) REFERENCES departments(department_id));
Query OK, 0 rows affected (0.06 sec)

mysql> -- Insert data into the departments table
mysql> INSERT INTO departments (department_id, department_name) VALUES (1, 'Human Resources'),(2, 'IT'),(3, 'Finance');
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> -- Insert data into the employees table
mysql> INSERT INTO employees (employee_id, employee_name, department_id) VALUES (101, 'Karim Nadkar', 1),(102,'Atharva More',2),(103,'Shuel Sawant',3),(104,'Shubham Gundekar',2),(105,'Aniket Patil',2),(106,'Sakib Mulani',3);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> -- Scenario 1: Retrieve Employees with Department Names Using INNER JOIN
mysql> SELECT e.employee_id, e.employee_name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.department_id;
+-------------+------------------+-----------------+
| employee_id | employee_name    | department_name |
+-------------+------------------+-----------------+
|         101 | Karim Nadkar     | Human Resources |
|         102 | Atharva More     | IT              |
|         104 | Shubham Gundekar | IT              |
|         105 | Aniket Patil     | IT              |
|         103 | Shuel Sawant     | Finance         |
|         106 | Sakib Mulani     | Finance         |
+-------------+------------------+-----------------+
6 rows in set (0.00 sec)

mysql> -- Scenario 2: Retrieve Employee Names & Department Names Using LEFT JOIN
mysql> SELECT e.employee_name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id;
+------------------+-----------------+
| employee_name    | department_name |
+------------------+-----------------+
| Karim Nadkar     | Human Resources |
| Atharva More     | IT              |
| Shuel Sawant     | Finance         |
| Shubham Gundekar | IT              |
| Aniket Patil     | IT              |
| Sakib Mulani     | Finance         |
+------------------+-----------------+
6 rows in set (0.00 sec)

mysql>