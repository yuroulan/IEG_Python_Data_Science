# Relational and Logical Operators

# Relational Operator
'''
> < >= <= == !=
output -->> boolean value (True / False)
'''

print(12 > 15)  # False

# Logical Operator

'''
boolean value

and 
a       b       R
F       F       F
F       T       F
T       F       F
T       T       T

or
a       b       R
F       F       F
F       T       T
T       F       T
T       T       T

not
a       R
T       F
F       T
'''

# exp :
# number is divisible by 3 or 7

n = int(input("Enter a number : "))
print(n%3 == 0 or n%7 == 0)


