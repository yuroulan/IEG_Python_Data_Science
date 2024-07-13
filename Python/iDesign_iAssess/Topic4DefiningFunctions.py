# Problem 1
'''
Default arguments using functions
Write a python program to get the name of the user and message and display it using functions.
Function specifications:
def greet(argument1,argument2 = “Welcome to Python Programming”)

Input Format:
Input consists of an string input.
Output Format:
Display the statements along with user input.
Refer to the sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output.]

Sample input and Output 1:
Menu
1. Name and Message
2. Name
1
Enter the name
Jack
Enter the message
How are you
Hello Jack, How are you


Sample input and Output 2:
Menu
1. Name and Message
2. Name
2
Enter the name
Jim
Hello Jim, Welcome to Python Programming
'''
def greet(name, message = "Welcome to Python Programming"):
    print(f"Hello {name}, {message}")

def main():
    print("Menu\n\
1. Name and Message\n\
2. Name")

    userInp = input()
    if userInp == '1':
        print("Enter your name")
        name = input()
        print("Enter the message")
        message = input()
        greet (name, message)
    elif userInp == '2':
        print("Enter the name")
        name = input()
        greet(name)

main()

# Problem 2
'''
Leap year using default arguments
 
Write a program to find leap year using default arguments.

Functional Specifications:
def daysInYear(argument1,argument2=False)

Input Format:

Input consists of a year.


Output Format:
Output prints the whether the given year is leap year or not.

 

Sample Input  and Output:
2000

2000 is a leap year
'''
def leapYearIs(leapYear, resultIs = False):
    if(leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0):
        result = f"{leapYear} is a leap year."
    else:
        result = f"{leapYear} is not a leap year."

    if resultIs:
        print(result)

    return resultIs
    

leapYear = int(input("Put any year : "))
leapYearIs(leapYear, resultIs = True)

# Problem 3
'''

Finding GCD and LCM
Write a program to find the GCD and LCM of two numbers using functions.

Python Function Specification:
def GCD (n1,n2):
def LCM (n1,n2):
Function should return the output.

C Function Specification:
int GCD (n1,n2):
int LCM (n1,n2):
Function should return the output.

INPUT AND OUTPUT FORMAT:
Input consists of two integers corresponding to two values.
Output consists of two integers corresponding to GCD and LCM of the two numbers.

SAMPLE INPUT AND OUTPUT:
Enter two integers:
3
9
Greatest common divisor of 3 and 9 = 3
Least common multiple of 3 and 9 = 9
'''
def GCD (n1,n2):
    if n2 == 0:
        return n1
    else:
        return GCD(n2, n1 %n2)

def LCM (n1,n2):
    return abs(n1 * n2) // GCD(n1, n2)

print("Enter two integers:")
n1 = int(input())
n2 = int(input())

print(f"Greatest common divisor of {n1} and {n2} = {GCD(n1, n2)}")
print(f"Least common multiple of {n1} and {n2} = {LCM(n1, n2)}")

# Problem 3
'''
Simple Calculator

Sita was a mathematics teacher and she had to teach the basic mathematic operations to her students. 
As she was good in programming as well she thought of writing a python program to 
display all the operations in a single program and perform them choice by choice. 
Help her with a  code to perform the operations.

Input and output format:
Input consists of integer 'n' indicating the choice of operation followed by the 
integers to perform the chosen operation. 
The output consists of answer performed according to the choice. 
Refer sample input and output for better understanding.

All the texts in bold indicate input and rest indicate output.

Function Specifications:
def addition(n1,n2):
def subtraction(n1,n2):
def multiplication(n1,n2):
def division(n1,n2):
def modulus(n1,n2):

Sample Input and Output 1:
Select the operation
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
Enter the choice(1/2/3/4/5):
3
Enter the first number
5
Enter the second number
8
5 * 8 = 40
 
Sample Input and Output 2:
Select the operation
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
Enter the choice(1/2/3/4/5):
6
Invalid Input
'''
def addition(n1,n2):
    add = n1 + n2
    return add
def subtraction(n1,n2):
    minus = n1 - n2
    return minus
def multiplication(n1,n2):
    mult = n1 * n2
    return mult
def division(n1,n2):
    div = n1 / n2
    return div
def modulus(n1,n2):
    mod = n1 % n2
    return mod

print("Select the operation:\n\
1.Add\n\
2.Subtract\n\
3.Multiply\n\
4.Divide\n\
5.Modulus")

userInp = int(input("Enter the choice(1/2/3/4/5):"))

if userInp in [1,2,3,4,5]:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))

    if userInp == 1:
        result = addition(n1, n2)
        print(f"{n1} + {n2} = {result}")
    elif userInp == 2:
        result = subtraction(n1, n2)
        print(f"{n1} - {n2} = {result}")
    elif userInp == 3:
        result = multiplication(n1, n2)
        print(f"{n1} * {n2} = {result}")
    elif userInp == 4:
        result = division(n1, n2)
        print(f"{n1} / {n2} = {result}")
    elif userInp == 5:
        result = modulus(n1, n2)
        print(f"{n1} % {n2} = {result}")
else:
        print("Invalid Input")      

# Problem 5
'''
Filter Events 

Write a program to get size of list and its elements and  to find numbers divisible by thirteen from a list using anonymous function (Lambda) and display those numbers.

Input Format:
The first line of input corresponds to the size of list 'n'.
The next 'n' line of input corresponds to the elements in the list .

Output Format:
The output consists of numbers divisible by thirteen separated by space.
Refer sample output for formatting specifications.

Problem Constraints:
n > 0 print the numbers divisible by thirteen separated by space, else display as "Invalid input".

Sample Input/Output 1:
Enter size of list
9
Enter the elements in list
12
65
54
39
102
339
221
50
70
65 39 221

Sample Input/Output 2:
Enter size of list
O
Invalid input
'''
n = int(input("Enter size of list\n"))

if n > 0:
    elements = []
    print("Enter the elements in list")
    for i in range(n):
        elemList = int(input())
        elements.append(elemList)

    x = lambda num: num % 13 == 0
    div = [num for num in elements if x(num)]
    
    if div:
        print(" ".join(map(str, div)))
    else:
        print("No numbers divisible by 13")
else:
    print("Invalid input")