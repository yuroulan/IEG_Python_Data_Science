# simple decision making
# find whether given number is positive, negative or zero
# find whether my business is making profit, loss or breakeven

expenses = 1000
sales = 1100

# Obj 1 : please print when we have profit
if (sales > expenses):                          # if (sales - expenses > 0) , True / have profit
    print("You are making profit")              
    # called as 'block' of code 
    # --> one or more than one statement to be executed
    # if only the statement is satisfied then executed

# Obj 2 : please print when we have profit and loss
if(sales > expenses):
    print("You are making profit")
else:
    print("You are making loss")

# nested if
# Obj 3 : please print when we have profit , loss and breakeven

if(sales > expenses):
    print("You are making profit")
else:
    if(sales == expenses):
        print("You are at breakeven")
    else:
        print("You are making losses")

# @

if(sales > expenses):
    print("You are making profit")
elif(sales == expenses):
    print("You are at breakeven")
else:
    print("You are making losses")

print("The END")

# have single line of statement to be executed
# condition True or False, can use the syntax

# find whether the given number is even

givenNumber = 6
if (givenNumber % 2 == 0): print("Even number.")

# find whether the given number is odd and even
givenNumber = 7
print("Even number") if (givenNumber % 2 == 0) else print("Odd number.")

# find whether given number is positive, negative or zero
givenNumber = 0
print("+ve") if (givenNumber > 0) else print("-ve") if (givenNumber < 0) else print("Zero")


operator = "+"









