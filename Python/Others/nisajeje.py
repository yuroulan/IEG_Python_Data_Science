# class Passport:  # parent, property of customer, 2
#     def __init__(self, country, passportNum):
#         self.country = country
#         self.passportNum = passportNum

#     def __str__(self):
#         return f"Country : {self.country} \nPassport Number : {self.passportNum}"

# class Customer:  # child, 1
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.icNum = ""
#         self.passport = None

#     def __str__(self):
#         message = f"First Name : {self.firstName}\n"
#         message = message + f"Last Name : {self.lastName}\n"
#         message = message + f"IC Number : {self.icNum}\n"
#         if self.passport != None:
#             message = message + f"{self.passport}"
#         return message

# # List to store multiple customers
# customers = []

# # Predefined first names and last names (example)
# names = [("Peter", "Parker"), ("Clark", "Kent"), ("Bruce", "Wayne")]

# # Loop to collect data for multiple customers
# for firstName, lastName in names:
#     # Collecting input from the user
#     print(f"Enter details for {firstName} {lastName}:")
#     country = input("Enter passport country: ")
#     passportNum = input("Enter passport number: ")

#     # 1) create instance of parent obj
#     # 2) create instance of child obj
#     # 3) assign child object on the property in the parent object
#     customer_instance = Customer(firstName, lastName)
#     passport_instance = Passport(country, passportNum)
#     customer_instance.passport = passport_instance

#     # Add the customer to the list
#     customers.append(customer_instance)

# # Print details for all customers
# for customer in customers:
#     print("\n" + str(customer))

class ElectronicProducts:
    def __init__(self, prodId, prodName, prodAvailabilityQtt, prodPrice):
        self.prodId = prodId
        self.prodName = prodName
        self.prodAvailabilityQtt = prodAvailabilityQtt
        self.prodPrice = prodPrice
        self.prodType = {
            prodId:{"Product Name":{prodName},
            "Product Availabile Quantity":{prodAvailabilityQtt},
            "Product Price":{prodPrice}
            }
        }

    def addItem(self, prodId, prodName, prodAvailabilityQtt, prodPrice):
        self.prodType[prodId] = {
            "Product Name":{prodName},
            "Product Availabile Quantity":{prodAvailabilityQtt},
            "Product Price":{prodPrice}
        }

    def updateItem(self):

        

    def checkItemDetails(self):
        if 





# =-------------------------------------------------------------------------------------------------------------=

# # to take input






# # n = int(input("Enter size of list\n"))

# # if n == 0:
# #     print("Invalid Input")

# # else:
# #     elements = []
# #     print("Enter the elements in list")
# #     for i in range(n):
# #         elemList = int(input())
# #         elements.append(elemList)

# #     x = lambda num: num % 13 == 0
# #     div = [num for num in elements if x(num)]
# #     print(" ".join(map(str, div)))
         
# # print("Invalid Input")

    
# # # Define the lambda function correctly
# # def is_divisible_by_thirteen(a):
# #     return a % 13 == 0

# # # Get the size of the list from the user
# # n = int(input("Enter size of list\n"))

# # if n > 0:
# #     # Initialize an empty list to store the elements
# #     elements = []

# #     # Prompt the user to enter each element
# #     print("Enter the elements in list:")
# #     for i in range(n):
# #         elemList = int(input())
# #         elements.append(elemList)
    
# #     # Use list comprehension to filter numbers divisible by 13
# #     div = [num for num in elements if is_divisible_by_thirteen(num)]

# #     # Check if there are any numbers divisible by 13 and print them
# #     if div:
# #         print(" ".join(map(str, div)))
# #     else:
# #         print("No numbers divisible by 13")
# # else:
# #     # If the size of the list is not greater than 0, print "Invalid input"
# #     print("Invalid input")

# # a = int(input())
# # b = int(input())

# # if a <= b:

# #     prime = []

# #     for i in range(a, b + 1):
# #         if i == 1:
# #             continue  # Skip 1 as it is not a prime number
        
# #         primeNum = True
        
# #         for divisor in range(2, int(i ** 0.5) + 1):
# #             if i % divisor == 0:
# #                 primeNum = False
# #                 break 
        
# #         if primeNum:
# #             prime.append(i)
    
# #     for i in prime:
# #         print(i, end=" ")


# # userContent = input("Enter your full sentences : ")
# # # let say input is = lumberjacks background downstream six-year-old

# # contentLower = userContent.lower()

# # characters = list(contentLower)
# # # print(characters)

# # uniqueChar = {char for char in characters if char.isalpha()}
# # # print(uniqueChar)
# # # print(len(uniqueChar))

# # if len(uniqueChar) == sum(char.isalpha for char in characters):
# #     print(f"The sentence '{userContent}' is not an isogram.")
# # else:
# #     print(f"The sentence '{userContent}' is an isogram.")

# # userContent = input("Enter your full sentences: ")
# # # Example input: lumberjacks background downstream six-year-old

# # # Convert the input sentence to lowercase
# # contentLower = userContent.lower()

# # # Extract characters from the input
# # characters = list(contentLower)
# # print(characters)

# # # Extract unique alphabetic characters
# # uniqueChar = {char for char in characters if char.isalpha()}
# # print(uniqueChar)
# # print(len(uniqueChar))

# # # Check if the length of unique characters set is equal to the count of alphabetic characters
# # if len(uniqueChar) == sum(char.isalpha() for char in characters):
# #     print(f"The sentence '{userContent}' is an isogram.")
# # else:
# #     print(f"The sentence '{userContent}' is not an isogram.")

    
# # -- >> Problem 6 << -- #

