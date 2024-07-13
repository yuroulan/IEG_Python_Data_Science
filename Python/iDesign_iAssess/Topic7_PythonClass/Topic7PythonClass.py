# Problem 1
'''
Class with Public Attributes

Create a class named Person with the following 2 public attributes.

name

age

 

Include a constructor:

           __init__(self,name, age)

 

Create an object of class Person to test the above class.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

Sample Input and Output:

[All text in bold corresponds to input and the rest corresponds to output]

Enter name
Mahirl
Enter age
10
Person Details
Mahirl
10
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}\n{self.age}"

# from Person import Person

name = input("Enter name")
age = input("Enter age")
print("Person Details")
person = Person(name, age)
print(person)

#-----------------------------------------------------------------------------------------#

# Problem 2
'''
Class Method

Create a class named Person with the following 2 private attributes.

__name

__age

Include a constructor:

__init__(self,name, age)

Include a method:

__str__(self)

This method returns a string corresponding to person details in the format specified in the sample output.

Include a class method:

from_string(cls, person_str)

This method creates and returns an object of Person class from a string. This method accepts a class variable and a string. String contains the values for name and age in a comma separated format.

Create objects of class Person to test the above class.

Note:

A class method is one that belongs to the class as a whole. It doesn't require an instance. Instead, the class will automatically be sent as the first argument. A class method is declared with the @classmethod decorator.

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

Sample Input and Output:

[All text in bold corresponds to input and the rest corresponds to output]

Creating object using __init__ method

Enter name

Mahirl

Enter age

10

Person Details

Mahirl is 10 years old

Creating object using class method

Enter name and age in comma separated format

Chandra,40

Person Details

Chandra is 40 years old
'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(',')
        return cls(name.strip(), int(age.strip()))

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"

# from Person import Person

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)

#-----------------------------------------------------------------------------------------#

# Problem 3
'''
One-to-One Relationship – 1 (Unidirectional)

Create a class named Address with the following private_attributes

__street

__city

__state

 

Include a constructor

__init__(self, street, city, state)

 

Include a method

__str__(self)

This method returns a string corresponding to Address details in the format specified

in the sample output.

 

Create a class named Person with the following private_attributes

__name

__age

__address (of type Address)

 

Include a constructor

__init__(self, name, age, address)

 

Include a method

__str__(self)

This method returns a string corresponding to Person details in the format specified

in the sample output.

 

Create objects of the above classes and test them.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

 

Sample Input and Output 1:

[All text in bold corresponds to input and the rest corresponds to output]

 

Enter name

Mahirl

Enter age

10

Enter address

Enter street

LMC Street

Enter city

Salem

Enter state

Tamilnadu

Person Details

Mahirl is a person who is 10 years old and lives in the following address : LMC Street , Salem , Tamilnadu
'''
class Address:
	
	def __init__(self,street, city, state):
		self.__street = street
		self.__city = city
		self.__state = state
	
	def __str__(self):
		return f"{self.__street} , {self.__city} , {self.__state}"
		
class Person:
	
	def __init__(self,name, age, address):
		self.__name = name
		self.__age = age
		self.__address = address
	
	def __str__(self):
		return f"{self.__name} is a person who is {self.__age} years old and lives in the following address : {self.__address}"

person_name = input("Enter name\n")
person_age = input("Enter age\n")
print("Enter address")
street = input("Enter street\n")
city = input("Enter city\n")
state = input("Enter state\n")
person_address = Address(street,city,state)
person = Person(person_name, person_age,person_address)
print("Person Details")
print(person)

#-----------------------------------------------------------------------------------------#

