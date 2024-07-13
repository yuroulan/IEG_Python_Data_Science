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