# # class userStr:
# #     def __init__(self):
# #         self.strFromUsers = input("Enter any words : ")
# #     def getStr(self):
# #         return self.strFromUsers
# #     def printStr(self):
# #         print(f"String from user : ", self.strFromUsers)

# # strInpUser = userStr()
# # strInpUser.printStr()

# '''
# # Write a Python class Employee with properties id, name, salary, 
# # and department and methods like _init_ calculateSalary, assignDepartment and _str_.

# # Sample Employee Data:

# # "E7876", "ADAMS", 50000, "ACCOUNTING"
# # "E7499", "JONES", 45000, "RESEA
# # "E7900", "MARTIN", 50000, "SALES"
# # "E7698", "SMITH", 55000, "OPERATIONS"

# # **Problem 7**

# Write a Python class Employee with properties id, name, salary, and department and methods like \__init__ calculateSalary, assignDepartment and \__str__.

# Sample Employee Data:

# ```
# "E7876", "ADAMS", 50000, "ACCOUNTING"
# "E7499", "JONES", 45000, "RESEARCH"
# "E7900", "MARTIN", 50000, "SALES"
# "E7698", "SMITH", 55000, "OPERATIONS"
# ```
# # Use 'assignDepartment' method to change the department of an employee.

# # Use '__str__' method to print the details of an employee.

# # Use 'calculateSalary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary.

# # Overtime is calculated as following formula:
# # overtime = hours_worked - 50
# # Overtime amount = (overtime * (salary / 50))
# # '''

# print("LIST OF EMPLOYEES DETAILS\n")

# class Employee:
#     def __init__(self, empId, empName, empSalary, empDepartment):
#         self.empId = empId
#         self.empName = empName
#         self.empSalary = empSalary
#         self.empDepartment = empDepartment

#     def __str__(self):
#         return f"Employee Id : {self.empId}\n\
# Employee Name : {self.empName}\n\
# Employee Salary : RM{self.empSalary:0.2f}\n\
# Employee Department : {self.empDepartment}\n"

#     def calculateSalary(self, empHoursWorked):
#         if empHoursWorked > 50:
#             overTime = empHoursWorked - 50
#             otAmnt = overTime * (self.empSalary / 50)
#             self.empSalary += otAmnt

#         return self.empSalary
    
#     def assignDepartment(self, empNewDepartment):
#         self.empDepartment = empNewDepartment

# employees = [
#     Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
#     Employee("E7499", "JONES", 45000, "RESEARCH"),
#     Employee("E7900", "MARTIN", 50000, "SALES"),
#     Employee("E7698", "SMITH", 55000, "OPERATIONS")
# ]

# # to print list of all employee details
# for employee in employees:
#     print(employee)

# # user option to edit or not
# while True:
#     userOption = input("\nDo you want to edit the content?\n\
# If yes, choose 'S' to edit content for salary and 'D' for department.\n\
# If no, choose 'E' to exit.\n\n\
# Your choose : ")
    
#     if userOption == 'E':
#         break 

#     elif userOption == 'S':
#     # to change salary if employee do overtime
#         try:
#             empIdNum = empIdNum = input("Enter employee Id to edit employee new salary : ")
#             empHoursWorked = int(input("Enter the number of hours worked : "))
#             editDone = False
#             for employee in employees:
#                 if employee.empId == empIdNum:
#                     oldEmpSalary = employee.empSalary
#                     empNewSalary = employee.calculateSalary(empHoursWorked)
#                     print(f"The new salary for {employee.empName} [RM{oldEmpSalary:0.2f}] is : RM{empNewSalary:0.2f}")
#                     print("\nAfter update content :")
#                     print(employee)
#                     editDone = True
#                     break
#             if not editDone:
#                 print(f"Employee for Id Number : {empIdNum} is not found.\n")
#         except:
#             print("Invalid input for hours worked. Please make sure its in integer.")

#     elif userOption == 'D':
#     # to change employee department
#         empIdNum = input("Enter employee Id to edit employee new department : ")
#         empNewDepartment = input("Enter employee new department : ")
#         editDone = False
#         for employee in employees:
#             if employee.empId == empIdNum:
#                 oldEmpDepartment = employee.empDepartment
#                 employee.assignDepartment(empNewDepartment)
#                 print(f"The new department for {employee.empName} [{oldEmpDepartment}] is : {empNewDepartment}")
#                 print("\nAfter update content : ")
#                 print(employee)
#                 editDone = True
#                 break
#         if not editDone:
#             print(f"Employee for Id Number {empIdNum} is not found.\n")

#     print("UPDATED EMPLOYEES DETAILS: \n")
#     for employee in employees:
#         print(employee)

# class ElectronicProducts:
#     def __init__(self, prodId, prodName, prodAvailabilityQtt, prodPrice):
#         self.prodId = prodId
#         self.prodName = prodName
#         self.prodAvailabilityQtt = prodAvailabilityQtt
#         self.prodPrice = prodPrice
#         self.prodType = {
#             prodId:{"Product Name":{prodName},
#             "Product Availabile Quantity":{prodAvailabilityQtt},
#             "Product Price":{prodPrice}
#             }
#         }

#     def addItem(self, prodId, prodName, prodAvailabilityQtt, prodPrice):
#         self.prodType[prodId] = {
#             "Product Name":{prodName},
#             "Product Availabile Quantity":{prodAvailabilityQtt},
#             "Product Price":{prodPrice}
#         }

#     def updateItem(self):
        

#     def checkItemDetails(self):
#         for product in self.prodId:
#             print(self.prodName("Product Name : "))
#             print(self.prodAvailabilityQtt("Product Availability Quantity : "))
#             print(self.prodPrice("Price : "))














