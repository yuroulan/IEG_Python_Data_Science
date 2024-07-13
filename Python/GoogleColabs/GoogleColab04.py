# Problem 1
# Print first 10 natural numbers using while loop

# natural number is all number but 0

num = 1

while num <=10:
    print(num, end=" ")
    num = num + 1
print()

#-------------------------------------------------------------------#

# Problem 2
# Print first 10 prime numbers using for loop

# to find prime number : 1. find factors of given number
#                           - exp : factors of 33 is 1 and 33

print("The first 10 prime number is : ")

num = 30
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
    print(i)

#-------------------------------------------------------------------#

# #Problem 3
# Get number of items as input and generate that many ADAM Numbers

adNums = int(input("Enter how many Adam number you want : "))

# let say, user want 5 number of Adam number

numIsAdam = 0
num = 1

while numIsAdam <= adNums:    # to check if adNums is Adam nums
        sqrAdNum = num ** 2   # exp : 13^2 = 169
        rvsAdNum = int(str(num)[::-1])    # exp : 13 = 31
        sqrRvsAdNum = rvsAdNum ** 2   # exp : 31^2 = 961
        rvsSqrRvsAdNum = int(str(sqrRvsAdNum)[::-1])  # exp : 961 = 169

        if rvsSqrRvsAdNum == sqrAdNum:
            print(num)
            numIsAdam += 1

        num += 1

#-------------------------------------------------------------------#

# Problem 4
# Get number of items as input and generate that many Armstrong Numbers

armStrNum = int(input("Enter how many Armstrong number you want : "))

armStrCounter = 0
num = 0

while armStrCounter < armStrNum :  # let say input = 2
    num_str = str(num)  # 0
    numDig = len(num_str)    # 1   

    total = 0
    for i in num_str:
        total += int(i) ** numDig

    if(total == num):
        print(num)
        armStrCounter += 1
    num += 1

#-------------------------------------------------------------------#

# Problem 5
# Write a program to print the following pattern using a loop.

'''
o

oo

ooo

oooo

ooooo
'''

pattern = 5

for i in range(1, pattern + 1):
    for j in range(1, i + 1):
        print("o", end=" ")
    print()

#-------------------------------------------------------------------#

# Problem 6
# Write a program to print the following pattern using a loop

'''
1

1 2

1 2 3

1 2 3 4

1 2 3 4 5
'''

num = 5

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#-------------------------------------------------------------------#

# Problem 7
# Get a number as input and calculate the sum of all numbers from 1 to the given number.

givNum = int(input("Enter one number to sum it altogether : "))

# let say givNum = 5

total = 0
startNum = 1

for i in range(1, givNum +1):
    total += i

print(f"The total sum of all numbers from {startNum} to {givNum} is : {total}" )

#-------------------------------------------------------------------#

# Problem 8
# Write a python program that takes few numbers as command line argument. 
# Use a loop to display all elements. 
# Use another loop to display all elements in the even position. 
# Use another loop to display all elements in the odd position.

import sys

numbers = sys.argv

print("All numbers inserted: ")
for num in numbers[1:]:     # to retrieve cmd line args, and exclude file name
    print(num, end=" ")     # to display all element in cmd line arg
print()

print("Numbers in even position is : ")

for i in range(1, len(numbers), 2):
    print(numbers[i], end="   ")
print()

print("Numbers in odd position is : ")

for i in range(2, len(numbers), 2):
    print("  " + numbers[i], end=" ")
print()

#-------------------------------------------------------------------#

# Problem 9
# Write a python program that takes few numbers as command line argument. 
# Find the average of those numbers.

import sys

nums = sys.argv[1:]

print("All numbers inserted: ")
for num in nums:     # to retrieve cmd line args, and exclude file name
    print(num, end=" ")     # to display all element in cmd line arg
print()

total = 0

for i in nums:
    total += int(i)

avg = total / len(nums)
print(f"The average number of {nums} is : {avg}")

#-------------------------------------------------------------------#

# Problem 10
# Write a Python program that takes a string as input, 
# which contains numbers separated by commas. 
# Convert the string to a list of numbers and 
# determine whether all the numbers are different from each other.

nStr = input("Enter the numbers (comma seperated) : ")

val = nStr.split(",")       # to convert into lists
print("Input given : ", val)

# to check if num is diff from each other

diff = 1

for i in range(len(val)):
    i = int(val[i])
    for j in range(i + 1, len(val)):
        j = int(val[j])

        if i == j:
            diff = 0
            print("Not all numbers are different from each other.")
    if not diff:
        break

if diff:
    print("All numbers are different from each other.")

#-------------------------------------------------------------------#

# Problem 11
# Write a Python program that takes a string as input, 
# which contains numbers separated by commas. 
# Convert the string to a list of numbers. 
# Now pick 3 unique numbers from the list whose sum is 100.

nStr = input("Enter any numbers (comma seperated) : ")

val = nStr.split(",")       # to convert into lists
print("Input given : ", val)

unqNum = 0
val = [int(num) for num in val]

for i in range(len(val)):
    if(unqNum == 1):
        break
    for j in range(i + 1, len(val)):
        num1 = val[i]
        num2 = val[j]
        num3 = 100 - (num1 + num2)
        if num3 in val[j + 1:]:
            print(f"The number lists that sum to 100 are : {num1}, {num2}, {num3}.")
            unqNum = 1
            break
if(unqNum == 0):
    print("No 3 number lists that can sum to 100.")

#-------------------------------------------------------------------#

# Problem 12
# Write a Python program to get 2 positive numbers as input and 
# multiply them without using the '*' operator.

# to take positive input

print("To multiply the both positive number you give: ")
n1 = int(input("Enter any only positive number (num1) : "))
n2 = int(input("Enter any only positive number (num2) : "))

num2 = n2

if n1 < 0:
    print("This is not positive number!")
elif n2 < 0:
    print("This is not positive number!")
else:
    mult = 0

# to multiply w/o * operator

    while n2 > 0:
        mult += n1
        n2 -= 1

    print(f"{n1} * {num2} = {mult}")

#-------------------------------------------------------------------#

# Problem 13
# Write a python program to print first 10 terms in a Fibonacci series

# to initiaze first and and second terms of Fibonacci series

fib = [0, 1]

# to print first term
a = fib[0]
print(a)

# to print sec term
b = fib[1]
print(b)

i = 2

while i < 10:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1

#-------------------------------------------------------------------#

# Problem 14
# Write a python program which takes a number as input and 
# convert the number to binary. 
# Note: Don't use any builtin functions.

num = int(input("Enter any number to be converted into binary : "))
numIn = num

# to initialize bin for str

if(num == 0):
    binToStr = "0"
else:
    binToStr = ""

    while num > 0:
        remNum = num % 2
        binToStr = str(remNum) + binToStr
        num //= 2

print(f"The binary number for {numIn} is {binToStr}.")

#-------------------------------------------------------------------#

# Problem 15
# Write a python program which takes a binary number as input and 
# convert the number to decimal. 
# Note: Don't use any builtin functions.

num = input("Enter any binary number to be converted into decimal : ")
numIn = num

# to initialize decimal value

decVal = 0
pow = 0

# to convert bin into dec

for val in num[::-1]:       # to reverse the bin num
    if(val == '1'):
        decVal += 2 ** pow
    pow += 1

print(f"The decimal number for {num} is {decVal}.")

