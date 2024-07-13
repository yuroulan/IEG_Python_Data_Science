# Problem 1 
'''
FizzBuzz:

Write a program that prints the numbers from 1 to 100. 
But for multiples of three, print "Fizz" instead of the number, 
and for the multiples of five, print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz".
'''

num = range(1, 101)
# print(num)

for i in num:
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz", sep=" ", end="\n")
    elif(i % 5 == 0):
        print("Buzz", sep=" ", end=" ")
    elif(i % 3 == 0):
        print("Fizz", sep=" ", end=" ")
    else:
        print(i, sep=" ", end=" ")

# Problem 2
'''
Collatz Sequence:

Write a program that takes an integer input from the user 
and generates the Collatz sequence for that number. 
The Collatz sequence is defined as follows:

start with a number n. 
If n is even, the next number is n/2. 
If n is odd, the next number is 3n + 1. 
Repeat the process until n becomes 1.
'''

def collatzSeq(num):
    cntSeq = []
    while num <= 1:
        if(num % 2 == 0):   # to check if nums is even / odd
            num // 2
        else:
            num *= 3 + 1
    cntSeq.append(1)
    return cntSeq

nums = int(input("Enter any number to check Collatz sequences : "))

collatzSeq = collatzSeq(num) # to generate Collatz sequence
print(f"Collatz sequences for {nums} is : {collatzSeq}")

# Problem 3

'''
GCD Calculation:

Write a program that takes two integers from the user 
and calculates their greatest common divisor (GCD) using the Euclidean algorithm.
'''
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)  

numA = int(input("Enter the first number : "))
numB = int(input("Enter the second number : "))
        
gcdNum = GCD(numA, numB)

print(f"GCD for {numA, numB} is {gcdNum}")

# Problem 4

'''
Rock, Paper, Scissors:

Write a program that plays the game of Rock, Paper, Scissors with the user. 
The user makes a choice, the program randomly chooses, and the winner is determined.

To generate random number use random module

import random

random.randint(1,3)
'''

import random

print("Lets play, Rock, Paper & Scissors!")
print("""Please choose any number : 
1 -->> Rock
2 -->> Paper
3 -->> Scissors""")

while True:
    yrChoice = input("Your choice is : ")
    if(yrChoice in ['1', '2', '3']):
        yrChoice = int(yrChoice)
        break
    else:
        print("Invalid! Please choose only 1 , 2 or 3.")

print(f"You choose {yrChoice}")

print("Now, let see what number computer choose!")
compChoice = random.randint(1,3)
print(f'Computer chose {compChoice}')

if(yrChoice == compChoice):
    print("Ops! It's a tie!")
elif(yrChoice == 1 and compChoice == 3 or\
     yrChoice == 2 and compChoice == 1 or\
     yrChoice == 3 and compChoice == 2):
    print("Yeay! You win!")
else:
    print("Oh no! You lose! Hahaha! Try again!")

# Problem 5
'''
Number Guessing Game:

Write a program that randomly generates a number between 1 and 100. 
The user has to guess the number. 
After each guess, the program tells the user whether the guess is 
too high, too low, or correct. The game continues until the user guesses the correct number.

To generate random number use random module

import random

random.randint(1,3)
'''
import random
compNum = random.randint(1, 100)

print("""Let's play a guessing game! 
Guess the number that the computer has generated between 1 and 100.""")

guess = 0

while guess != compNum:
    userGuess = int(input("Your guess: "))
    guess = userGuess

    if guess < compNum:
        print("Too low! Guess a higher number!")
    elif guess > compNum:
        print("Too high! Guess a lower number.")
    else:
        print(f"True! You guessed the right number -->> {compNum}")

# Problem 6
'''
Problem 6 Perfect Number: 

Write a program that generates 10 perfect numbers.

Example

6: The divisors of 6 are 1, 2, 3, and 6. 
The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.

28: 
The divisors of 28 are 1, 2, 4, 7, 14, and 28. 
The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
'''
num = 40
prime = []

for i in range(2, num):
    primeNum = True
    for divisor in range(2, i):
        if(i % divisor == 0):
         primeNum = False
         break
    if(primeNum == True):
        prime.append(i)
for i in prime:
    break

for num in prime:
   q = 2 ** num - 1
   for divisor in range(2, q):
      qPrime = True
      if(q % divisor == 0):
         qPrime = False
         break
   if(qPrime == True):
         perfNum = q * 2 ** (num -1)
         print(perfNum)

