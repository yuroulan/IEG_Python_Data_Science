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