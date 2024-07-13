

fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]

# to print all fruit in the list
for fruit in fruits:
    print(fruit)
print('-'*50)

# print fruit which in even position
for fruit in fruits[::2]:
    print(fruit)
print('-'*50)

# print fruit that have 6 character
for fruit in fruits:
    if(len(fruit) == 6):
        print(fruit)
print('-'*50)

#----------------------------------------------------------------------#

# Wed 12/6/2024

# for while (conditional loop)

# range opt : will not generate number
# use to select from list
# fx called range help to generate number

# numbers = [1,2,3,4,,5,6,7,8,9,10.....10000] -->> cannot

numbers = range(1, 10000)

# to do multiplication table

print("Multiplication Table of 5.")
multiplicants = [1,2,3,4,5,6,7,8,9,10,11,12]
multiplier = 5
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)
print('-' * 50)

# start index is included and end index not included
print("Multiplication Table of 2.")
multiplicants = range(1, 13)
multiplier = 2
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)
print('-' * 50)

products = ["cooking oil", "ginger", "garlic", "tomato", "milk"]
for product in products:
    print(product)

print('-' * 100)

# to do while loop
# do you have a list? No
# how many digits did we have? Dunno

# take number as input
# print all digits in the number

usernumber = int(input("Enter the number : "))
# mynumber = 12345
# do you have a list? No
# how many digits did we have? Dunno
mynumber = usernumber

while(mynumber > 0):
    print(mynumber % 10)
    mynumber = mynumber // 10

mynumber = usernumber
print('-' * 100)

numberOfdigis = len(str(mynumber))
while(mynumber > 0):
    print(mynumber // 10 ** numberOfdigis)
    mynumber =mynumber % 10 ** numberOfdigis
    numberOfdigis = numberOfdigis -1
mynumber = str(usernumber)

print('-' * 100)

for number in mynumber:
    print(mynumber)

print('-' * 100)

# Hanafi's solution
num = int(input("Enter a number: "))
i = 0
while i < len(str(num)):
    print(int(str(num)[i]))
    i += 1
print('-' * 50)

#-------------------------------------------------------------------#

# Wed 19/6/2024

# for that have else part
# code in else part will get executed only
# when all the fruits are iterated fully
# the iteration is exhausted

fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]

# to print all fruit in the list
for fruit in fruits:
    print(fruit)
    if fruit == "durian" :
        break
else:
    print("All fruits are printed.")

# generate first 10 prime numbers
# the iteration is dunno

for num in range(2, 51):
    for divisor in range(2, num):
        if(num % divisor == 0):
            break       # we leave the while loop after printing 5 numbers
    else:
        print(f"{num} is a prime number.")

# while that have else part
# code in else part will get executed only
# when only are condition is fail
# cond in while loop must return FALSE 

count = 10
givenNumber = 2
while count > 0:
    for divisor in range(2, givenNumber):
        if(givenNumber % divisor == 0):
            break
    else:
        count -= 1
        print(f"{givenNumber} is a prime number.")
    givenNumber += 1
else:
    print("10 prime numbers are printed.")



count = 10
givenNumber = 2
while count > 0:
    for divisor in range(2, givenNumber):
        if(givenNumber % divisor == 0):
            break
    else:
        count -= 1
        print(f"{givenNumber} is a prime number.")
        if givenNumber > 10:
            break
    givenNumber += 1
else:
    print("10 prime numbers are printed.")

# Continue keyword
# continue the loop w/o executing the following statement

numbers = range(1, 10000)

# to do multiplication table

print("Multiplication Table of 7.")
multiplicants = [1,2,3,4,5,6,7,8,9,10,11,12]
multiplier = 7
for multiplicant in multiplicants:
    if multiplicant % 5 == 0:
        continue
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)