# Problem 7
'''
Harmonic Series:

Write a program that calculates the sum of the first n terms of the harmonic series. 
Take the n as Input.

Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''

yrNum = int(input("Enter any number to calculate sum of first of the Harmonic number : "))
total = 0

for i in range(1, yrNum + 1):
    total += 1/i

print(f"Total sum of the first {yrNum} terms of the harmonic number is : {total:0.2f}")

# Problem 8
'''
Number to Words:

Write a program that converts a number to its word representation 
(e.g., 123 to "one hundred twenty-three").
'''
# to store words for num from 1 to 19
class1 = ["", "One", "Two", "Three", "Four", "Five", "Six", 
          "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", 
          "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
# to store words for num from 20 to 90
class2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
          "Eighty", "Ninety"]

def numToWords(num):
    wrd = ""
    if num // 100 > 0:
        wrd += class1[num // 100] + " Hundred and"
    num %= 100
    if num >= 20:
        if wrd:
            wrd += " "
        wrd += class2[num // 10]
        if num % 10 != 0:
            wrd += " " + class1[num % 10]
    elif num >= 10:
        if wrd:
            wrd += " "
        wrd += class1[num]
    else:
        if num > 0:
            if wrd:
                wrd += " "
            wrd += class1[num]
    return wrd

yrNum = int(input("""Please enter any number to convert into its word representation.
*Note that only up to 10 digits can be converted.
Your number: """))

if yrNum > 9999999999:
    print("Only up to 10 digits can be converted. Please re-enter the number.")
else:
    bill = yrNum // 1000000000
    yrNum %= 1000000000
    mill = yrNum // 1000000
    yrNum %= 1000000
    thou = yrNum // 1000
    yrNum %= 1000
    rem = yrNum

    numWords = ""
    if bill > 0:
        numWords += numToWords(bill) + " Billion and"
    if mill > 0:
        if numWords:
            numWords += " "
        numWords += numToWords(mill) + " Million and"
    if thou > 0:
        if numWords:
            numWords += " "
        numWords += numToWords(thou) + " Thousand and"
    if rem > 0 or len(numWords) == 0:
        if numWords:
            numWords += " "
        numWords += numToWords(rem)
    
    print(numWords)

# Problem 9
'''
Roman to Integer

Write a program to convert a Roman numeral to an integer 
and also convert integer to Roman numeral
'''
# make list of roman num
# make function for int to roman 
# make function for roman to int

# to make list for rom num
symVal1 = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), 
              ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

# to build fx for option '1'
def numToRom(n):
    result = ""
    for sym, val in symVal1:
        while n >= val:
            result += sym
            n -= val
    return result

symVal2 = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, 
           "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}


def romToNum(r):
    result = 0
    i = 0
    while i < len(r):
        if(i + 1 < len(r) and r[i:i+2 in symVal2]):
            result += symVal2[r[i:i+2]]
            i += 2
        else:
            result += symVal2[r[i]]
            i += 1
    return result

# to make user choose option
while True:
    userchoose = input("""Choose your option :
    1) Integer Number to Roman Number Converter
    2) Roman Number to Integer Number Converter
Your choose : """)
    if(userchoose == '1' or userchoose == '2'):
        break
    else:
        print("Please choose only option '1' or '2'")

if(userchoose == '1'):
    yrNum = int(input("Enter an integer number to be converted : "))
    romNum = numToRom(yrNum)
    print(f"The roman number for {yrNum} is {romNum}")
elif(userchoose == '2'):
    yrNum = (input("Enter a roman number to be converted : "))
    intNum = romToNum(yrNum)
    print(f"The integer number for {yrNum} is {intNum}")
    
# Problem 10
'''
String Compression

Write a program to perform basic string compression using the counts of repeated characters 
(e.g., "aabcccccaaa" -> "a2b1c5a3").
'''
strcomp = input("Enter string value: ") # let say user input = aaabbjee
strvalchar = strcomp[0]  # initialize char val into index 0 to be first val # a
count = 0
result = ""

for i in strcomp:
    if i == strvalchar: # if next str same with first str ;
        count += 1  # plus 1 
    else:
        result += str(strvalchar) + str(count)  # aaabbjee if compress -->> a3b2j1e2
        strvalchar = i  # to update current char of i to track new char count
        count = 1  # Reset count to 1 to start count new char occurence

result += str(strvalchar) + str(count)

print(f"The compressed string for {strcomp} is {result}")




















