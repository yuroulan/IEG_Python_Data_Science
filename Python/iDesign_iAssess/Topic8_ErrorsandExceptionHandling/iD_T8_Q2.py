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