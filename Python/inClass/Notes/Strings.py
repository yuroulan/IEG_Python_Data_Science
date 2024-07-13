# Thu 6/6/2024

# Exp 1
# + is arithmetic operator used for addition
# both side must be integer or float
# 

# BUT if both data is strings then 
# python peforms 'String Concatenation'

firstName = "Khairi"
lastName = "Abu Bakar"
fullName = firstName + " " + lastName
print(fullName)
print("-" * 50)

#-------------------------------------------------------------------#

# Exp 2
# one is string and one is number
# python dont know weither to perform add or string concatenation

carplate = "JCG"
number = 9876
# carplatenumber = carplate + number <-- not working
# can only concatenate str to str not int

carplatenumber = carplate + str(number)
print("Carplate Number :", carplatenumber)
print("-" * 50)

#-------------------------------------------------------------------#

# Exp 3
# how to * str with str
# when * str with int the * becomes time operator

product = "book \n" 
print(product * 5)
print("-" * 50)

#-------------------------------------------------------------------#

# Tue 11/6/2024

# \ also called as space sequence 
# \n -->> new line character
# \t -->> tab character
# \r -->> carriage return

print("my name is Anati Mahirah. \r I am 25 years old.")

filepath = input("Enter the path : ")
filepath = "c:\newfolder\table\readme.txt"
filepath = "c:\\newfolder\\table\\readme.txt"
print(filepath)

# odd string
# raw strings
filepath = r"c:\newfolder\table\readme.txt"
print(filepath)

# string values / literal -->> "" and ''
# to diff variables and literals
# nameError = variables
# can use """....""" or '''...''' ( to handle multi-line strings)

"""                             # ignored
nwfnerfbueriffuefjbhrui         

"""

#----------------------------------------------------------------------#

# relationship between strings and list
# string are nothing but list of character

message = "Hello World" # ['H', 'e', 'l', 'l', 'l', 'o'', 'w', 'o', 'r', 'l', 'd']
print(message[0])
print(message[0:5])
print(message[-5:])
print(message[::-1])

mynumber = 86749
print(int(str(mynumber)[::-1]))

#----------------------------------------------------------------------#

total = 2 + 3 + 4 + \
5 + 6

#----------------------------------------------------------------------#

# many value that seperated by comma (str)
# want to split
numbers = input("Enter the numbers (comma seperated) : ") # return str
print(numbers)      # str
print(type(numbers))
values = numbers.split(",") 
print(values)       # convert into lists
print(type(values))
print('-' * 50)

# to do sum
total = 0
for value in values:
    total = total + int(value)
    print(total)
print(value)





















