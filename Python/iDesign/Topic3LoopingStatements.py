# Problem 1
'''
Count
Mars Spell Bee is the largest self-motivated spelling competition held for school children. The children from different schools who are participating in the competition will be given a registration code.  The registration is on a first come first serve basis to a maximum of N entries.

The competition is conducted in two different galleries of the venue.  Just for the ease of their management, the Event organizers have announced to divide the children into two groups, to attend the competition in the two chosen galleries. By that note, all those children who have their registration code as an even number will be put in one gallery and those with odd number will be in another gallery.
Help the organizers to find count of number of even registration codes and odd registration codes from the total N.

Note: The registration code need not be unique as each child will have a unique school code.

Input Format:
The first line of input consists of a single integer N denoting the number of registration codes issued for the competition.
The next n lines of input consists of integers, denoting the registration codes of each child.

Output Format:
Output a single with the count of even numbers and odd numbers from N, separated by a single space.
Refer sample input and output for formatting specifications.

Sample Input 1:
3
1
4
10
Sample Output 1:
2 1

Sample Input 2:
5
2
6
23
12
11
Sample Output 2:
3 2
'''

# input consist of single integer N

N = int(input())

countEvenNum = 0
countOddNum = 0

for i in range(N):
    n = int(input())
    if(n % 2 == 0):
        countEvenNum += 1
    else:
        countOddNum += 1

print(countEvenNum, countOddNum)
    
# Problem 2
'''
Hazecraft Client Series
The Event Organizing Company "Hazecraft" focuses on event management in a way that creates a win-win situation for all involved stakeholders. Hazecraft doesn't look at building one time associations with clients but aim at creating long-lasting collaborations that will span years to come. This goal of the company has helped them to evolve and gain more clients within a notable time.
The number of clients of the company from the start day of their journey till now is recorded sensibly and is seemed to have followed a specific series like 2,3,5,7,11,13,17,19, 23,…, etc

Write a program that takes an integer N as the input and will output the series till the Nth term.

Note:

The given series is prime number series.
 
Input Format:

The first line of the input is an integer N.

Output Format:

The output is a single line series till Nth term, each separated by a space.
Refer sample input and output for formatting specifications.

Sample Input 1:

5

Sample Output 1:

2 3 5 7 11

Sample Input 2:

10

Sample Output 2:

2 3 5 7 11 13 17 19 23 29
'''

N = int(input())

primeNumFound = 0   # count
num = 2 # modulus

while(primeNumFound < N):
    primeNum = True
    for i in range(2, num):
        if(num % i == 0):
            primeNum = False
            break
    if primeNum:
        print(num, end=" ")
        primeNumFound += 1
    num += 1

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

# Problem 4

'''
Lucky Pairs
Richie and Riya are participating in a game called "Lucky pairs" at the Annual Game Fair in their Company. As per the rules of the contest, two members form a team and Richie initially has the number A and Riya has the number B.
There are a total of N turns in the game, and Richie and Riya alternatively take turns. In each turn the player whose turn it is, multiplies his or her number by 2. Richie has the first turn. Suppose after the entire N turns, Richie’s number has become C and Riya’s number has become D. The final score of the team will be the sum of the scores (C+D) of both the players after N turns.

Write a program to facilitate the quiz organizers to find the final scores of the teams.

Input Format:
The only line of input contains 3 integers A, B, and N.

Output Format:
Output a single line which contains the integer that gives the final score of the team which will be the sum of the scores of both the players after N turns.
Refer sample input and output for formatting specifications.

Sample Input 1:
1 2 1

Sample Output 1:
4

Sample Input 2:
3 2 3

Sample Output 2:
16    
'''
x,y,z = input().split() # let say, input 1 2 1

RichA = int(x)  # 1
RiyaB = int(y)  # 2
N = int(z)  # 1
turns = 0

while turns < N: 
    if(turns % 2 == 0): # for even position
        RichA *= 2
    else:
        RiyaB *= 2

    turns += 1

sum = RichA + RiyaB
print(sum)


# Problem 5

N = input()
Nlist = list(N)
print(Nlist)

firstDig = int(Nlist[0])
# firstInt = int(firstDig)
print(firstDig)

secDig = int(Nlist[-1])
print(secDig)

if int(N) >= 10:
    diff = firstDig - secDig
    print(abs(diff))
else:
    print("Invalid input")

        








