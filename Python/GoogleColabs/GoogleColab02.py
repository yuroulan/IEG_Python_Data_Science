# Exercise 1: Check Even or Odd
# Write a Python program that takes an integer as input and 
# checks whether it is even or odd

# devide number by 2. 
# if there is a remainder, the number is odd.
# if there is no remainder, the number is even.
# formula -->> num % 2 = 0

num = int((input("Please insert any value : ")))


if(num % 2 == 0):
    print("The value given is even number.")
else:
    print("The value given is odd number.")

#-------------------------------------------------------------------#

# Exercise 2: Grade Evaluation
# Write a Python program that takes a score (between 0 and 100) as input and 
# prints the corresponding grade based on the following criteria:
# A for scores 90 and above
# B for scores 80-89
# C for scores 70-79
# D for scores 60-69
# F for scores below 60

val = int(input("Please insert value between 0 ~ 100 : "))

if(val >= 90 and val <= 100):
    print("This student obtain A.")
elif(val >= 80 and val <= 89):
    print("This student obtain B.")
elif(val >= 70 and val <= 79):
    print("This student obtain C.")
elif(val >= 60 and val <= 69):
    print("This student obtain D.")
else:
    print("This student obtain F.")

#-------------------------------------------------------------------#

# Exercise 3: Check Leap Year
# Write a Python program that takes a year as input and 
# checks whether it is a leap year

# Leap Year Rule :
# leap year if divisible by 4
# but if divisible by 100, its not a leap year
# also divisible by 400

leapYear = int(input("Put any year : "))

if(leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0):
    print("This year is a leap year.")
else:
    print("This year is not a leap year.")

#-------------------------------------------------------------------#

# Exercise 4: Number Comparison
# Write a program that takes three numbers as input and 
# prints the largest one.

print("Give me 3 different value : ")

val1 = int((input("First value : ")))
val2 = int((input("Second value : ")))
val3 = int((input("Third value : ")))

if(val1 >= val2 and val1 >= val3):
    print(f"The biggest number is {val1}.")
elif(val2 >= val1 and val2 >= val3):
    print(f"The biggest number is {val2}.")
else:
    print(f"The biggest number is {val3}.")

#-------------------------------------------------------------------#

# Exercise 5: Check Vowel or Consonant
# Write a Python program that takes a single character as input and 
# checks whether it is a vowel or consonant.

singChar = str(input("Please give one single character (a ~ z): "))


if(singChar == "a" or singChar == "A" or singChar == "e" or singChar == "E" or singChar == "I" or singChar == "i" or singChar == "o" or singChar == "O" or singChar == "u" or singChar == "U"):
    print("This character is a vowel.")
else:
    print("This character is a consonant.")

#-------------------------------------------------------------------#

# Exercise 6: BMI Calculator
# Write a program that calculates the Body Mass Index (BMI) and 
# categorizes it into different weight statuses 
# The formula for BMI is weight / height^2, where weight is in kilograms and height is in meters.
# Categories:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 24.9
# Overweight: 25 <= BMI < 29.9
# Obesity: BMI >= 30

print("Please enter your weight (kg) and height (m) below : ")

weight = (float(input("Weight (kg) : ")))
height = float(input("Height (m) : "))

BMI = weight / (height ** 2)

print("Your BMI is : " , BMI)

if(BMI < 18.5):
    print("Your BMI category is underweight.")
elif(18.5 <= BMI < 24.9):
    print("Your BMI category is normal weight.")
elif(25 <= BMI < 29.9):
    print("Your BMI category is overweight.")
else:
    print("Your BMI category is obesity.")

#-------------------------------------------------------------------#

# Exercise 7: Triangle Type Checker
# Write a program that takes the lengths of three sides of a triangle and 
# determines whether the triangle is equilateral, isosceles, or scalene.
# Equilateral: All three sides are equal.
# Isosceles: Exactly two sides are equal.
# Scalene: All three sides are different.

print("Please put the value of sides of a triangle below : ")

Tri1 = input("Side (1) : ")
Tri2 = input("Side (2) : ")
Tri3 = input("Side (3) : ")

if(Tri1 == Tri2 and Tri1 == Tri3):
    print("This triangle is Equilateral because all the three sides were equal." )
elif(Tri1 != Tri2 and Tri1 != Tri3):
    print("This triangle is Scalene because all three sides were different.")
else:
    print("This triangle is Isosceles because exactly two sides were equal.")

#-------------------------------------------------------------------#

# Exercise 8: ATM Withdrawal
# Write a program that simulates an ATM withdrawal. 
# The user enters the withdrawal amount and 
# the program checks if the amount is a multiple of 10. 
# If it is, the program prints the number of each denomination (50, 20, 10) required to dispense the amount. 
# If not, it prints an error message. 
# For example if the amount is 233 then it must print "4 50 dollar bills, 1 20 dollar bills, 1 10 dollar bills, 3 1 dollar bills

