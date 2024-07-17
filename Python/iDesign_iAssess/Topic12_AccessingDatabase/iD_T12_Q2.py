# Problem 2
'''
Select Statement   

   
Write a program to execute a SELECT query to display all the records from 'user' table.

In this program, the SELECT statement is used to retrieve the records from the database based on the client's need. The retrieved data will be stored in a Result and this Result is used to display those selected records. Here, use a SELECT statement to display the records from the'user' table.

    
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

+----+-------+----------------+-----------+----------+
| Id |  Name | Contact Detail |  Username | Password |
+----+-------+----------------+-----------+----------+
| 1  |  John |   9876543210   |  johny   |  12345   |
| 2  | Peter |   9873216540   | peterey  |  pet123  |
| 3  |  Adam |   9871236504   | adamanta |  ad@123  |
| 4  | Linda |   8794561320   |lindahere |   abcd   |
| 5  |  Tony |   7894561230   |  tonii   |  abc123  |
+----+-------+----------------+-----------+----------+
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

    # to establish a connection
    connection = mysql.connector.connect(
        host = dburl,
        port = port,
        user = username,
        password = password,
        database = dbname
    )

    if connection.is_connected():
        dbInfo = connection.get_server_info()

        cursor = connection.cursor()
        query = "SELECT * FROM user"
        cursor.execute(query)

        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ['Id', 'Name', 'Contact Detail', 'Username', 'Password']

        for row in records:
            table.add_row(row)

        print(table)

except mysql.connector.Error as e:
    print(f"Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()