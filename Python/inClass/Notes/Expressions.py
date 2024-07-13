# Thu 6/6/2024

# Exp 1
# arithmetic operators
# add / sub / mult / div / exp 
x = 7
y = 2

# expressions can be passed to print fx
# expression is an argument to print fx
print("Addition :" , x + y)
print("Substraction :" , x - y)
print("Multiplication :" , x * y)
print("Division :", x / y)
print("Quotient :", x // y)
print("Remainder :", x % y)
print("-" * 50)

#-------------------------------------------------------------------#

# Exp 2
# How to find exponent
# 10 x 10 x 10

print(10 ** 3)
print("-" * 50)

# what is max no. of 64 bit have
print((2 ** 64) - 1)
print("-" * 50)

#-------------------------------------------------------------------#

# Fri 7/6/2024

# Assignment Operators
x = 100                         # we assign 100 to x
x += 1          # x = x + 1
x += 2          # x = x + 2     # x incrementing by 2
x += 5          # x = x + 5

#-------------------------------------------------------------------#

# Fadhli's Equation
x = 108                         # x = 108 + 109 = 217
x += x + 1                      # x = x + (x + 1)
print(x)

x -= 1                          # x = x - 1
x *= 1                          # x = x * 1
x /= 1                          # x = x / 1
x //= 5                         # x = x // 5
x %= 5                          # x = x % 5

#-------------------------------------------------------------------#

# Comparasion Opt
# To create True statement

print("-" * 50)
myHeight = 5.2
yourHeight = 5.3
myBroHeight = 5.2

print(myHeight < yourHeight)
print(yourHeight > myHeight)
print(myHeight == myBroHeight)

print(myHeight != yourHeight)
print(myHeight <= myBroHeight)  # less than or equals to
print(myHeight <= yourHeight)

print(myBroHeight >= myHeight)  # greater than or equals to
print(yourHeight >= myHeight)

#-------------------------------------------------------------------#

# Logical Opt (more than one condition)
# and : both / all conditions must be True (4th keyword)
# or: any one of conditions is True (5th keyword)
# To create TRUE statement

print("-" * 50)
a = 10
b = 7
c = 4

print(a > b and a > c )         # True means a is the biggest number
print(c < a and c < b)          # True means c is the smallest number

print(a > b or a > c)           # True means a can be bigger than b, a can be bigger than c, a can be bigger than a and c
print(b < a and b >c)

a = 4
b = 7
c = 10
print ((b < a and b > c) or (b > a and b < c))

#-------------------------------------------------------------------#

# Negation Opt 
# if True it change to False
# if False it change to True

isAvailable = True
print(not isAvailable)
print(not not isAvailable)

# sometime we have a statement to be executed
# when the condition fails but dont have any statement to be
# executed when the condition is True
# not (6th keyword)
# if(condition == True)
#     nothing to do
# else
#     got something to do
# if (not condition == True)
#   got something to do

myHeight = 5.2
yourHeight = 5.3

print(myHeight < yourHeight)         # False  --> True
print(not myHeight < yourHeight)     # True   --> False
print(not not myHeight < yourHeight) # False  --> True

#-------------------------------------------------------------------#




