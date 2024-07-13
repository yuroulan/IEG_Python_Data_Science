# Problem 1
'''
Problem 1:

A pangram is a sentence using every letter of the alphabet at least once. 
It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) 
or upper-case (e.g. K).

For this exercise, a sentence is a pangram if it contains each of the 26 letters 
in the English alphabet.

Example: The quick brown fox jumps over the lazy dog.

Your task is to figure out if a sentence is a pangram.
'''

content = "The quick brown fox jumps over the lazy dog."    # set sentence as content

# set into lowercase to avoid upper case and lowercase of same character double the value
contentLower = content.lower()  

# to get list of individual char of contentLower including non alphabet
characters = list(contentLower)
# print(characters)
# print(len(characters))

# to exclude non alphabet characters
uniqueChar = {char for char in characters if char.isalpha()}
# print(uniqueChar)
# print(len(uniqueChar))

# declare set of characters
# sameChar = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
# , "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
sameChar = set("abcdefghijklmnopqrstuvwxyz")

# uniquewords = uniqueChar.difference(sameChar)

if uniqueChar <= sameChar:
    print(f"The sentence '{content}' is a pangram.")
else:
    print(f"The sentence '{content}' is not a pangram.")

#-----------------------------------------------------------------------------------------------#

# Problem 2
'''
Problem 2:

An isogram (also known as a "non-pattern word") is a word or phrase 
without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks background downstream six-year-old

The word isograms, however, is not an isogram, because the s repeats.

Your task is to figure out if the user input is isogram
'''
userContent = input("Enter your full sentences : ")
# let say input is = lumberjacks background downstream six-year-old

contentLower = userContent.lower()

characters = list(contentLower)
# print(characters)

uniqueChar = {char for char in characters if char.isalpha()}
# print(uniqueChar)
# print(len(uniqueChar))

if len(uniqueChar) == sum(char.isalpha() for char in characters):
    print(f"The sentence '{userContent}' is an isogram.")
else:
    print(f"The sentence '{userContent}' is not an isogram.")
    
#-----------------------------------------------------------------------------------------------#
# Problem 3
'''
Parse and evaluate simple math word problems returning the answer as an integer.

What is 5?    -> 5
What is 5 plus 13?    -> 18
What is 7 minus 5?    -> 2
What is 6 multiplied by 4?     -> 24
What is 25 divided by 5?       -> 5
What is 5 plus 13 plus 6?      -> 24
What is 3 plus 2 multiplied by 3?       -> 15
'''
def evaluateSimpleMath(problem):
    problem = problem.lower()
    problem = problem.replace("what is", "").strip()
    problem = problem.replace("plus", "+")
    problem = problem.replace("minus", "-")
    problem = problem.replace("multiplied by", "*")
    problem = problem.replace("divided by", "/")
    problem = problem.replace("?", "").strip()

    try:
        result = eval(problem)
        return int(result)
    except Exception as e:
        print("Error:", e)

problems = [
    "What is 5?",    
    "What is 5 plus 13?",    
    "What is 7 minus 5?",    
    "What is 6 multiplied by 4?",   
    "What is 25 divided by 5?",   
    "What is 5 plus 13 plus 6?",      
    "What is 3 plus 2 multiplied by 3?"
]

for problem in problems:
    print(f"{problem} -> {evaluateSimpleMath(problem)}")
#-----------------------------------------------------------------------------------------------#
# Problem 4
'''
For this exercise, you need to know two things about them:

Each resistor has a resistance value. Resistors are small - so small in fact that 
if you printed the resistance value on them, it would be hard to read. 
To get around this problem, manufacturers print color-coded bands onto the resistors 
to denote their resistance values. Each band has a position and a numeric value.

The first 2 bands of a resistor have a simple encoding scheme: each color maps 
to a single number. For example, if they printed a brown band (value 1) followed 
by a green band (value 5), it would translate to the number 15.

In this exercise you are going to create a helpful program so that you don't have 
to remember the values of the bands. The program will take color names as input 
and output a two digit number, even if the input is more than two colors!

The band colors are encoded as follows:

1.   Black: 0
2.   Brown: 1
3.   Red: 2
4.   Orange: 3
5.   Yellow: 4
6.   Green: 5
7.   Blue: 6
8.   Violet: 7
9.   Grey: 8
10.  White: 9
From the example above:

brown-green should return 15

brown-green-violet should return 15 too, ignoring the third color
'''
colorEncoded = {
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,
    'green':5,
    'blue':6,
    'violet':7,
    'grey':8,
    'white':9
}