# Problem 4
'''
One-to-Many Relationship [Bidirectional]

Create a class named City with the following private_attributes

__name

__state (of type State)

 

Include a constructor

__init__(self, name, state)

 

Include a method

__str__(self)

This method returns a string corresponding to City details in the format specified

in the sample output.

 

Create a class named State with the following private_attributes

__name

__city_list (of type City)

 

Include a constructor

__init__(self, name, city_list)

 

Include a method

__str__(self)

This method returns a string corresponding to State details in the format specified in the sample output.

 

Include @property decorator for name

Include @property decorator for city_list

Include @setter decorator for city_list

 

Create objects of the above classes and test them.


Note :
Perform case-sensitive string comparison.
Initially state_list have the below states.

Tamilnadu
Andhra
Karnataka
Kerala

If any new state is added other than the state in the list, it must be added to the state_list. [Refer sample input and output]

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

[All text in bold corresponds to input and the rest corresponds to output]

 

Sample Input and Output 1:

Enter City Details

Enter city name

Coimbatore

Enter state name

Tamilnadu

Do you want to add another city? Type Yes / No

Yes

Enter city name

Chennai

Enter state name

Tamilnadu

Do you want to add another city? Type Yes / No

Yes

Enter city name

Bangalore

Enter state name

Karnataka

Do you want to add another city? Type Yes / No

Yes

Enter city name

Vijayawada

Enter state name

Andhra

Do you want to add another city? Type Yes / No

Yes

Enter city name

Cochin

Enter state name

Kerala

Do you want to add another city? Type Yes / No

Yes

Enter city name

Bhopal

Enter state name

Madhya Pradesh

Do you want to add another city? Type Yes / No

No

 

City Details

 

Coimbatore is in state Tamilnadu

Chennai is in state Tamilnadu

Bangalore is in state Karnataka

Vijayawada is in state Andhra

Cochin is in state Kerala

Bhopal is in state Madhya Pradesh

 

State Details

 

Tamilnadu has 2 cities

Andhra has 1 cities

Karnataka has 1 cities

Kerala has 1 cities

Madhya Pradesh has 1 cities
'''
from City import City
from State import State

state_list = []
state_list.append(State("Tamilnadu",[]))
state_list.append(State("Andhra",[]))
state_list.append(State("Karnataka",[]))
state_list.append(State("Kerala",[]))

print("Enter City Details")
city_created_list = []
choice = "Yes"
while choice == "Yes" :
	city_name = input("Enter city name\n")
	state_name = input("Enter state name\n")
	state_found_flag = 0
	for state in state_list :
		if state_name == state.name :
			city = City(city_name, state)
			state.city_list.append(city)
			city_created_list.append(city)
			state_found_flag = 1
	if state_found_flag == 0 :
		state = State(state_name,[])
		state_list.append(state)
		city = City(city_name, state)
		city_created_list.append(city)
		state.city_list.append(city)
	choice = input("Do you want to add another city? Type Yes / No\n")

print("\nCity Details\n")
for city in city_created_list :
	print(city)

print("\nState Details\n")	
for state in state_list :
	print(state)
      
class City:
    def __init__(self, name, state):
        self.__name = name
        self.__state = state
    
    @property
    def name(self):
        return self.__name
    
    @property
    def state(self):
        return self.__state
    
    def __str__(self):
        return f"{self.__name} is in state {self.__state.name}"
    
class State:
    def __init__(self, name, city_list=None):
        self.__name = name
        if city_list is None:
            city_list = []
        self.__city_list = city_list
             
    @property
    def name(self):
        return self.__name
    @property
    def city_list(self):
        return self.__city_list

    @city_list.setter
    def city_list(self, city_list):
        self.__city_list = city_list
    
    def __str__(self):
        return f"{self.__name} has {len([city.name for city in self.__city_list])} cities"

# from Person import Person

person_first_name = input("Enter first name\n")
person_last_name = input("Enter last name\n")
person_age = input("Enter age\n")
person = Person(person_first_name, person_last_name, person_age)
print("Full name of the person is ",person.fullname())
print("Person Details")
print(person)

#-----------------------------------------------------------------------------------------#

# Problem 5
'''
Duplicate User

Tina works in a consultancy, and she was currently associated with the task where she had to remove the duplicate users from the list by comparing the phone numbers of the users. She thought writing code as per the requirement would make her work easier. So she asks one of her friends, to write a code for her. Imagine you are Tina's friend, help her by writing the code as it is required. 

Write a Python code to check duplicate user details. There can be only one user with a specific mobile number. If two users exist with the same mobile number they are duplicate. Check whether user information is the same or not by overriding the equals method.

 

Create a User class with the following attributes 

Attributes

Datatype

name

str

username

str

password

str

mobile_number

int

 

Use __init__() constructor to initialize the variables with respect to class.

Override __eq__() method that compares mobile_number of the two objects.

 

Input format :

Input consists of 2 user’s details, which contains (name, username, password, mobile_number).

Output format :

The output is a string value, denoting whether the users were same or not by comparing the mobile number of the user.

 

[All Texts in bold corresponds to the input and rest are output] 

Sample Input and Output - 1:
Enter the details of User 1
Name :
Meena
Username :
Meena2020
Password :
Basic
Mobile Number :
1234567890
Enter the details of User 2
Name :
Meena
Username :
Meena1010
Password :
Probob
Mobile Number :
0987654321
User 1 and User 2 are not equal

Sample Input and Output - 2:
Enter the details of User 1
Name :
Vasu
Username :
Va450
Password :
particles
Mobile Number :
9894098490
Enter the details of User 2
Name :
Vasu
Username :
Vasavi
Password :
500
Mobile Number :
9894098490
User 1 and User 2 are equal
'''
# Main.py
from User import User

