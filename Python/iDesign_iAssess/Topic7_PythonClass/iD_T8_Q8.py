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