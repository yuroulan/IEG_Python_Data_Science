# 2.
'''
Module: Continuous Prime Sum
In Maple Casino, there is a play in which contestant hit a ball to two numbered plates, and then contestant has to say a number which is summation of all the prime numbers from 1 to 'n' , here 'n' represent the first plate number. And the operation will continue upto 't' times, here 't' represent the second plate number.

Explanation:
First we perform the sum operation of all the prime numbers from 1 to 7 i.e. {2,3,5,7}, the sum of these prime numbers is: 17.
Then, again we have to perform the sum of all the prime numbers from 1 to 17, which is the previous sum of prime numbers.
1 to 17: {2,3,5,7,11,13,17}, and the resultant sum of prime numbers is: 58.
This operation will continue upto 2 times (for above mentioned sample input).

Write a program to find the continous sum of prime numbers 't' times.

Input Format:
First line as integer which corresponds to last integer of prime series.
Second line as integer which corresponds to number of times we have to perform the sum operation of that prime series.

Output Format:
A line as integer which corresponds to sum of all the prime numbers.

Input Format:
7
2
Output Format:
Sum:58
'''
def is_prime(num):
    """ Function to check if a number is prime """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_primes_up_to(num):
    """ Function to calculate all prime numbers up to 'num' """
    primes = []
    for i in range(2, num + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    num = int(input().strip())  # Read the last integer of prime series
    t = int(input().strip())    # Read the number of times to perform the sum operation
    
    prime_list = calculate_primes_up_to(num)
    n = sum(prime_list)
    
    for _ in range(t):
        prime_numbers = calculate_primes_up_to(n)
        n = sum(prime_numbers)
        print("Sum:", n)

if __name__ == '__main__':
    main()