def get_user_details(user_number):
    print(f"Enter the details of User {user_number}")
    name = input("Name :\n")
    username = input("Username :\n")
    password = input("Password :\n")
    mobile_number = int(input("Mobile Number :\n"))
    return User(name, username, password, mobile_number)

# Main function to compare two users
def main():
    user1 = get_user_details(1)
    user2 = get_user_details(2)

    if user1 == user2:
        print(f"User 1 and User 2 are equal")
    else:
        print(f"User 1 and User 2 are not equal")

if __name__ == "__main__":
    main()

# User.py
class User:
    def __init__(self,name,username,password,mobile_number):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    def __eq__(self, other):
        if isinstance(other, User):
            return self.mobile_number == other.mobile_number
        return False
#-----------------------------------------------------------------------------------------#

# Problem 6
'''
Calculate Cost using Date
Praveen who is working as Reservation Manager, asks for help from the development team to build a code that calculates the total cost to be charged on the customer by considering the date of Booking, date of vacating the hall, and cost per day. Imagine you are working in the development team and this task is assigned to you.  Write a program to calculate the total amount charged by the Hall Manager.
Create a class Hall in ‘Hall.py’ with the following variables.

Variable	DataType
start_date	Date
end_date	Date
cost_per_day	int
 

Use __init__() constructor to initialize the variables with respect to class.

Use a 3 Argument constructor (start_date, end_date, cost_per_day).
Use the following methods in Hall class to perform the corresponding operation.
 
Method	Description
no_days(self)	This method is used to calculate the number of days Item (say Hall) booked or used.
cost(self,d)	Calculate the Total amount for Item (say Hall). Where ‘d’ is a number of days that is been calculated. (Call this method inside the no_days() method).
 
Note:
The format of the date is  "Jul 1 2014" (without quotes). 
 
Input Format:
The first line of the input is the Start date
The Second line of the input is the end date. 
The Third line of input consists of cost per day.
Output Format:
Display the number of days of stay and the total cost to be charged with the customer.
Refer to sample input and output for formatting specifications.
Note :
→ Output statements should be printed inside the Hall class and not in the Main class.
→ no_days() method should be called from the Main class and the cost() method should be called from no_days() method.
 
All text in bold corresponds to input and the rest corresponds to output.

Sample Input-Output:
Enter Start time
Dec 25 2017
Enter the End time
Dec 27 2017
Enter the cost per day
1500

Total number of days 2
Total cost 3000 
'''
# Main.py
from Hall import Hall
from datetime import datetime

def main():
    print("Enter Start time")
    start_date_str = input()
    start_date = datetime.strptime(start_date_str, "%b %d %Y")
    
    print("Enter the End time")
    end_date_str = input()
    end_date = datetime.strptime(end_date_str, "%b %d %Y")
    
    print("Enter the cost per day")
    cost_per_day = int(input())
    
    hall = Hall(start_date, end_date, cost_per_day)
    hall.no_days()

if __name__ == "__main__":
    main()


# Hall.py

from datetime import datetime

class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = start_date
        self.end_date = end_date
        self.cost_per_day = cost_per_day

    def no_days(self):
        delta = self.end_date - self.start_date
        days = delta.days
        self.cost(days)  # Call cost method with the number of days calculated
        return days

    def cost(self, days):
        total_cost = days * self.cost_per_day
        print(f"Total number of days {days}")
        print(f"Total cost {total_cost}")
#-----------------------------------------------------------------------------------------#

