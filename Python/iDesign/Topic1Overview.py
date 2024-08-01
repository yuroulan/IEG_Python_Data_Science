# Question 1

''' Welcome Message
"Pine Tree" is a recently launched startup Event Management company. The company gained a good reputation within a short span because of its highly reliable service delivery.

Nikhil, the founder of this company wished to take the company’s services to the next step and decided to design an Event Management System that would let its Customers plan and host events seamlessly via an online platform. As a part of this requirement, Nikhil wanted to write a piece of code for his company’s Amphi Event Management System that will welcome all the Customers who are using it. Help Nikhil on the task.

Output Format:
Output should display "Welcome to Amphi Event Management System".
Refer sample output for formatting specifications.

Sample Output:
Welcome to Amphi Event Management System '''

print("Welcome to Amphi Event Management System")

#-------------------------------------------------------------------#

# Question 2

''' Customized Welcome Message
Nikhil, the founder of “Pine Tree” company wished to design an Event Management System that would let its Customers plan and host events seamlessly via an online platform.

As a part of this requirement, Nikhil wanted to write a piece of code for his company’s Amphi Event Management System that will display customized welcome messages by taking Customers’ name as input. Help Nikhil on the task.

Input Format:
First line of the input is a string that corresponds to a Customer’s name. Assume that the maximum length of the string is 50.

Output Format:
Output should display the welcome message along with the Customer’s name.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output:
Enter your name
Beena
Hello Beena ! Welcome to Amphi Event Management System '''

name = str(input("Enter your name"))
print(f"Hello {name:.50}! Welcome to Amphi Event Management System")

#-------------------------------------------------------------------#

# Question 3

''' Total Expenses for the Event
 
The prime functionality of an Event Management System is budgeting. An Event Management System should estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event. Nikhil, the founder of "Pine Tree" wanted to include this functionality in his company’s Amphi Event Management System and requested your help in writing a program for the same.

The program should get the branding expenses, travel expenses, food expenses and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses.

Input Format:
First input is a int value that corresponds to the branding expenses.
Second input is a int value that corresponds to the travel expenses.
Third input is a int value that corresponds to the food expenses.
Fourth input is a int value that corresponds to the logistics expenses.

Output Format:
First line of the output should display the float value that corresponds to the total expenses for the Event.
Next four lines should display the percentage rate of each of the expenses.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output:
Enter branding expenses
20000
Enter travel expenses
40000
Enter food expenses
15000
Enter logistics expenses
25000
Total expenses : Rs.100000.00
Branding expenses percentage : 20.00%
Travel expenses percentage : 40.00%
Food expenses percentage : 15.00%
Logistics expenses percentage : 25.00% '''

BrandExp = int(input("Enter branding expenses"))
TravExp = int(input("Enter travel expenses"))
FoodExp = int(input("Enter food expenses"))
LogExp = int(input("Enter logistics expenses"))

TotExp = BrandExp + TravExp + FoodExp + LogExp

print(f"Total expenses : Rs.{TotExp:.2f}")

# percentages

BrandExpPer = ( BrandExp / TotExp ) * 100
print(f"Branding expenses percentage : {BrandExpPer:.2f}%")

TravExpPer = (TravExp / TotExp ) * 100
print(f"Travel expenses percentage : {TravExpPer:.2f}%")

FoodExpPer = ( FoodExp / TotExp ) * 100
print(f"Food expenses percentage : {FoodExpPer:.2f}%")

LogExpPer = ( LogExp / TotExp ) * 100
print(f"Logistics expenses percentage : {LogExpPer:.2f}%")

#-------------------------------------------------------------------#

# Question 4

'''Tickets sold for Charity Event
HelpIndia, a famous NGO has been selective in identifying events to raise funds for charity. Suzanne is a volunteer from the NGO who was selling tickets to the public for the charity event. She sold 'X' more adult tickets than children tickets and she sold twice as many senior tickets as children tickets. Assume that an adult ticket costs $5, children ticket costs $2 and senior ticket costs $3.
Suzanne made 'Y' dollars from ticket sales. Find the number of adult tickets, children tickets, and senior tickets sold.
 
Input Format:
The first input is an integer value X that corresponds to the number of adult tickets more than children tickets.
The second input is an integer value Y that corresponds to the money in dollars made by Suzanne from ticket sales.

Output Format:
The first line of the output should display the number of children tickets sold.
The second line of the output should display the number of adult tickets sold.
The third line of the output should display the number of senior tickets sold.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output :
Enter the value of X
10
Enter the value of Y
700
Number of children tickets sold : 50
Number of adult tickets sold : 60
Number of senior tickets sold : 100 '''

# She sold 'X' more adult tickets than children tickets and 
# she sold twice as many senior tickets as children tickets.
# Assume that an adult ticket costs $5, 
# children ticket costs $2 and 
# senior ticket costs $3.
# Suzanne made 'Y' dollars from ticket sales. 

xVal = int(input("Enter the value of X"))
yVal = int(input("Enter the value of Y"))

# a = c + X
# s = 2c
# Y = 5a +2c+3s

children = int((yVal - (5 * xVal)) / 13)
adult = int(children + xVal)
senior = int(2 * children)

print(f"Number of children tickets sold : {children}")
print(f"Number of adult tickets sold : {adult}")
print(f"Number of senior tickets sold : {senior}")

