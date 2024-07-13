# Problem 3
'''
Series
The Event Organizing Company "Buzzcraft" focuses event management in a way that creates a win-win situation for all involved stakeholders. Buzzcraft don't look at building one time associations with clients, instead, aim at creating long-lasting collaborations that will span years to come. This goal of the company has helped them evolve and expand big with organizing many events till date.
The number of events that the company organizes every month is recorded sensibly and is seemed to have followed a specific series like: 30, 35, 38, 41, 54, 53 ...

Write a program which takes an integer N as the input and will output the series till the Nth term.

Input Format:
First line of the input is an integer N.

Output Format:
Output a single line the series till Nth term, each separated by a comma.
Refer sample input and output for formatting specifications.

Sample Input 1:
5

Sample Output 1:
30 35 38 41 54

Sample Input 2:
10

Sample Output 2:
30 35 38 41 54 53 78 71 110 95
'''
N = int(input())

# to initialize first value and iteration of each value
num = 0
iter = []  # empty list
oddIter = 0
evenIter = 0
firstNum = 30
secNum = 35

while num < N: # N == kedudukan nombor dalam list ATAU giliran keberapa
    
    if(num % 2 == 0): # 0,2,4,6,8,..
        firstNum = firstNum + oddIter # 
        iter.append(firstNum)
        oddIter = oddIter + 8
    else: 
        # if num % 2 != 0 # 1,3,5,7,9,..
        secNum = secNum + evenIter
        iter.append(secNum)
        evenIter = evenIter + 6
    num += 1
    
for val in iter:
    print(val,end=" ")