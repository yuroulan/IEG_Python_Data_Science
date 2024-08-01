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

# Problem 2
'''
Module: Factorial Number

A Mother wants to teach his 4th standard son about the factorial of a number. She told that the product of an integer and all the integers below, it is called a factorial of that number. Then she gave him a number to find the factorial of that number. So help that kid to find the factorial of that number.

Thus, write a program to find the factorial of a given number.

Input Format:  
The input consists of an integer which represents a number.

Output Format:
The output consists of an integer value represents factorial of that number.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
3
6
'''
def fact(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

n = int(input())

result = fact(n)
print(result)

# Problem 3
'''
Module: Element Search

In a school, class teacher wants to organize a game for L.K.G students and the game is like there will be a  basket  with numbered balls teacher will give one number and student has to search for that particular  numbered ball if student found that  numbered ball  then he has to say "Got It!" otherwise  "Sorry!".
Help the students to write a program to search the numbered ball.

Input  Format: 

The first line of input corresponds to the number of balls in the basket,n.
The next n  line of input consists of the numbered balls in the basket.
The last line of input consists of a numbered ball to be searched.

Output Format:

The output is a  string consist of 'Got It!' or 'Sorry!' (without quotes).
[All text in bold corresponds to input and the rest corresponds to output.]

Sample Input and Output 1:

5
21
18
90
6
74
6
Got It!

Sample Input and Output 2:

5
21
18
90
6
74
10
Sorry!
'''
def balltobesearched(balls, n2):
    if n2 in balls:
        return "Got It!"
    else:
        return "Sorry!"

n1 = int(input())

balls = []
for i in range(n1):
    n2 = int(input())
    balls.append(n2)

n3 = int(input())

result = balltobesearched(balls, n3)
print(result)

# Problem 4
'''
Module: Word Count
Teacher organize a debate competition, In order to check the student's talking skills, she will write a list of topics in cards, student has to pick one of the cards then she wants to group the student based on the topics they have selected  and she will name the group based on the topic's name.
Now help her to find a number of students in each group.

Input Format:
The first line of input is a string consists of lower case letter words  (each word will indicate topics selected by the student)


Output Format:
The output consists of a count of each word.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output:
mother father mother GST father GST facebook facebook GST
facebook-2
father-2
gst-3
mother-2
'''
def main():
    inpStr = input("Enter the String\n").lower().split()
    toCount = {}

    for topic in inpStr:
        if topic in toCount:
            toCount[topic] += 1
        else:
            toCount[topic] = 1

    for topic in sorted(toCount):
        print(f"{topic}-{toCount[topic]}")

if __name__ == '__main__':
    main()

# Problem 5
'''
Module: GCD of Two Numbers

The greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. After the explanation given by tuition teacher, now he wants to conduct the small test to check their understanding of GCD concept.
So, help the students by writing a program to find the GCD of Two Numbers.

Input  Format: 
The input consists of two integers.

Output  Format:
The output consists GCD of Two Numbers.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
Enter the two positive numbers
12
14
GCD:2
'''
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)  

print("Enter the two positive numbers")
numA = int(input())
numB = int(input())
        
gcdNum = GCD(numA, numB)

print(f"GCD:{gcdNum}")  

# Problem 6
'''
Module: First Non-Repeating Character

Sandhya and Pooja are playing string game. And Sandhya gives a string to Pooja, and she has to find a first non-repeating character from that string. So help Pooja by writing a program to find the first non-repeating character from that string.

Input Format:
The input consists of a string.

Output Format:  
The output consists of a character which represents the first non-repeating character.
If there is no non-repeating character in the string, then print '#'.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
swiiss
w

Sample Input and output 2:
naddan
#
'''
def firstnonRepeatingChar(s):
    countChar = {}

    for char in s:
        if char in countChar:
            countChar[char] += 1
        else:
            countChar[char] = 1

    for char in s:
        if countChar[char] == 1:
            return char
        
    return '#'

s = str(input())
print(firstnonRepeatingChar(s))

# Problem 7
'''
Write a program to calculate maximum and minimum number from the given user input.

Note : Use built-in function only.

Input and Output Format :

(Refer sample input and output)

[All text in bold corresponds to input and rest others are output]

Sample Input and Output :

Enter the values:

1 4 6 12 73 92 134

The maximum value is : 134

The minimum value is : 1
'''

def maximumMinimum(nums):

    listNum = list(map(int, nums.split()))

    maxVal = max(listNum)    # max and min is a builtin fx
    minVal = min(listNum)

    print(f"The maximum value is : {maxVal}")
    print(f"The minimum value is : {minVal}")

print("Enter the values:")
userInp = input()
maximumMinimum(userInp) # tuple

# Problem 8
'''
Write a program to find the character based on the ASCII value given by the user as an input. Display the character based on the ascii value provided by the user.

Note : Refer to the problem requirements

Input and Output Format :

(Refer to sample input and Output)

[All text in bold corresponds to input and rest others are output]

Sample Input and Output :

Enter the value :

65

Character of ASCII value 65 is  A
'''
def acsiitoChar(asciiVal):
    char = chr(asciiVal)

    print(f"Character of ACSII value {asciiVal} is {char}")

print("Enter the value:")

asciiVal = int(input().strip())
acsiitoChar(asciiVal)

# iassess
# 1.
'''
Module: String Splitting
Akash wants to send a message to his colleague about his official team work. But he wants to maintain his message privacy, so he will encrypt his message and send that to his friend. Now his colleague wants to decode that message. Akash gave a hint to his colleague, like he has to decode his message by splitting his message with a particular character sent by him. Help Akash's colleague to decode the message by writing a program.

Input Format:
The first line of input consists of a string.
The next line of input consists of a character.

Output Format:
The output is a list of strings after splitting.
Every first letter of splitted word should be in capital.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
aaahggghbbb
h
Strings after splitting
Aaa
Ggg
Bbb

Sample Input and Output 2:
ahhg&hcg&fhgf90
&
Strings after splitting
Ahhg
Hcg
Fhgf90
'''
def decode(nStr, nChar):
    # Split the string using the specified character
    capLetter = [letter.capitalize() for letter in nStr.split(nChar)]
    
    # Print the formatted output
    print("Strings after splitting")
    for letter in capLetter:
        print(letter)

# Example usage:
print("Enter the message:")
nStr = input().strip()  # Read the message input
print("Enter the character for splitting:")
nChar = input().strip()  # Read the split character input

decode(nStr, nChar)

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


    