# every number that is multiple of 10 is having zero placed 
# next to the number by which 10 is multiplied
# exp : 60, 40, 30, 50 and etc.

print("Please enter the withdrawal amount!")

# user will put their desired withdrawal amount

withDrAmn = int(input("Withdrawal Amount : "))    # 230

# need to make sure the value put is a multiple of 10
# valAmn_10 = withDrAmn % 10 != 0

# let say user put 230 for withdrawal

# Denomination calculation

if(withDrAmn % 10 == 0):
    Deno_50 = withDrAmn // 50                           # 4 --> deno (4x50)
    DenoRem_50 = withDrAmn % 50                         # 30

    Deno_20 = DenoRem_50 // 20                          # 1 --> deno (1 x 20)
    DenoRem_20 = DenoRem_50 % 20                        # 10

    Deno_10 = DenoRem_20 // 10                          # 1 --> deno (1 x 10)
    DenoRem_10 = DenoRem_20 % 10                        # 0

    print(f"""Accept! 
{Deno_50} x 50 dollar bills | {Deno_20} x 20 dollar bills | {Deno_10} x 10 dollar bills
Total withdrawal value = {withDrAmn} dollar""")
else:
    print("Error! Make sure your value is a multiple of 10.")



#-------------------------------------------------------------------#

# Exercise 9: Adam Number
# Write a Python program to check whether a given number is an Adam number.
# An Adam number is a number for which the square of the number and 
# the square of its reverse are themselves reverses of each other. 
# In other words, if you take a number, reverse it, square both the original number and the reversed number, and 
# the results are still reverse of each other, then the original number is called an Adam number.

# To solve :
# 1) 13 ^ 2 = 169
# 2) rvs = 13 = 31
# 3) 31 ^ 2 =961
# 4) rvs2 = 961 = 169 -->> step 1)

print("""Please put any number to check Adam number.
p/s: Only number between 0 to 100 is applicable for now :D""")

num = int(input("Your number : "))

# let say num = 13
# to reverse num = 31

num1 = num ** 2                                             # 169
remNum1 = num % 10                                          # 3
divNum1 = num // 10                                         # 1
# print(remNum1 , divNum1)

revNum = (remNum1 * 10) + (divNum1 % 10)                    # 31
print(f"The reverse value for {num} is : " , revNum)

# sqr revNum = 31 = 961
sqrRevNum = revNum ** 2                                     # 31 ^ 2 = 961
print(f"The square value for {revNum} is : " , sqrRevNum)   # 961
                         
adNum = 0
# To re-reverse the sqrRevNum = 961 = 169
reRevNum1 = sqrRevNum // 10                                  # 96
# print(sqrRevNum)  
reRevRem1 = (adNum * 10) + (sqrRevNum % 10)                 # (1) # 1
# print(reRevRem1)

reRevNum2 = reRevNum1 // 10                                 # 9
# print(reRevNum2)
reRevRem2 = (reRevRem1 * 10) + (reRevNum1 % 10)             # (2) # 16
# print(reRevRem2)

reRevNum3 = reRevRem2 // 10                                 # 0
# print(reRevNum3)
reRevRem3 = (reRevRem2 * 10) + (reRevNum2 % 10)             # (3) # 9 = 169
print(f"The reverse square for {sqrRevNum} is :" , reRevRem3)  

if(reRevRem3 == num1):
    print("So the value you insert is Adam Number.")
else:
    print("So the value you insert is not Adam Number.")

#-------------------------------------------------------------------#

# Exercise 10: Armstrong Number
# Write a Python program to check whether a given number is an Armstrong number.
# An Armstrong number (also known as a Narcissistic number or a Pluperfect number) 
# is a number that is equal to the sum of its own digits 
# each raised to the power of the number of digits. 
# For example, 153 is an Armstrong number because 
# 1 ** 3 + 5 ** 3 + 3 ** 3 = 153
# Other Armstrong number is including 0, 1, 153, 370, 371 and 407

print("""Please enter any number from 0 ~ 1000 .
Lets check whether the value is Armstrong Number or not.""")

armStr = int(input("Your Value : "))

# reverse the value given by user
# let say value given = 153

n1 = armStr // 10         
r1 = armStr % 10

n2 = n1 // 10
r2 = n1 % 10

n3 = n2 // 10
r3 = n2 % 10
# print(r3 , r2 , r1)

num1 = r3 ** 3
num2 = r2 ** 3
num3 = r1 ** 3
print(f"""To prove its Armstrong Number by ;
{r3} * {r3} * {r3} = {num1} 
{r2} * {r2} * {r2} = {num2}
{r1} * {r1} * {r1} = {num3}""")

addNumAll = num1 + num2 + num3
print(f"Then, add up {num1} + {num2} + {num3} = " , addNumAll)


if(addNumAll == armStr):
    print("The value added up is equal to the number you put.")
    print("Therefore, this number is an Armstrong Number.")
else:
    print("Unfortunately, this number is not an Armstrong Number.")

