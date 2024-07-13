# Problem 1
'''
Write a Python program that accepts two numbers as input (say x and y) and finds x/y.

When the denominator is 0, the program should raise a ZeroDivisionError Exception and print the message shown in the sample output.

 

Input Format:

Input consists of 2 integers

 

Output Format:

Output is either the result or the error message.

Refer sample output.

[All text in bold corresponds to input and the rest corresponds to output]

 

Sample Input and Output 1:

Enter number 1

6

Enter number 2

3

2.0

 

Sample Input and Output 2:

Enter number 1

5

Enter number 2

0

Divide By Zero Error
'''
def divide():
    try:
        x =int( input("Enter number 1"))
        y = int(input("Enter number 2"))
        
        div = x / y
        print(div)
        
    except ZeroDivisionError:
        print("Divide By Zero Error")

divide()

# Problem 2
'''
# def divide():
try:
    x = (input("Enter number 1\n"))
    y = (input("Enter number 2\n"))
    
    div = int(x) / int(y)
    print(div)
        
except ZeroDivisionError:
    print("Divide By Zero Error")

except ValueError:
    print("Invalid Value")
        
# divide()
'''
class NotEligibleException(Exception):
    pass

class Student:
    def __init__(self, marks):
        self.marks = marks

    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")

try:
    marks = int(input("Enter marks of student\n"))
    s = Student(marks)

    if s.check_marks() == True:
        print("Eligible")
except NotEligibleException as e:
    print("Inside Except Block :", e)

# Problem 3
'''
P5 / Custom Exception

Create a class named Student with a single attribute – marks.

Include a method named check_marks in the Student Class.

This method checks whether the marks is greater than  or equal to 90 and if it is greater than or equal to 90, the method returns True.

If the marks is less than 90, a custom Exception named NotEligibleException is raised and an appropriate message as shown in the sample output is displayed.

 

Create a custom Exception class named NotEligibleException.

 

Create an object of the student class and test the above methods.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

 

Sample Input and Output 1:

Enter marks of student

98

Eligible

 

Sample Input and Output 2:

Enter marks of student

56

Inside Except Block : Not Eligible
'''
class NotEligibleException(Exception):
    pass

class Student:
    def __init__(self, marks):
        self.marks = marks

    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")

try:
    marks = int(input("Enter marks of student\n"))
    s = Student(marks)

    if s.check_marks() == True:
        print("Eligible")
except NotEligibleException as e:
    print("Inside Except Block :", e)

# Problem 4
'''
Write a program that prompts users to enter numbers till he enters one positive number. Whenever the user enters a negative number or a string , raise a ValueError exception and handle it appropriately and display the message shown in the sample output.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

 

Sample Input and Output 1:

Enter a positive integer

5

Good! You entered 5

 

Sample Input and Output 2:

Enter a positive integer

-6

You entered a negative number. Retry!

Enter a positive integer

-9

You entered a negative number. Retry!

Enter a positive integer

3

Good! You entered 3
'''
def getPositiveInt():

    while True:
        try:
            posInt = (input("Enter a positive integer\n"))

            num = int(posInt)

            if num <= 0:
                raise ValueError("You entered a negative number. Retry!")
            else:
                print(f"Good! You entered {num}")
                break

        except ValueError as e:
            print(e)
            print("")


getPositiveInt()

# Problem 5
'''
Type Error Exception
Saurav is coach of ABC school cricket team. His team captain not performing well from last few matches. So, coach wants to find the batting average of his captain.
Thus, write a program to find the batting average of his captain, for given 'n' matches.

This program may generate Type Error exception, if there is a type mismatch when rating is got as input. Use exception handling mechanisms to handle this exception. 
  
Input and Output Format: 
Refer sample input and output for formatting specifications.
Batting average should be rounded off to two decimal places.

Note: All text in bold corresponds to input and the rest corresponds to output. 
  
Sample Input and Output 1: 
Enter the number of matches
4 
Enter the scores
34
12
24
20
Batting average: 22.50

Sample Input and Output 2: 
Enter the number of matches
2 
Enter the scores
10
r 
Type Error Exception
'''
try:
    matchesNum = int(input("Enter the number of matches\n"))  
    
    print("Enter the scores")
    scores = []
    for _ in range(matchesNum):
        score = input()
        scores.append(int(score))

    totRuns = sum(scores)
    battAvg = totRuns / matchesNum

    print(f"Batting average: {battAvg:.2f}")  

except ValueError:
    print("Type Error Exception")
except TypeError:
    print("Type Error Exception: Invalid type conversion")
except Exception as e:
    print(e)