# Problem 7
'''
Student Details

Veena is a clerk in a college. She keeps the records of all the student details in her system. She is finding it difficult to manage the records manually so she contacts her friend Tina a software Engineer, to help her by writing a code that takes all the student details and displays in the ordered manner. Tina wanted to help Veena but she is not so confident in coding. Help Tina in writing code as required by Veena.   

Write a program to display the details of the Student by overriding the __str__() Method.

Create a class named Student with the following private attributes.

Data Type

Variable Name

int

__id

str

__username

str

__password

str

__name

str

__address

str

__city

int

__pincode

int

__contact_number

str

__email


Use __init__() constructor to initialize the attributes with respect to class.


And this class includes the following member function. 

No

Method Name

Method Description

1

__str__()    

This method, returns the student details of the current object.


Input Format:  
The first input corresponds to the student's id.
The second input corresponds to the student's username.
The third input corresponds to the student's password.
The fourth input corresponds to the student's name.
The fifth input corresponds to the student's address.
The sixth input corresponds to the student's city.
The seventh input corresponds to the student's address Pincode.
The eighth input corresponds to the student's contact number.
The ninth input corresponds to the student's email id.

Output Format:  
All the user entered details will be displayed one by one(newline).
The details are printed inside the __str__() method.

Refer to sample input and output for formatting specifications.

[All text in bold corresponds to input and the rest corresponds to output.]
Sample input and output: 

Enter the student id

1

Enter the  student's username

nicky

Enter the password

nicky

Enter the name of the student

nicky

Enter the address

nantoor

Enter the city

mysuru

Enter the pincode

123456

Enter the contact number

1234567890

Enter the email id

nicky@gmail.com

Id :  1
User Name :  nicky
Password :  nicky
Name :  nicky
Address :  nantoor
city :  mysuru
Pincode :  123456
Contact Number :  1234567890
email :  nicky@gmail.com
'''
# Import the Student class from Student.py (assuming it's in the same directory)
from Student import Student

# Take input from the user
u_id = int(input("Enter the student id\n"))
username = input("Enter the student's username\n")
password = input("Enter the password\n")
name = input("Enter the name of the student\n")
address = input("Enter the address\n")
city = input("Enter the city\n")
pincode = int(input("Enter the pincode\n"))
contact_number = input("Enter the contact number\n")  # Keep contact number as string
email = input("Enter the email id\n")

# Create a Student object
student = Student(u_id, username, password, name, address, city, pincode, contact_number, email)

# Print the student details using the __str__() method
print(student)

# Define the Student class
class Student:
    def __init__(self, _id, username, password, name, address, city, pincode, contact_number, email):
        self.__id = _id
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__city = city
        self.__pincode = pincode
        self.__contact_number = contact_number
        self.__email = email

    def __str__(self):
        details = [
            f"Id :  {self.__id}",
            f"User Name :  {self.__username}",
            f"Password :  {self.__password}",
            f"Name :  {self.__name}",
            f"Address :  {self.__address}",
            f"City :  {self.__city}",
            f"Pincode :  {self.__pincode}",
            f"Contact Number :  {self.__contact_number}",
            f"Email :  {self.__email}"
        ]
        return "\n".join(details)

#-----------------------------------------------------------------------------------------#

# Problem 8
'''
Hierarchical Inheritance

Create a class named Employee with the following 3 protected attributes
    _name
    _pay
    _email

Include a __init__ method to initialize the values.
    Name and pay are passed as arguments. Email is formed by concatenating name
    with .”@gmail.com”

Include @property decorator for the attribute name.

Create a subclass named Developer (derived from the Employee class) with 1 additional attribute.
    _prog_lang
Include an appropriate  __init__ method to initialize the values.

Create a subclass named Manager (derived from the Employee class) with 1 additional attribute.
    _employees

the employees is a list that contains the list of employees assigned to a manager.

Include an appropriate  __init__ method to initialize the values.
    In this method, set the default value of employees to None.
    Inside the method, if the value of employees is None, initialize it to a []. (empty list)

Include addEmployee()  and removeEmployee() methods.
    
Create another class named Utility. This class is normally used for adding all commonly used methods. 
Include a method named to return a list of employees under each manager.

Create objects of the above classes and test them.
The manager list is prepopulated. Assume that we are not going to add a new Managers in this program.

Input and Output Format:
Refer Sample Input and Output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]

Sample Input and Output:
Menu
1)Employee
2)Developer

Enter choice
1
Enter Employee details in comma separated format
Esha,20000
Enter manager name
Arun
Do you want to continue? Type yes/no
yes
Menu
1)Employee
2)Developer

Enter choice
2
Enter Developer details in comma separated format
Fathima,30000,Java
Enter manager name
Deva
Do you want to continue? Type yes/no
yes
Menu
1)Employee
2)Developer

Enter choice
2
Enter Developer details in comma separated format
Geetha,28000,Java
Enter manager name
Arun
Do you want to continue? Type yes/no
no

Manager and Employee Allocation List


Manager Name :Arun
Employee List :
Esha Geetha 

Manager Name :Babu
Employee List :
None

Manager Name :Chandru
Employee List :
None


Manager Name :Deva
Employee List :
Fathima
'''
from Employee import Employee
from Developer import Developer
from Manager import Manager
from Utility import Utility


manager_list = []
manager_list.append(Manager("Arun",80000))
manager_list.append(Manager("Babu",100000))
manager_list.append(Manager("Chandru",60000))
manager_list.append(Manager("Deva",60000))