def resVal(colors):
    colorList = colors.split('-')

    dig1 = colorEncoded[colorList[0].lower()]
    dig2 = colorEncoded[colorList[1].lower()]

    return str(dig1) + str(dig2)

print(resVal('brown-green'))
print(resVal('brown-green-violet'))
#-----------------------------------------------------------------------------------------------#
# Problem 5
'''
Your task is to Validate Credit Card Number

Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety 
of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

The task is to check if a given string is valid

Valid credit card number

4539 3195 0343 6467

The first step of the Luhn algorithm is to double every second digit, 
starting from the right. We will be doubling

4_3_ 3_9_ 0_4_ 6_6_

If doubling the number results in a number greater than 9 then subtract 9 from the product. 
The results of our doubling:

8569 6195 0383 3437

Then sum all of the digits:

8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80

If the sum is evenly divisible by 10, then the number is valid. This number is valid!
'''

def checkValidity(cardNum):
    cardNum = ''.join([char for char in cardNum if char.isdigit()])
    cardNum = cardNum[::-1]

    totalSum = 0

    for i, digit in enumerate(cardNum):
        n = int(digit)

        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        totalSum += n

    return totalSum % 10 == 0

cardNum = "4539 3195 0343 6467"

if checkValidity(cardNum):
    print(f"{cardNum} is valid.")
else:
    print(f"{cardNum} is invalid")

#-----------------------------------------------------------------------------------------------#
# Problem 6
'''
Write a Python class that has two methods: getString and printString , 
The getString accept a string from the user and printString prints the string in upper case.
'''
class userStr:
    def __init__(self):
        self.strFromUsers = input("Enter any words : ")
    def getStr(self):
        return self.strFromUsers
    def printStr(self):
        print(f"String from user : ", self.strFromUsers)

strInpUser = userStr()
strInpUser.printStr()

# Problem 7
'''
Write a Python class Employee with properties id, name, salary, 
and department and methods like _init_ calculateSalary, assignDepartment and _str_.

Sample Employee Data:

"E7876", "ADAMS", 50000, "ACCOUNTING"
"E7499", "JONES", 45000, "RESEARCH"
"E7900", "MARTIN", 50000, "SALES"
"E7698", "SMITH", 55000, "OPERATIONS"
'''

print("LIST OF EMPLOYEES DETAILS\n")

class Employee:
    def __init__(self, empId, empName, empSalary, empDepartment):
        self.empId = empId
        self.empName = empName
        self.empSalary = empSalary
        self.empDepartment = empDepartment

    def __str__(self):
        return f"Employee Id : {self.empId}\n\
Employee Name : {self.empName}\n\
Employee Salary : RM{self.empSalary:0.2f}\n\
Employee Department : {self.empDepartment}\n"

    def calculateSalary(self, empHoursWorked):
        if empHoursWorked > 50:
            overTime = empHoursWorked - 50
            otAmnt = overTime * (self.empSalary / 50)
            self.empSalary += otAmnt

        return self.empSalary
    
    def assignDepartment(self, empNewDepartment):
        self.empDepartment = empNewDepartment

employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]

# to print list of all employee details
for employee in employees:
    print(employee)

# user option to edit or not
while True:
    userOption = input("\nDo you want to edit the content?\n\
If yes, choose 'S' to edit content for salary and 'D' for department.\n\
If no, choose 'E' to exit.\n\n\
Your choose : ")
    
    if userOption == 'E':
        break 

    elif userOption == 'S':
    # to change salary if employee do overtime
        try:
            empIdNum = input("Enter employee Id to edit employee new salary : ")
            empHoursWorked = int(input("Enter the number of hours worked : "))
            editDone = False
            for employee in employees:
                if employee.empId == empIdNum:
                    oldEmpSalary = employee.empSalary
                    empNewSalary = employee.calculateSalary(empHoursWorked)
                    print(f"The new salary for {employee.empName} [RM{oldEmpSalary:0.2f}] is : RM{empNewSalary:0.2f}")
                    print("\nAfter update content :")
                    print(employee)
                    editDone = True
                    break
            if not editDone:
                print(f"Employee for Id Number : {empIdNum} is not found.\n")
        except:
            print("Invalid input for hours worked. Please make sure its in integer.")

    elif userOption == 'D':
    # to change employee department
        empIdNum = input("Enter employee Id to edit employee new department : ")
        empNewDepartment = input("Enter employee new department : ")
        editDone = False
        for employee in employees:
            if employee.empId == empIdNum:
                oldEmpDepartment = employee.empDepartment
                employee.assignDepartment(empNewDepartment)
                print(f"The new department for {employee.empName} [{oldEmpDepartment}] is : {empNewDepartment}")
                print("\nAfter update content : ")
                print(employee)
                editDone = True
                break
        if not editDone:
            print(f"Employee for Id Number {empIdNum} is not found.\n")

    print("UPDATED EMPLOYEES DETAILS: \n")
    for employee in employees:
        print(employee)

