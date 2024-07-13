#Problem 1:
# A laboratory technician always needs to prepare various solutions.
# Coming Sunday, he has to create a 20-liter solution that is 35% salt by mixing two available solutions. 
# One solution (A) is 25% salt, and 
# the other solution (B) is 50% salt. 
# How many liters of each solution are required to achieve the desired concentration?

# Coming Monday, he has to create an 8-liter solution that is 25% sugar by mixing two available solutions. 
# One solution (A) is 15% sugar, and 
# the other solution (B) is 40% sugar. 
# How many liters of each solution are required to achieve the desired concentration?

# Write a simple, generic Python program to assist the laboratory technician. 
# The program must take all these numbers (20 liters, 35, 25, 50) as input and 
# calculate the required liters of each solution and print them. 
# Please note that the same program must work for the second problem as well (8 liters, 25, 15, 40).

# The maximum stock for solution (A) and solution (B) is always 3 liter only. 
# After calculating/printing the required quantity of A and B, throw proper message. 
# For example, required quantity of solution (A) is less than 3 liter say "Solution (A) is available can proceed". 
# If required quantity of solution (B) is greater than 3 liter say "Solution (B) is not available, please order 1.3 liter now"

''' This code is to calculate the required quantity of A and B 
expected input from user -->> 20l, 35%, 25%, 50% (salt)
-->> 8l, 15%, 40% (sugar) '''

# how many SolA and solB needed for 20 litre and 35% of salt?
# how many solA and solB needed for 8 litre and 25% of sugar?

solVal = float(input("Enter volume value of solution : "))                # 20
solCon = float(input("Enter concentration value of solution : "))         # 35
solConA = float(input("Enter concentration value of solution A : "))      # 25
solConB = float(input("Enter concentration value of solution B : "))      # 50

solB = float((solVal * (solCon - solConA)) / (solConB - solConA))
solA = float(solVal - solB)
ordSolA = float(solA - 3)
ordSolB = float(solB - 3)

if(solA <= 3):
    print("Solution A is available. Can proceed.")
else:
    print(f"Solution A is not available. Please order {ordSolA:.2f} liter now.")
    
if(solB <= 3):
    print("Solution B is available. Can proceed.")
else:
    print(f"Solution B is not available. Please order {ordSolB:.2f} liter now.")

#-------------------------------------------------------------------#

# Problem 2:
# Initialize two variables, x = 0b10101100 and y = 0b11011001.
# Write Python code to:
# Extract the lower 4 bits from x.
# Check if y is even or odd.
# Clear the upper 4 bits of x.
# Check if the 5th bit of y is set.


x = 0b10101100 
y = 0b11011001

# to extract lower 4 bits from x
# expected output = 0b1100

ext = 0b00001111
print(bin(x & ext))         

# to check if y is even or odd

if(y & 0b00000001 == 1):
    print("Odd number.")
else:
    print("Even number.")

# to clear the upper 4 bits of x
# expected output = 0b1100

clr = 0b00001111
print(bin(x & clr))

# to check if the 5th bit of y is set

check = 0b00010000

if(y & check):
    print("5th bit of y is set.")
else:
    print("5th bit of y is not set.")

#-------------------------------------------------------------------#

# Problem 3:
# A construction project requires two workers to complete. 
# Worker A can complete the project in 12 hours, 
# while Worker B can complete the same project in 16 hours. 
# How long will it take for both workers to complete the project 
# if they work together?

# Another project requires Worker C, who can complete it in 8 hours, 
# and Worker D, who can complete it in 10 hours. 
# How long will it take for both workers to complete this project 
# if they work together?

# Write a simple, generic Python program to assist in calculating 
# the time required for two workers to complete a project when working together. 
# The program must take all these numbers (12, 16) as input 
# and calculate the required time. Finally, print the result. 
# Please note that the same program must work 
# for the second problem as well (8, 10).

