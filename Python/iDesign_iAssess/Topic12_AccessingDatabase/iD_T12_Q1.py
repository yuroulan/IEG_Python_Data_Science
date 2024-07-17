# Problem 1
'''
Item Details

   

Write a program to execute a SELECT query to display all the records from ‘item’ table.

In this program, the SELECT statement is used to retrieve the records from the database based on the client's need. The retrieved data will be stored in a Result and this Result is used to display those selected records. Here, use a SELECT statement to display the records from the ‘item’ table.

Table Schema:



Note: 
For display the result set use PrettyTable 

For example : 
from prettytable import PrettyTable.
x = PrettyTable() 
x.add_row([....]) #Use this for add all the rows 
print x #To print the final result set   

[All text in bold corresponds to the input and rest corresponds to the output]

Sample Input and Output:

+----+-------------+---------+--------------+
| ID |     Name    | Deposit | Cost per day |
+----+-------------+---------+--------------+
| 1  |     Food    | 50000.0 |   10000.0    |
| 2  | Electronics | 85000.0 |   15000.0    |
| 3  |   Fashion   | 36000.0 |    8000.0    |
| 4  |   Grooming  | 15000.0 |    5000.0    |
| 5  |    Books    | 20000.0 |    7500.0    |
+----+-------------+---------+--------------+
'''


import mysql.connector,configparser,sys
from mysql.connector import Error
from prettytable import PrettyTable

try:
    # to read database
    config = configparser.RawConfigParser()
    config.read('mysql.properties')

    dburl = config.get('DatabaseSection', 'db.host');
    dbname = config.get('DatabaseSection', 'db.schema');
    username = config.get('DatabaseSection', 'db.username');
    password = config.get('DatabaseSection', 'db.password');
    port = config.get('DatabaseSection', 'db.port');

    # to establish a connection to mySql
    connection = mysql.connector.connect(
        host = dburl,
        port = port,
        user = username,
        password = password,
        database = dbname
    )

    if connection.is_connected():
        dbInfo = connection.get_server_info()
        # print(f"Connected to MySQL Server version {dbInfo}")

        # to execute SELECT query
        cursor = connection.cursor()
        query = "SELECT * FROM item"
        cursor.execute(query)

        # to fetch records
        records = cursor.fetchall()

        # to create pretty table
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Deposit', 'Cost per day']

        for row in records:
            table.add_row(row)

        print(table)

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")