# Problem 6
'''
Invalid age exception
 
A vote is a formal expression of an individual's choice in voting. Government elected by its citizens, and voting is an important right in our society. Log sabha election in Delhi held in October 2016. And as we know that voting age 18, is a minimum age established by law that a person must attain before they become eligible to vote.
Thus, write a program to get the name and age of the people who all are eligible for voting.

Note:
If people is eligible to vote only after 18 and above.

This program may generate:
1. InvalidAgeRange Custom Exception when the People's age is below 18
 Use exception handling mechanisms to handle these exceptions

Create a class called CustomException which extends Exception and it includes constructor to initialize the message.
Use appropriate exception handling mechanisms to handle these exceptions  

Input and Output Format:
Refer sample input and output for formatting specifications.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample  Input/Output 1:
Enter the Name
naveen
Enter the age
25
Voter name: naveen
Voter age: 25

Sample  Input/Output 2:
Enter the Name
shilpa
Enter the age
12
CustomException: InvalidAgeRangeException
'''
# i assess
# 1
'''
Area (Polymorphism)
                                                    
Create a base Class Shape and derive the CalAreaSquare, CalAreaRectangle, CalAreaTriangle, CalAreaCircle classes.

Use the following method in base class Shape:
Method Name            Description
area()                          Display the input parmaters

Calculate area of square in all the derived classes:
Method Name            Description
area()                                       Find the area of the Square, Rectangle, Triganle and Circle, in their respective derived classes.

Note: The area of triangle=0.5*base*height
pi value will be considered as 3.14

Sample Input and Output Format 1:
Select an Option
1.Square
2.Rectangle
3.Triangle
4.Circle
4
Enter the radius
2
Radius of Circle : 2
Area of Circle : 12.57
'''
class Shape:
    def area(self):
        pass

class CalAreaSqr(Shape):
    def area(self, side):
        self.side = side
        print(f"Side of Square : {self.side}")
        print(f"Area of Square : {self.side * self.side:.2f}") 

class CalAreaRect(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
        print(f"Area of Rectangle : {self.length * self.width}")

class CalAreaTri(Shape):
    def area(self, base, height):
        self.base = base
        self.height = height
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        print(f"Area of Triangle : {0.5 * self.base * self.height:.2f}")

class CalAreaCircle(Shape):
    def area(self, radius):
        self.radius = radius
        print(f"Radius of Circle : {self.radius}")
        print(f"Area of Circle : {3.14 * self.radius * self.radius:.2f}")

# Main program
print("Select an Option")
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")

option = int(input())

if option == 1:
    side = int(input("Enter the side length"))
    square = CalAreaSqr()
    square.area(side)
elif option == 2:
    length = int(input("Enter the length"))
    width = int(input("Enter the breadth"))
    rectangle = CalAreaRect()
    rectangle.area(length, width)
elif option == 3:
    base = int(input("Enter the base"))
    height = int(input("Enter the height"))
    triangle = CalAreaTri()
    triangle.area(base, height)
elif option == 4:
    radius = int(input("Enter the radius"))
    circle = CalAreaCircle()
    circle.area(radius)
else:
    print("Invalid Option")

# 2
'''
Student-Feedback(single Inheritance)

[Note :
Strictly adhere to the object oriented specifications given as a part of the problem statement.
Use the same class names and member variable names. ]

Create a base class named Student with the following  member variables / attributes  .



Data Type	Variable Name
Integer	id
String	name
String	department
Integer	courseId

Include a 4-argument constructor. The order of parameters passed to the constructor is id,name,department,courseId.
Override a str() method to display the details of the class.

Create a child class named StudentRating with the following  member variables / attributes  .



Data Type	Variable Name
Integer	id
String	review
Integer	stars
Student	student

Include a 4-argument constructor. The order of parameters passed to the constructor is id,review, stars, student(inherited from Student class.
Override a str() method to display the details of the class.

Input and Output Format:  
Refer sample input and output for formatting specifications.  
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
Enter the student id
12
Enter the student name
Prakash
Enter the department
ECE
Enter the course id
250
Enter the Rating id
4
Enter review
Very good Student!!!
Enter number of stars
5
Student :
Id :  12
Name :  Prakash
Department :  ECE
Course Id :  250
Rating ID :  4
Review :  Very good Student!!!
Rating Stars :  5
'''
class Student:
    def __init__(self, id, name, department, courseId):
        self.id = id
        self.name = name
        self.department = department
        self.courseId = courseId

    def __str__(self):
        return (f"Student :\n"
                f"Id :  {self.id}\n"
                f"Name :  {self.name}\n"
                f"Department :  {self.department}\n"
                f"Course Id :  {self.courseId}")

class StudentRating:
    def __init__(self, id, review, stars, student):
        self.id = id
        self.review = review
        self.stars = stars
        self.student = student

    def __str__(self):
        return (f"{self.student}\n"
                f"Rating ID :  {self.id}\n"
                f"Review :  {self.review}\n"
                f"Rating Stars :  {self.stars}")

# Main Program
print("Enter the student id")
student_id = int(input())
print("Enter the student name")
student_name = input()
print("Enter the department")
student_department = input()
print("Enter the course id")
student_courseId = int(input())

student = Student(student_id, student_name, student_department, student_courseId)

print("Enter the Rating id")
rating_id = int(input())
print("Enter review")
rating_review = input()
print("Enter number of stars")
rating_stars = int(input())

student_rating = StudentRating(rating_id, rating_review, rating_stars, student)

print(student_rating)
   
# iasses
# 1
'''
P4 / Index Error

An input list is given in the code template.

Write a program to find the sum of first n values from the given list.

For invalid ‘n’ values, raise an IndexError Exception and display the message shown in the sample output.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

 

Sample Input and Output 1:

[2, 3, 1, 5, 6, 7, 1]

Enter n

5

Sum = 17

 

Sample Input and Output 2:

[2, 3, 1, 5, 6, 7, 1]

Enter n

10

Index Value out of range

'''
numlist = [2,3,1,5,6,7,1]
print(numlist)

n = int(input("Enter n\n"))

try:
    sum = 0
    for i in range(n):
        sum += numlist[i]
    print("Sum =", sum)

except IndexError:
    print("Index Value out of range")

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
