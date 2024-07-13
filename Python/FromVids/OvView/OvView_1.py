# Vid 2 - Variables and Printing
age = 30
print(age)
# print(30)

age = 40 
print(age)

# snack case

friend_age = 23
friendAge = 23
friend_age_1 = 23
countries_visited = 9

PI = 3.14159                        # -->> constant
RADIANS_TO_DEGREES = 180 / PI

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 3 - Numbers in Python

age = 35                            # integer
PI = 3.14159                        # float

math_operation = 1 + 3 * 4 / 2 - 2  # 5
print(math_operation)

float_division = 12 / 3
print(float_division)

integer_division = 12 // 3
print(integer_division)

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 4 - Remainder of a division

integer_division = 13 // 5
print(integer_division)

remainder = 13 % 5
print(remainder)

x = 37
remainder = x % 2
print(remainder)

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 5 - Python strings

"""
Strings

This file talks about strings.
"""

my_string = "Hello, world!"
print(my_string)

string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'
any_other_with_quotes = "He said \"You are amazing!\" yesterday."
print(string_with_quotes)
print(another_with_quotes)
print(any_other_with_quotes)
print('\n')

multiline = """Hello, world.

My name is Jose. Welcome to my program."""
print(multiline)
print('\n')

name = "Jose"
greeting = "Hello, " + name
print(greeting)

age = 34
# print("You are " + age)    # -->> error because str cannot be add with int
# convert int into str 

age = "34"
print("You are " + age)

# @

age = 24
age_as_str = str(age)
print("You are " + age_as_str)

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 6 - python strings formatting

age = 45
print(f"You are {age}")

name = "Anati"
greeting = f"How are you, {name}"
print(greeting)

name = "Pika"
# final_greeting = "How are you, {}"   -->> cannot 
# but put this:
final_greeting = "How are you, {}"
pika_greeting = final_greeting.format(name)
print(pika_greeting)
# the (name) will be replace in {}

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

name = "Adam"
final_greeting = "How are you, {name}"
Adam_greeting = final_greeting.format(name = "Adam")
print(Adam_greeting)

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 7 - User input in Python

my_name = "Anati"
yr_name = input("Enter your name : ")
print(f"Hello {yr_name}. My name is {my_name}")

# age = input("Enter your age : ")
age = int(input("Enter your age : "))
# age_num = int(age)
print(f"You have lived for {age * 12} months")

print("-" * 50)

#-------------------------------------------------------------------#

# Vid 8 - Booleand and Comparasion in Python

age = int(input("Enter your age : "))
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming : {can_learn_programming}")

age = int(input("Enter your age : "))
# usually_not_working = age < 18 or age > 65   -->> want to avoid negative sentences
# print(f"At {age}, you are usually not working : {usually_not_working}")

usually_working = age >= 18 or age <= 65
print(f"At {age}, you are usually working : {usually_working}")

print(bool(35))     # -->> True
print(bool(""))     # -->> False
print(bool(0))      # -->> False

# True and False
# if
x = True and False  # if first statement is True, then output will show the False one
print(x)

x = 35 and 0   # 0
x = 0 and 35   # 0

name = ""
surname = "Smith"
greeting = name or f"Mr. {surname}"
print(greeting)

name = input("Enter your name: ")
surname = input("Enter your name: ")
greeting = name or f"Mr. {surname}"
print(greeting)

# print(not True)  -->> False
# print(not False) -->> True
















 





