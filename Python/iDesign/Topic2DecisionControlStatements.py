# Problem 1
'''
Lucky Winner
It was the inaugural ceremony of "Fantasy Kingdom" Amusement park and the park Management has announced some lucky prizes for the visitors on the first day. Based on this, the visitors whose ticket number has the last digit as 3 or 8, are declared as lucky winners and attracting prizes are awaiting to be presented for them.
Write a program to find if the last digit of the ticket number of visitors is 3 or 8.

 
Input Format:
First line of the input is an integer that corresponds to the ticket number.

Output Format:
Output should display as "Lucky Winner" if the last digit of the ticket number is 3 or 8. Otherwise print "Not a Lucky Winner".
Refer sample input and output for formatting specifications.

Sample Input 1:
43

Sample Output 1:
Lucky Winner

Sample Input 2:
41

Sample Output 2:
Not a Lucky Winner
'''

# visitors lucky tickets end with digit 3 or 8
# to find the last digit of ticket is 3 or 8

tickNum = int(input())
tickNum %= 10

if(tickNum == 3 or tickNum == 8):
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")

#-------------------------------------------------------------------#

# Problem 2
'''
Ticket Types
The Magic Castle, the home of the Academy of Magical Arts at California has organized the great 'WonderWorks Magic Show'. Renowned magicians were invited to mystify and thrill the crowd with their world’s spectacular magic tricks. The Ticket booking for the show started 2 days prior and there were different types of tickets offered with different fare. The show organizers wanted to place a scanning machine at the entrance of the venue for scrutiny. The machine will take the input of a character denoting the various ticket types and displays the equivalent ticket type of the given character.

There are 5 types of tickets, each of which is denoted by a character (both upper case and lower case). Please find the equivalent strings for the characters.
E or e - Early Bird Ticket
D or d - Discount Ticket
V or v - VIP Ticket
S or s - Standard Ticket
C or c - Child Ticket
Write a piece of code for the scanning machine that will take the input of a character and print the equivalent string as given.

Note:
Refer to problem specifications.

Input Format:
The first line of the input is one of the character that denotes one of ticket types.

Output Format:
Output should display the equivalent ticket type of the character.
Refer sample input and output for formatting specifications.

Sample Input 1:
e

Sample Output 1:
Early Bird Ticket

Sample Input 2:
S

Sample Output 2:
Standard Ticket
'''

firstChar = input()

if(firstChar == 'E' or firstChar == 'e'):
    print("Early Bird Ticket")
elif(firstChar == 'D' or firstChar == 'd'):
    print("Discount Ticket")
elif(firstChar == 'V' or firstChar == 'v'):
    print("VIP Ticket")
elif(firstChar == 'S' or firstChar == 's'):
    print("Standard Ticket")
else:
    print("Child Ticket")

#-------------------------------------------------------------------#

# Problem 3

'''

Total Expenses
The much awaited event at the entertainment industry every year is the "Screen Awards". This year the event is going to be organized on December 25 to honour the Artists for their professional excellence in Cinema. The Organizers has this time decided to launch an online portal to facilitate easy booking of the Award show’s tickets.

They specifically wanted to provide an option for bulk booking in the portal, wherein there are many discounts announced. Write a program to help the Organizers to create the portal as per the requirement given below.
Given the ticket cost as 'X'.
If the number of tickets purchased is less than 50, there is no discount.
If the number of tickets purchased is between 50 and 100 (both inclusive), then 10% discount is offered.
If the number of tickets purchased is between 101 and 200(both inclusive), 20% discount is offered.
If the number of tickets purchased is between 201 and 400(both inclusive), 30% discount is offered.
If the number of tickets purchased is between 401 and 500(both inclusive), 40% discount is offered.
If the number of tickets purchased is greater than 500, then 50% discount is offered.

Input Format:
First line of the input is an integer that corresponds to the cost of the ticket ‘X’.
Second line of the input is an integer that corresponds to the number of tickets purchased.

Output Format:
Output should display a double value, which gives the total expenses in purchasing the tickets after discounts. Display the output correct to 2 decimal places.
Refer sample input and output for formatting specifications.

Sample Input 1:
100
5

Sample Output 1:
500.00

Sample Input 2:
100
300

Sample Output 2:
21000.00
'''

tickPrice = int(input())    # ist
tickQuantitiy = int(input())    # 2nd

noDisc = tickPrice * tickQuantitiy

if(tickQuantitiy > 500):
    disc = 50 / 100 * tickPrice
    aftDisc = tickPrice - disc
    total = aftDisc * tickQuantitiy
    print(f"{total:0.2f}")
elif(tickQuantitiy >= 401 and tickQuantitiy <= 500):
    disc = 40 / 100 * tickPrice
    aftDisc = tickPrice - disc
    total = aftDisc * tickQuantitiy
    print(f"{total:0.2f}")
elif(tickQuantitiy >= 201 and tickQuantitiy <= 400):
    disc = 30 / 100 * tickPrice
    aftDisc = tickPrice - disc
    total = aftDisc * tickQuantitiy
    print(f"{total:0.2f}")
elif(tickQuantitiy >= 101 and tickQuantitiy <= 200):
    disc = 20 / 100 * tickPrice
    aftDisc = tickPrice - disc
    total = aftDisc * tickQuantitiy
    print(f"{total:0.2f}")
