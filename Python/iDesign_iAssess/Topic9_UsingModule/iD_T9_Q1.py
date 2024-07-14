# Problem 1
'''
Module: Fibonacci Series
The teacher was teaching about number series generation and one of the series is like she will write first two number of the series and each student has to write a next number of the series on the board and next number will be the addition of previous two numbers and first two numbers will be 0 and 1. 
So, help the students by writing a program to generate the Fibonacci series.

Input Format:  
The input consists of integer which represents 'n' as number of values in the series

Output Format:
The output consists of series of integer numbers.

Sample Input 1:
3
Sample Output1:
0 1 1

Sample Input 2:
6
Sample Output2:
0 1 1 2 3 5
'''

def fib(n):
    a, b = 0, 1

    # Initialize two variables:
    #   - `a` to 0, representing the first number in the Fibonacci sequence
    #   - `b` to 1, representing the second number in the Fibonacci sequence

    series = [] # Create an empty list named `series` to store the Fibonacci numbers

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series

n = int(input())

result = fib(n)

print(" ".join(map(str, result)))