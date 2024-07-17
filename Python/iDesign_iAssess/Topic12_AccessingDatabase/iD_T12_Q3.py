# Problem 3
'''
Insert Statement

          
Write a program to execute an INSERT query to accept run-time parameters and display all the records from the 'user' table.

Table Schema:

                                                                                                                                            

 

Table Name: 'user'
Note: For display, the result set use PrettyTable 
For example : 
from prettytable import PrettyTable.
x = PrettyTable() 
x.add_row([....]) #Use this for add all the rows 
print x #To print the final result set

[All text in bold corresponds to the input and rest corresponds to the output]
Sample Input/Output:

Enter the user detail in CSV format
Antony,9873216540,Antonie,an@987
+----+--------+----------------+-----------+----------+
| Id |  Name  | Contact Detail |  Username | Password |
+----+--------+----------------+-----------+----------+
| 1  |  John  |   9876543210   |   johny   |  12345   |
| 2  | Peter  |   9873216540   |  peterey  |  pet123  |
| 3  |  Adam  |   9871236504   |  adamanta |  ad@123  |
| 4  | Linda  |   8794561320   | lindahere |   abcd   |
| 5  |  Tony  |   7894561230   |   tonii   |  abc123  |
| 6  | Antony |   9873216540   |  Antonie  |  an@987  |
+----+--------+----------------+-----------+----------+
'''
import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Read database configuration from mysql.properties
config = configparser.RawConfigParser()
config.read('mysql.properties')

dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

x = PrettyTable()
x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]

try:
    mydb = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password
    )
    cursor = mydb.cursor(buffered=True)

    alterQuery = "ALTER TABLE user MODIFY id BIGINT AUTO_INCREMENT"
    cursor.execute(alterQuery)
    mydb.commit()

    print("Enter the user detail in CSV format")
    u = input()
    d = u.split(",")

    insertQuery = "INSERT INTO user (Name,Contactdetail,Username,Password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insertQuery, (d[0], d[1], d[2], d[3]))
    mydb.commit()

    selectQuery = "SELECT * FROM user"
    cursor.execute(selectQuery)
    result = cursor.fetchall()

    for row in result:
        x.add_row([row[0], row[1], row[2], row[3], row[4]])

    print(x)

except Error as e:
    print(e)

finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None:
        mydb.close()