# worker A = 12 hours
# worker B = 16 hours
workHrA = int(input("Worker A completed hour for one project : "))
workHrB = int(input("Worker B completed hour for one project : "))

# for time rate for projects per hour ; 
# workRateA = 1/12
# workRateB = 1/16
workRateA = 1 / workHrA
workRateB = 1 / workHrB
totWorkRate = workRateA + workRateB
# print(totWorkRate)

totTimeReq = 1 / totWorkRate

print(f"Worker A and worker B will need around {totTimeReq:.4f} hours to finish one project.")

#-------------------------------------------------------------------#

# Problem 4:
# Initialize two variables, a = 0b10101000 and b = 0b01010100.
# Write Python code to:
# Set the lower 4 bits of a.
# Combine the bits of a and b using OR.
# Create a mask to set the 2nd and 6th bits of a.

a = 0b10101000
b = 0b01010100

# to set lower 4 bits of a
# using or

toSet = 0b00001111
print(bin(a | toSet))

# to combine the bits of a and b using OR

print(bin(a | b))

# to create a mask to set the 2nd and 6th bits of a

create = 0b00100010
print(bin(a | create ))

#-------------------------------------------------------------------#

# Problem 5:
# An investor decides to invest a total of RM30,000 in two different accounts. 
# The first account offers a 5% annual interest rate, 
# while the second account offers a 7% annual interest rate. 
# If the total annual interest earned is RM1,800, 
# how much money was invested in each account?

# Another investor decides to invest a total of RM50,000 in two different accounts. 
# The first account offers a 3% annual interest rate, 
# while the second account offers a 6% annual interest rate. 
# If the total annual interest earned is RM2,400, 
# how much money was invested in each account?

# Write a simple, generic Python program to assist in 
# calculating the amount of money invested in each account 
# to achieve the desired total annual interest. 
# The program must take all these numbers (30000, 5, 7, 1800) as input 
# and calculate the required amounts. 
# Finally, print the result. Please note that the same program 
# must work for the second problem as well (50000, 3, 6, 2400).

totInvMon = float(input("Total invested money : "))
anIntRateA = float(input("Annual interest rate for 1st account : "))
anIntRateB = float(input("Annual interest rate for 2nd account : "))
totAnInt = float(input("Total annual interest earned : "))

accA = float(((totAnInt - (anIntRateB * totInvMon)) / (anIntRateA - anIntRateB)))
accB = float(totInvMon - accA)

print(f"The money invested in 1st account is RM{accA:.2f}.")
print(f"The money invested in 2nd account is RM{accB:.2f}.")

#-------------------------------------------------------------------#

# Problem 6:
# Initialize two variables, x = 0b10101100 and y = 0b11010010.
# Write Python code to:
# Swap the values of x and y without using a temporary variable.
# Toggle the 3rd and 5th bits of x.
# Check if two given numbers a = 29 and b = 15 are different

# to initialize 2 variables

# to swap the values of x and y w/o using temporary variable

x = 0b10101100
y = 0b11010010

print(f"Before swapping, x = {bin(x)} , y = {bin(y)}")

x = x ^ y
#print(bin(x))

y = x ^ y       # 0b10101100
#print(bin(y))

x = x ^ y           # 0b11010010
#print(bin(x))

print(f"After swapping, x = {bin(x)} , y = {bin(y)}")

# to toggle (flip a bit) the 3rd and 5th bits of x

x = 0b10101100

print(f"Before toggle 3rd and 5th bits of x, x = {bin(x)}")

mask = 0b00010100
# 3rd is 1 -->> 0
# 5th is 0 -->> 1

toggle = x ^ mask

print(f"After toggle 3rd and 5th bits of x, x = {bin(toggle)}")

# to check if two given numbers a = 29 and b = 15 are different

a = 29
b = 15

a != b

if(a != b):
    print(f"The two given numbers a = {a} and b = {b} are different.")
else:
    print(f"The two given numbers a = {a} and b = {b} are not different.")


 

