#-------------------------------------------------------------------#

# Question 5

''' Tile Game
In connection to the National Mathematics Day celebration, the Regional Mathematical Scholars Society had arranged for a Mathematics Challenge Event where school kids participated in large number. Many interesting math games were conducted, one such game that attracted most kids was the tile game where the kids were given 'n' square tiles of the same size and were asked to form the largest possible square using those tiles.

Help the kids by writing a program to find the area of the largest possible square that can be formed, given the side of a square tile (in cms) and the number of square tiles available.

Input Format:
First line of the input is an integer that corresponds to the side of a square tile (in cms).
Second line of the input is an integer that corresponds to the number of square tiles available.

Output Format:
Output should display the area of the largest possible square that can be formed (in square cms) with the available tiles.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output :
Enter the side in cm of a square tile
5
Enter the number of square tiles available
8
Area of the largest possible square is 100sqcm '''

# to know the largest possible square using tiles given
# let say sides of tile is 5cm 
# when tiles has 4, the sides is 5 + 5 = 10cm
# 10 cm (vertical) , 10cm (horizontal)

sideSqr = int(input("Enter the side in cm of a square tile"))   # 5cm
numTiles = int(input("Enter the number of square tiles available"))  # 8 tiles
sqrt = int(numTiles  ** (1/2))

sides = int((sideSqr * sqrt) ** 2)

print(f"Area of the largest possible square is {sides} sqcm")

#-------------------------------------------------------------------#

# Question 6

''' Wisconsin State Fair is one of the largest midsummer celebrations in the Midwest Allis, showcasing the agriculture skills and prowess of the state. The Event organizers hired few part-time employees to work at the fair and the agreed salary paid to them are as given below:

Weekdays --- 80 / hour
Weekends --- 50 / hour

Justin is a part-time employee working at the fair. Number of hours Justin has worked in the weekdays is 10 more than the number of hours he had worked during weekends. If the total salary paid to him in this month is known, write a program to estimate the number of hours he had worked during weekdays and the number of hours he had worked during weekends.

Input Format:
First line of the input is a double value that corresponds to the total salary paid to Justin.

Output Format:
First line of the output should display the number of hours Justin has worked during the weekdays.
Second line of the output should display the number of hours Justin has worked during the weekends.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output:
Enter the total salary paid
2750
Number of weekday hours is 25
Number of weekend hours is 15 '''

# part time employee

# Weekdays --- 80 / hour , X
# Weekends --- 50 / hour , Y

# no of hour justin work in weekdays is 10 more
# than the number of hour he working in weekends

# weekdays = 10 + weekends  -->> X
# Ts = (known) = 80 (Y) + 50 (X) -->> Total Salary
# Ts = 80Y + 50(10+Y)

Ts = int(input("Enter the total salary paid"))

Y = int((Ts - 800) / 130)
X = int(10 + Y)

print(f"Number of weekday hours is {X}")
print(f"Number of weekend hours is {Y}")

#-------------------------------------------------------------------#

# Question 7

''' Command Line Argument- Count
Write a program to accept strings as command line argument and print the number of arguments entered.

Sample Input (Command Line Argument) 1:
Command Arguments

Sample Output 1:
Arguments :
Command
Arguments
Number of arguments is 2

Sample Input (Command Line Argument) 1:
Commands

Sample Output 2:
Arguments :
Commands
Number of arguments is 1 '''

import sys

# arguments = ["Command" , "Arguments"]

print("Arguments :")

for argument in sys.argv[1:]:
    print(argument)
    
print("Number of arguments is", len(sys.argv) - 1)   

#-------------------------------------------------------------------#

# iassess

'''
WonderWorks Magic Show
The Magic Castle, the home of the Academy of Magical Arts at California has organized the great ‘WonderWorks Magic Show’. 3 renowned magicians were invited to mystify and thrill the crowd with their world’s spectacular magic tricks. At the end of each of the 3 magicians’ shows, the audience were requested to give their feedback in a scale of 1 to 10. Number of people who watched each show and the average feedback rating of each show is known. Write a program to find the average feedback rating of the WonderWorks Magic show.

Input Format:
First line of the input is an integer value that corresponds to the number of people who watched show 1.
Second line of the input is a float value that corresponds to the average rating of show 1.
Third line of the input is an integer value that corresponds to the number of people who watched show 2.
Fourth line of the input is a float value that corresponds to the average rating of show 2.
Fifth line of the input is an integer value that corresponds to the number of people who watched show 3.
Sixth line of the input is a float value that corresponds to the average rating of show 3.

Output Format:
Output should display the overall average rating for the show. Display the rating correct to 2 decimal places.
Refer sample input and output for formatting specifications.
'''

show1 = int(input("Enter the number of people who watched show 1"))
avg1 = float(input("Enter the average rating for show 1"))
show2 = int(input("Enter the number of people who watched show 2"))
avg2 = float(input("Enter the average rating for show 2"))
show3 = int(input("Enter the number of people who watched show 3"))
avg3 = float(input("Enter the average rating for show 3"))

totAvg1 = show1 * avg1
totAvg2 = show2 * avg2
totAvg3 = show3 * avg3

AllAvgTot = totAvg1 + totAvg2 + totAvg3

print("The overall average rating for the show is {AllAvgTot:0.2f}")
