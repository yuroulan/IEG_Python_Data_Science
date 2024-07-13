# list
fruits = ["apple", "orange", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# overseafruits = fruits -->> cannot
# overseafruits = fruits.copy() -->> right way

# new list is same as original list
# we iterate thru the list and create a new list
# can use map fx
overseafruits =[]
for fruit in fruits:
    overseafruits.append(fruits)
print("copy using for loop:", overseafruits)

prices = [10, 20, 30, 40, 50]
pricewithsst = []
for price in prices:
    pricewithsst.append(price + (price * 0.06))
print("copy using for loop:", pricewithsst)

# using a class called map
# it will return map object (interator)
# 1. cvrt exp into fx

def calculateSST(price):
    return price + (price * 0.06)

# 2. Use map class
# - will take 2 parameters
# 1st parameter is yr fx
# 2nd parameter is yr list
pricewithsst = map(calculateSST, list(prices))

# 2. new list created <= original list
# same like prime number coding
multipleofthree = []
for number in range(0, 16):
    if(number % 3 == 0):
        multipleofthree.append(number)
print(multipleofthree)

numbers = [9, 4,3, 7, 6, 5, 11, 12, 18, 17, 27]

for number in numbers:
    evenNum = []
    if(number % 2 ==0):
        evenNum.append(number)
print(evenNum)

def isMultipleOfThree(number):
    return True if (number % 3 == 0) else False
multipleofthree = filter(isMultipleOfThree, range(0,16))
print(f"filter : ", multipleofthree)


# list comprehension -->> newlist = oldlist + for loop 
# -->> list + for loop
# for problem 1 and 2

# [expression for number in numbers]
overseafruits = [fruit for fruit in fruits]
pricewithsst = [price + (price * 0.06) for price in prices]

# [expression for number in numbers condition]
multipleofthree = [number for number in range(0, 16) if(number % 3 == 0)]
print(multipleofthree)

evenNum = [evenNum for number in numbers if(number % 2 == 0)]
print(evenNum)

pricewithsst
# we iterate thru the list and reduce it to a single value (cannot use list comp)
numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total = total + number
print(total)


# functools (builtin module) to import reduce

from functools import reduce

def calculateTotal(previous, current):
    return previous + current


















