# Problem 4
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