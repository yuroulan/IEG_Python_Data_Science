# Problem 4
'''
Contact Details

Write a program to execute a query to display the details of a user from the 'user' table in a MySql database and also update contact details and display the details for that user.

         
In this program, display the user table first and prompt the user to provide a username. If the username is present in the user table, get the contact details to be updated and update it in the user table. Otherwise, Display an error message.

Table Schema:




Note: 
For display, the result set use PrettyTable 

For example : 
from prettytable import PrettyTable.
x = PrettyTable() 
x.add_row([....]) #Use this for add all the rows 
print x #To print the final result set  

     

[All text in bold corresponds to the input and rest corresponds to the output]

Sample Input and Output 1:

+----+-------+----------------+-----------+----------+

| Id |  Name | Contact Detail |  Username | Password |

+----+-------+----------------+-----------+----------+

| 1  |  John |   9876543210    |   johny   |  12345   |

| 2  | Peter |   9873216540   |  peterey  |  pet123  |

| 3  |  Adam |   9871236504   |  adamanta |  ad@123  |

| 4  | Linda |   8794561320   | lindahere |   abcd   |

| 5  |  Tony |   7894561230   |   tonii   |  abc123  |

+----+-------+----------------+-----------+----------+

Enter the username:

John

+----+------+----------------+----------+----------+

| Id | Name | Contact Detail | Username | Password |

+----+------+----------------+----------+----------+

| 1  | John |   9876543210   |  johny   |  12345   |

+----+------+----------------+----------+----------+

Enter the mobile number to be updated:

9621675431

+----+------+----------------+----------+----------+

| Id | Name | Contact Detail | Username | Password |

+----+------+----------------+----------+----------+

| 1  | John |   9621675431   |  johny   |  12345   |

+----+------+----------------+----------+----------+

 

Sample Input and Output 2:

+----+-------+----------------+-----------+----------+

| Id |  Name | Contact Detail |  Username | Password |

+----+-------+----------------+-----------+----------+

| 1  |  John |   9620685431   |   johny   |  12345   |

| 2  | Peter |   9873216540   |  peterey  |  pet123  |

| 3  |  Adam |   9871236504   |  adamanta |  ad@123  |

| 4  | Linda |   8794561320   | lindahere |   abcd   |

| 5  |  Tony |   7894561230   |   tonii   |  abc123  |

+----+-------+----------------+-----------+----------+

Enter the username:

admin

No such user is present
'''
