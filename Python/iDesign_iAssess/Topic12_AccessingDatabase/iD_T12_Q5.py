# Problem 5
'''
Delete User Details

 

Write a program to execute a query to display the details of a user from the 'user' table in MySQL database and also delete details given the user and display the details for the remaining user.

         
In this program, display the user table first and prompt the user to provide a username. If the username is present in the User table, delete a row and display the User table. Otherwise, Display an error message and then print the table.

Table Schema:



Note: 
For display, the result set use PrettyTable 

For example : 
from prettytable import PrettyTable.
x = PrettyTable() 
x.add_row([....]) #Use this for add all the rows 
print x #To print the final result set   

[All Texts in bold corresponds to the input and rest are output]

Sample Input and Output 1:

+----+-------+------------+-----------+----------+

| ID |  Name |   Mobile   |  Username | Password |

+----+-------+------------+-----------+----------+

| 1  |  John | 9876543210 |   johny   |  12345   |

| 2  | Peter | 9873216540 |  peterey  |  pet123  |

| 3  |  Adam | 9871236504 |  adamanta |  ad@123  |

| 4  | Linda | 8794561320 | lindahere |   abcd   |

| 5  |  Tony | 7894561230 |   tonii   |  abc123  |

+----+-------+------------+-----------+----------+

Enter the username to be deleted:

Jim

User not found

+----+-------+------------+-----------+----------+

| ID |  Name |   Mobile   |  Username | Password |

+----+-------+------------+-----------+----------+

| 1  |  John | 9876543210 |   johny   |  12345   |

| 2  | Peter | 9873216540 |  peterey  |  pet123  |

| 3  |  Adam | 9871236504 |  adamanta |  ad@123  |

| 4  | Linda | 8794561320 | lindahere |   abcd   |

| 5  |  Tony | 7894561230 |   tonii   |  abc123  |

+----+-------+------------+-----------+----------+

 

Sample Input and Output 2:

+----+-------+------------+-----------+----------+

| ID |  Name |   Mobile   |  Username | Password |

+----+-------+------------+-----------+----------+

| 1  |  John | 9876543210 |   johny   |  12345   |

| 2  | Peter | 9873216540 |  peterey  |  pet123  |

| 3  |  Adam | 9871236504 |  adamanta |  ad@123  |

| 4  | Linda | 8794561320 | lindahere |   abcd   |

| 5  |  Tony | 7894561230 |   tonii   |  abc123  |

+----+-------+------------+-----------+----------+

Enter the username to be deleted:

lindahere

Username lindahere with id=4 deleted successfully

+----+-------+------------+----------+----------+

| ID |  Name |   Mobile   | Username | Password |

+----+-------+------------+----------+----------+

| 1  |  John | 9876543210 |  johny   |  12345   |

| 2  | Peter | 9873216540 | peterey  |  pet123  |

| 3  |  Adam | 9871236504 | adamanta |  ad@123  |

| 5  |  Tony | 7894561230 |  tonii   |  abc123  |

+----+-------+------------+----------+----------+
'''

import mysql.connector
import configparser
import sys
from mysql.connector import Error
from prettytable import PrettyTable

# Read database configuration from file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

try:
    connection = mysql.connector.connect(
        host=dburl,
        port=port,
        user=username,
        password=password,
        database=dbname
    )

    if connection.is_connected():
        dbInfo = connection.get_server_info()

        cursor = connection.cursor()
        query = "SELECT * FROM user"
        cursor.execute(query)
        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID", "Name", "Mobile", "Username", "Password"]

        for row in records:
            table.add_row(row)

        print(table)

        username_to_delete = input("Enter the username to be deleted:")

        cursor.execute("SELECT * FROM user WHERE Username = %s", (username_to_delete,))
        user = cursor.fetchone()

        if user:
            cursor.execute("DELETE FROM user WHERE Username = %s", (username_to_delete,))
            connection.commit()
            print(f"Username {username_to_delete} with id={user[0]} deleted successfully")
        else:
            print("User not found")

        # Display updated table
        cursor.execute(query)
        records = cursor.fetchall()

        table.clear_rows()
        for row in records:
            table.add_row(row)

        print(table)

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")