input_obj_list = []
choice = "yes"
while choice=="yes" :
	print("Menu\n1)Employee\n2)Developer\n")
	choice1 = input("Enter choice\n")
	if choice1 == "1" :
		input_str = input("Enter Employee details in comma separated format\n")
		name, pay = input_str.split(",")
		employee = Employee(name, pay)
		input_obj_list.append(employee)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(employee)
				
	else :
		input_str = input("Enter Developer details in comma separated format\n")
		name, pay, prog_lang = input_str.split(",")
		developer = Developer(name, pay, prog_lang)
		input_obj_list.append(developer)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(developer)
	choice = input("Do you want to continue? Type yes/no\n")

print("\nManager and Employee Allocation List")	
Utility.print_employees_under_each_manager(manager_list)
print("\n")

from Employee import Employee
 
class Developer(Employee):
    def __init__(self, name, pay, prog_lang) :
        Employee.__init__(self, name, pay)
        self.prog_lang = prog_lang
    def __str__(self) :
        return "" + Employee.__str__(self)
    
from Employee import Employee
class Manager(Employee):
 
    def __init__(self, name, pay, employees=None):
        Employee.__init__(self, name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.employees.append(emp)
        else:
            raise ValueError("Only Employee instances can be added")
 
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            raise ValueError("Employee not found")
        
from Employee import Employee
from Developer import Developer
from Manager import Manager
 
class Utility:
    @staticmethod
    def print_employees_under_each_manager(manager_list):
        for manager in manager_list:
            if not isinstance(manager, Manager):
                raise ValueError("Only Manager instances can be printed")
            print(f"\nManager Name: {manager.name}")
            if manager.employees:
                print("Employee List:")
                for employee in manager.employees:
                    print(employee.name)
            else:
                print("Employee List:")
                print("None")
class Employee:
 
    def __init__(self, name, pay) :
        self._name = name
        self.pay = pay
    @property
    def name(self) :
        return self._name
    def __str__(self) :
        return self.name
#-----------------------------------------------------------------------------------------#

# Problem 9
'''
College Details (Overloading)
Write a program to illustrate Method Overloading in Python for the following College class.

 

Create a class named College.

There are no attributes in this class.

 
Invoke the __str__() function two times with different different arguments to implement function overloading, as below:

1.  __str__(). print the College Id,College name ,city,state,pincode of a particular College.
2.  __str__(). print the College name, contactNumber and emailId of a particular College.

Input and Output Format:

Refer sample input and output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.


Sample Input and Output:

1. Enter College address and Display
2. Enter  the contact details and Display
3. exit
Enter your choice
1
Enter the College id
Bit01
Enter the College name
Bit Meshra
Enter the City
Ranchi
Enter the State
Jharkhand
Enter the Pincode
822101
id : Bit01,Name : Bit Meshra,City : Ranchi,State : Jharkhand,Pincode : 822101

Enter your choice
2
Enter the name of the College
Nit jamshedpur
Enter the contact number
9876543210
Enter the email id
nit@ideal.in
Name : Nit jamshedpur,Contact Number : 9876543210,Email : nit@ideal.in

Enter your choice
3
'''

class College:
    def __init__(self, collId=None, collName=None, city=None, state=None, pincode=None, contactNum=None, email=None):
        self.collId = collId
        self.collName = collName
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNum = contactNum
        self.email = email
    
    def __str__(self):
        if self.collId and self.city and self.state and self.pincode:
            return f"id : {self.collId}\nName : {self.collName}\nCity : {self.city}\nState : {self.state}\nPincode : {self.pincode}\n"
        elif self.contactNum and self.email:
            return f"Name : {self.collName}\nContact Number : {contactNum}\nEmail : {email}\n"
        else:
            return "No details"
        
print("1. Enter College address and Display\n\
2. Enter  the contact details and Display\n\
3. exit")

while True: 
    userOption = int(input("Enter your choice"))

    if userOption == 1:
        collId = input("Enter the College id\n")
        collName = input("Enter the College name\n")
        city = input("Enter the City\n")
        state = input("Enter the State\n")
        pincode = input("Enter the Pincode\n")
        d1 = College(collId=collId, collName=collName, city=city, state=state, pincode=pincode)
        print(d1)

    elif userOption == 2:
        collName = input("Enter the name of the College\n")
        contactNum = input("Enter the contact number\n")
        email = input("Enter the email id\n")
        d2 = College(collName=collName, contactNum=contactNum, email=email)
        print(d2)

    elif userOption == 3:
        break

    else:
        print("Invalid Choice")

# Problem 10
	
		
	


	
		

		
		





