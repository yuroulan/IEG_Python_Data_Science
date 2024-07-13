#Problem 5

'''
Team Event
Super Quiz Bee is a famous quiz Competition that tests students on a wide variety of academic subjects. This week’s competition was a Team event and students who register for the event will be given a unique registration code N. The participants are teamed into 10 teams and the team to which a participant is assigned to depends on the absolute difference between the first and last digit in the registration code.

The event organizers wanted your help in writing an automated program that will ease their job of assigning teams to the participants. If the registration number given is less than 10, then the program should display "Invalid Input".

Input Format:
The only line of input contains an integer N.

Output Format:
Output the absolute difference between the first and last digit of N.
Refer sample input and output for formatting specifications.

Sample Input 1:
345

Sample Output 1:
2

Sample Input 2:
9

Sample Output 2:
Invalid Input
'''
N = input()
Nlist = list(N)
#print(Nlist)

firstDig = int(Nlist[0])
# firstInt = int(firstDig)
#print(firstDig)

secDig = int(Nlist[-1])
#print(secDig)

if int(N) >= 10:
    diff = firstDig - secDig
    print(abs(diff))
else:
    print("Invalid input")