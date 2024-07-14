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