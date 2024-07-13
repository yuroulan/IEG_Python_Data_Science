'''
1) xor , and , or , not
2) eqn opt for right shift

control statements :

conditional statements :
simple if
if else
cascaded if else / if else ladder
nested if else

if condition :
- using indentation (tab)

if(condition):
    stmt 1
    stmt 2
    stmt 3
else
    stmt 4

'''

# example
# if

age = int(input("Enter age : "))

if(age >= 18):
    print("Eligible to vote")
print("Welcome")

# elif

age = int(input("Enter age : "))

if(age >= 18 and age < 25):
    print("Eligible to vote")
elif(age >= 25):
    print("can vote and stand in election")
print("Welcome")

# cascaded if 

age = int(input("Enter age : "))

if(age >= 18 and age < 25):
    print("Eligible to vote")
elif(age >= 25):
    print("can vote and stand in election")
else:
    print("too young")
print("Welcome")

# nested if else

age = int(input("Enter age : "))

if(age <= 120 and age >= 0):
    if(age >= 18 and age < 25):
        print("Eligible to vote")
    elif(age >= 25):
        print("can vote and stand in election")
    else:
        print("too young")
else:
    print("Invalid age")
print("Welcome")

# 3 nesting

age = int(input("Enter age : "))

if(age <= 120 and age >= 0):
    if(age >= 25):
        if(age >= 60):
            print("senior")
        print("can vote and stand for election")
    elif(age >= 18):
        print("eligible to vote")
    else:
        print("too young")
else:
    print("Invalid age")
print("Welcome")


'''looping statements :


'''