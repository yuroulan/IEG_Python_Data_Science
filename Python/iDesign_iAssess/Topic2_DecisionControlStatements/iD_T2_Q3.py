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
