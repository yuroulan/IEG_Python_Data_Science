# 2
'''
CustomException: Invalid Password Exception
Vicky's father wants to create the whatsApp account. But again and again Invalid Password error comes. So Vicky helps his father to create a account. During account creation he has enter the username and password, in which the password should be contain atleast one lowercase letter, one upper case letter and a number, otherwise exception occured.
So write a program to check the password is valid or invalid.

Note:
Conditions for a valid password: 
Password should contain atleast one lowercase letter, one upper case letter and a number. 
Use exception handling mechanisms to handle these exceptions 
 
Input and Output Format: 
Refer sample input and output for formatting specifications. 
All text in bold corresponds to input and the rest corresponds to output. 

Sample Input and Output 1 : 
Enter the username
Vikram
Enter the password 
1samudrA
Employee Username: Vikram
Password: 1samudrA

Sample Input and Output 2 : 
Enter the username 
Rashmi
Enter the password 
hawai
CustomException: Invalid Password Exception
'''
username = input("Enter the username\n")
password = input("Enter the password\n")

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

lowCase = 0
upperCase = 0
numCase = 0

for i in password:
    if i.islower():
        lowCase += 1
    if i.isupper():
        upperCase += 1
    if i.isdecimal():
        numCase += 1

try:
    if lowCase >= 1 and upperCase >= 1 and numCase >= 1:
        print(f"Employee Username: {username}\nPassword: {password}")
    else:
        raise CustomError("CustomException: Invalid Password Exception")
except CustomError as e:
    print(e)