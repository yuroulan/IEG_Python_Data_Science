# Exercise 1: Basic Arithmetic Operations
# Write a Python program that does the following:
# Prompts the user to enter two numbers
# Stores these numbers in two variables 
# Performs and prints the results of addition, subtraction, 
# multiplication, and division of these two numbers

print("Please insert any number!")

a1 = int(input("First number :"))
a2 = int(input("Second number :"))

print("Addition for first and second number is :" , a1 + a2)
print("Substraction for first and second number is :" , a1 - a2)
print("Multiplication of first and second number is :" , a1 * a2)
print("Division of first and second number is :" , a1 / a2)

#-------------------------------------------------------------------#

# Exercise 2: Temperature Converter
# Write a Python program that:
# Prompts the user to enter a temperature in Celsius. 
# Converts the temperature to Fahrenheit. 
# Prints the temperature in Fahrenheit. 
# (Hint: The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32)

print("Please enter temperature value (in Celcius)!")

C = float(input("Temperature value :"))
CeltoFah = C * 9/5 +32

print("Temperature value (Celcius converted to Fahrenheit) is :" , CeltoFah)

#-------------------------------------------------------------------#

# Exercise 3: Area and Perimeter of a Rectangle
# Write a Python program that:
# Prompts the user to enter the length and width of a rectangle. 
# Calculates the area and perimeter of the rectangle. 
# Prints the area and perimeter.

print("Please insert the length and width value of a rectangle!")

Length = float(input("Length value :"))
Width = float(input("Width value :"))

AreaofRec = Length * Width

print("The total area of the rectangle is :" , AreaofRec)

#-------------------------------------------------------------------#

# Exercise 4: Simple Interest Calculator
# Write a Python program that:
# Prompts the user to enter the principal amount, rate of interest, and time in years. 
# Calculates the simple interest. 
# Prints the simple interest. 
# (Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)

print("Please enter the value required below :")

P = float(input("Principal Amount ="))
R = float(input("Rate of Interest ="))
T = float(input("Time in Years ="))

SI = (P * R * T) / 100
print("The simple interest is :" , SI)

#-------------------------------------------------------------------#

# Exercise 5: Swapping Two Variables
# Write a Python program that:
# Prompts the user to enter two numbers. 
# Swaps the values of the two variables. 
# Prints the values before and after swapping.

print("Please enter any two numbers to be swap!")

n1 = int(input("First number :"))
n2 = int(input("Second number :"))
print("Your original value is =" , n1 , n2)

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print("The swapped value =" , n1 , n2)
#-------------------------------------------------------------------#

# Exercise 6: Square and Cube
# Write a Python program that:
# Prompts the user to enter a number. 
# Calculates the square and cube of the number. 
# Prints the square and cube.

print("Please enter any number!")

num = int(input("Your number :"))

sqr = (int(num ** 2))
cube = (int(num ** 3))

print("The square value of this number is :" , sqr)
print("The cube value of this number is :" , cube)

#-------------------------------------------------------------------#

# Exercise 7: Calculate BMI
# Write a Python program that:
# Prompts the user to enter their weight in kilograms and height in meters. 
# Calculates the Body Mass Index (BMI). 
# Prints the BMI. 
# (Hint: The formula to calculate BMI is: BMI = weight / (height * height))

print("Please enter your weight (kg) and height (m) below :")

weight = (float(input("Weight (kg) :")))
height = float(input("Height (m) :"))

BMI = weight / (height * weight)

print("Your BMI is :" , BMI)

#-------------------------------------------------------------------#

# Exercise 8: Compound Interest Calculator
# Write a Python program that:
# Prompts the user to enter the principal amount, rate of interest, time in years, and number of times interest is compounded per year. 
# Calculates the compound interest. 
# Prints the compound interest.
# (Hint: The formula to calculate compound interest is: 
# A = P(1 + R / 100n)nt where A is the amount
# P is the principal amount 
# R is the annual interest rate 
# t is the time the money is invested for
# and n is the number of times interest is compounded per year)

print("Please enter all the requirement below :")

P = float(input("Principal Amount :"))
R = float(input("Rate of Interest :"))
t = float(input("Time in Years :"))
n = float(input("Number of Interest :"))

A = P * (1 + R / 100 * n) * n * t

print("The value of compound interest is :" , A)

#-------------------------------------------------------------------#

# Exercise 9: Convert 97409 to Binary
# Write a Python program that:
# Converts the given integer 97409 to its binary representation. 
# Prints the binary representation.

# result = str(remainder) + result 

valGiv = 97409
print("To convert the value given into binary = " , valGiv)

q1 = valGiv // 2
r1 = str(valGiv % 2)

q2 = q1 // 2
r2 = str(q1 % 2)

q3 = q2 // 2
r3 = str(q2 % 2)

q4 = q3 // 2
r4 = str(q3 % 2)

q5 = q4 // 2
r5 = str(q4 % 2)

q6 = q5 // 2
r6 = str(q5 % 2)

q7 = q6 // 2
r7 = str(q6 % 2)

q8 = q7 // 2
r8 = str(q7 % 2)

q9 = q8 // 2
r9 = str(q8 % 2)

q10 = q9 // 2
r10 = str(q9 % 2)

q11 = q10 // 2
r11 = str(q10 % 2)

q12 = q11 // 2
r12 = str(q11 % 2)

q13 = q12 // 2
r13 = str(q12 % 2)

q14 = q13 // 2
r14 = str(q13 % 2)

q15 = q14 // 2
r15 = str(q14 % 2)

q16 = q15 // 2
r16 = str(q15 % 2)

bin = r16 + r15 + r14 + r13 + r12 + r11 + r10 + r9 + r8 + r7 + r6 + r5 + r4 + r3 + r2 + r1

print("The binary number for 97409 is :" , bin)

#-------------------------------------------------------------------#

# Exercise 10: Convert 1011 to Decimal
# Write a Python program that:
# Converts the given binary 1011 to its decimal representation. 
# Prints the decimal representation.

valGiv = 1011
print("To convert the value given into decimal :" , valGiv)

n1 = 1
n2 = 0
n3 = 1
n4 = 1

v1 = int((2 ** 0) * n4)
v2 = int((2 ** 1) * n3)
v3 = int((2 ** 2) * n2)
v4 = int((2 ** 3) * n1)

print(int(v4 + v3 + v2 + v1))