#-----------------------------------------------------------------------------------------------#

# Problem 8
'''
Write a Python class Inventory with attributes like id, productName, 
availableQuantity and price. Add methods like addItem, updateItem, and checkItem_details.

Use a dictionary to store the item details, where the key is the id and the value is a dictionary 
containing the productName, availableQuantity and price.

Sample Data:
{
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}
'''
class Inventory:
    def __init__(self):
        self.items = {}

    def addItem(self, prodId, prodName, prodAvailQtt, prodPrice):
        if prodId in self.items:
            print(f"Items with ID[{prodId}]already exists.")
        self.items[prodId] = {
            "name":{prodName},
            "availQtt":{prodAvailQtt},
            "price":{prodPrice}
        }
        print(f"Item with ID[{prodId}] added successfully.")

    def updateItem(self, prodId, prodName=None, prodAvailQtt=None, prodPrice=None):
        if prodId in self.items:
            if prodName is not None:
                self.items[prodId]["name"] = prodName
            if prodAvailQtt is not None:
                self.items[prodId]["availQtt"] = prodAvailQtt
            if prodPrice is not None:
                self.items[prodId]["price"] = prodPrice
            print(f"Items with ID[{prodId}]")
        else:
            print(f"Item with ID[{prodId}] does not exist.")

    def checkItem_Details(self, prodId):
        if prodId in self.items:
            return self.items[prodId]
        else:
            return f"Item with ID[{prodId}] does not exist."

inventory = Inventory()
inventory.addItem("97410", "Television", 20, 1499.55)
inventory.addItem("97411", "Radio", 32, 654.25)

inventory.updateItem("97411", prodAvailQtt=30, prodPrice=620.00)

print(inventory.checkItem_Details("97411"))

#-----------------------------------------------------------------------------------------------#
# Problem 9
'''
Write a Python class BankAccount with attributes like accountNumber, openingBalance, currentBalance, 
dateOfOpening and customerName. 
Add methods like deposit, withdraw, and checkBalance.
'''
class BankAccount:
    def __init__(self, accountNumber, customerName, openingBalance, currentBalance, dateOfOpening):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.openingBalance = openingBalance
        self.currentBalance = currentBalance
        self.dateOfOpening = dateOfOpening

    def __str__(self):
        print(f"Customer Account Number : {self.accountNumber}\n\
Customer Name : {self.customerName}\n\
Date of Opening : {self.openingBalance}\n\n\
Current Balance : RM{self.currentBalance}")

    def deposit(self, depoAmount):
        if depoAmount > 0:
            self.currentBalance += depoAmount
            print(f"RM{depoAmount} is successfully deposited into your account.\n\
Current Balance :\n\
RM{self.currentBalance}\n")
        else:
            print(f"Current Balance : RM{self.currentBalance}")

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= self.currentBalance:
            self.currentBalance -= withdrawAmount
            print(f"RM{withdrawAmount} withdrew from account.\n\
Current Balance :\n\
RM{self.currentBalance}")
        else:
            print("Insufficient Balance.")
        
    def checkBalance(self):
        return self.currentBalance
    
custBankInfo = BankAccount("10115-1011-05-27850", "Siti Mahirah", "2018-20-03", 2500)
custBankInfo.deposit(1300)
custBankInfo.withdraw(800)
print(custBankInfo.checkBalance())

#-----------------------------------------------------------------------------------------------#
# Problem 10
'''
Write a Python class to check the validity of a string of parentheses,

'(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order, for example

"()" and "()[]{}" are valid
"[)", "({[)]" and "{{{" are invalid.
'''

class ParenthesesValidator():
    def __init__(self):
        selfPair = {
            "(":")",
            "{":"}",
            "[":"]"
        }

    def validity(self, s:str) -> bool:
        stack =eval('[]')

        for char in s:
            if char in self.pair.values():
                eval('stack.append(char)')
            elif char in self.pair.keys():
                if not stack or stack[-1] != self.pair[char]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0
    
    validator = ParenthesesValidator()
    print(validator.validity("()"))     # T
    print(validator.validity("()[]{}")) # T
    print(validator.validity("(]"))     # F
    print(validator.validity("([)]"))   # F
    print(validator.validity("{[]}"))   # T
    print(validator.validity("{{{"))    # F
            
    


    


