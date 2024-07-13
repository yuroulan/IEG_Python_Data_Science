# product is a variable
# "Television" is a string value/literal
# to differentiate the variables from values we use double quotes ""
# or single quote '' -->> product = 'Television'

product = "Television"          # string
quantity = 2                    # integer
price = 1455.25                 # float
available = True                # True/ False (Boolean Value/Literal) # 1st & 2nd keyword

print('\n' "Product :", product)
print('\n' "Quantity :", quantity)
print('\n' "Price : RM", price)
print('\n' "Availability :", available)
print('\n')

# type is another built in fx that tell what is the
# data type of the variables (dynamically assigned by python)
# ((a + b) * c)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print('\n' "Total for 1 Television : RM", total)
print('\n')

# in real world use cases the 10 will not be hard code
# the 10 is coming from an input device (keyboard)
# so the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))
price = "1455.25"
# print(quantity * price) -->> not working

# type casting
# convert one data to another
# from str to int we have a built in fx int
# from str to float we have a built in fx float
total = int(quantity) * float(price)
print('\n' "Total for 10 Television : RM", total)
print('\n')

firstNumber = 500
# to see adress
# use built in fx "id"
print(id(firstNumber))

secondNumber = 500
print(id(secondNumber))
print('\n')

firstString = "Hello"
secondString = "Hello"
print(id(firstString))
print(id(secondString))

#-------------------------------------------------------------------#

# Fri 7/6/2024

# assign more than one value to more than one variables in one time

print("-" * 50)
x , y = 101 , 102               # x , y is assignment operators 
print(x)                        # (assigned value to variables)
print(y)

# x , y = 105 -->> not supported / not working

print("-" * 50)
x , y = 101 + 1 , 102 + 2
print(x)
print(y)

# Initialization
# assign variables but dont want add expression

print("-" * 50)
x = 0                           # numeric initializer
x = ""                          # string initializer / empty string / empty brain
x = None                        # no brain # 3rd keyword
print(type(None))               # None -->> want to create variable but dont know what value to assign



