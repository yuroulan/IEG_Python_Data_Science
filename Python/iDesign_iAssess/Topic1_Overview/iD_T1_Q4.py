# Question 4

'''
Tickets sold for Charity Event
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
Number of senior tickets sold : 100 
'''

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