elif(tickQuantitiy >= 50 and tickQuantitiy <= 100):
    disc = 10 / 100 * tickPrice
    aftDisc = tickPrice - disc
    total = aftDisc * tickQuantitiy
    print(f"{total:0.2f}")
else:
    print(f"{noDisc:0.2f}")

#-------------------------------------------------------------------#

# Problem 4
'''
Salary Computation
Danny has recently got his job offer as an Event Concept Creator at Sparsh Event Services. The Company has sent him a detailed salary structure with details of his basic salary, HRA and DA. The Company has promised to pay him as under:

If his basic salary is less than Rs. 15000, then HRA = 15% of basic salary and DA = 90% of basic salary.
If his basic salary is either equal to or above Rs. 15000, then HRA = Rs. 5000 and DA = 98% of basic salary.

If the Danny’s salary is given as input, write a program to find his gross salary.

Note : Gross Salary = Basic Salary+HRA+DA
 
Input Format:
First line of the input is an integer that corresponds to the basic salary of Danny.

Output Format:
Output should display the double value that refers to the gross salary of Danny. Display the output correct to 2 decimal places.
Refer sample input and output for formatting specifications.

Sample Input 1:
12000

Sample Output 1:
24600.00

Sample Input 2:
30000

Sample Output 2:
64400.00
'''

basSal = int(input())

if(basSal < 15000):
    HRA = 15 / 100 * basSal
    DA = 90 / 100 * basSal
    grossSal = basSal + HRA + DA
    print(f"{grossSal:0.2f}")
elif(basSal >= 15000):
    HRA = 5000
    DA = 98 / 100 * basSal
    grossSal = basSal + HRA + DA
    print(f"{grossSal:0.2f}")
else:
    print()

# Problem 5

'''
Grades of Rides
“AquaticaCarnival” is the most successful event dedicated to children and families. The Event has more than 20 rides for children and adults and the organizers always ensure not to compromise on the safety of the visitors.
To ensure the safety of the rides, the organizers have graded the rides in the fair according to the following conditions:
Hurl Factor must be greater than 50.
Spin Factor must be greater than 60.
Speed factor must be greater than 100.

The grades are as follows:
Grade is 10 if all three conditions are met.
Grade is 9 if conditions (i) and (ii) are met.
Grade is 8 if conditions (ii) and (iii) are met.
Grade is 7 if conditions (i) and (iii) are met.
Garde is 6 if only one condition is met.
Grade is 5 if none of three conditions are met.
Write a program display the grade of the rides, given the values of hurl factor, spin factor and speed factor of the ride under consideration.

Input Format:
First line of the input consists of 3 integers that gives the Hurl Factor, Spin Factor and Speed Factor of the ride, each separated by a space.

Output Format:
Output should display the grade of the ride depending on Conditions.
Refer sample input and output for formatting specifications.

Sample Input 1:
51 89 150

Sample Output 1:
10

Sample Input 2:
45 69 102

Sample Output 2:
8
'''
factors = input()

factors = factors.split(" ")

strFact = []                           # str to int
for factor in factors:
    strFact.append(int(factor))

HF = strFact[0] > 50
SF = strFact[1] > 60
SPF = strFact[2] > 100

if(HF and SF and SPF):
    print("10")
elif(HF and SF):
    print("9")
elif(SF and SPF):
    print("8")
elif(HF and SPF):
    print("7")
elif(HF or SF or SPF):
    print("6")
else:
    print("5")

# iassess
'''
Card Game
The Westland Game Fair is the premier event of its kind for kids interested in some intellectual and cognitive brain games. Alan, a middle school boy is visiting the fair where he is very much drawn by the Card game.

The game’s rules are:
A player needs to pick 3 cards from a big lot of cards. There are 4 types of Cards namely Spade(S), Heart(H), Club(C) and Diamond (D). If all the 3 cards that the player picks are of the same type and same number, they get a Double Bonanza. If all the 3 cards are of the same type or if they all have the same number, they get a Bonanza. Otherwise they do not get a Bonanza. Alan has now picked 3 cards and is awaiting to know if he has got a bonanza. Please help him to know if he has won the Bonanza or not.

Input Format:
There are 3 lines of input.
Each of the line consists of character and integer input, which corresponds to the type of the card and the number in it that Alan picked. The type of card and the number are separated by a single space.

Output Format:
Output should display "Double Bonanza" or "Bonanza" or "No Bonanza" based on the conditions given.
Refer sample input and output for formatting specifications.

Sample Input 1:
S 5
S 5
S 5

Sample Output 1:
Double Bonanza

Sample Input 2:
S 6
S 5
H 5

Sample Output 2:
No Bonanza
'''

cards1 = input()
cards2 = input()
cards3 = input()

cards1 = cards1.split(" ")
cards2 = cards2.split(" ")
cards3 = cards3.split(" ")

# types of card (S, H, C, D)

type1, num1 = cards1[0] , cards1[1]
type2, num2 = cards2[0] , cards2[1]
type3, num3 = cards3[0] , cards3[1]

if(type1 and type2 and type3):
    print("Double Bonanza")
elif(type1 or type2 or type3):
    print("Bonanza")
else:
    print("No Bonanza")


