# functions

print("Hello World!!!")

# can i just use print() as above
# or do i have to create a function 
# place this code inside the function and 
# call the function

'''
1) Organize code
2) Un-organized code
'''

# How many places are you going to have this line of code
# code development (first time)
# code maintenance (second time)

# more than 1 time it must be converted to a function
# declaring a function
# def is a keyword we use to declare a function
# fx must have a name following the def keyboard
# the fx name is followed by parenthesis ()
# which followed by colon:
# suppose to be inside fx
# must have indentation

def sayHelloWorld():
    print("Hello World!!!")

# how to call or invoke a fx
# use fx name followed by parenthesis ()
# what will happened if not call or invoke fx -->> nothing happened (waste fx)

sayHelloWorld()

def greeting():
    print("Good Morning")

greeting()

# to take some input
# some fx required some input
# or a variable / place holder to keep the inp
# called as "parameter"

def greeting(name):             # name -->> parameter
    print("Good Morning", name)

# since the fx requires inp, must pass value
# the value is called "Argument"

greeting("John")                # John is argument

# to calculate simple interest
# take more than one parameter(s)

def calculateSimpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    print(interest)

# call / invoke the fx by passing more than one argument(s)
# the num of argument(s) must be same as num of parameter(s)
# arguments are positional

calculateSimpleInterest(1000, 1, 6)
calculateSimpleInterest(1000, 2, 7)
calculateSimpleInterest(1000, 3, 5)
# calculateSimpleInterest(1000, 3, input("Please key in rate : "))

# usually

'''rate = int(input("Please key in interest : "))
calculateSimpleInterest(1000, 3, rate)'''

# context
def buylunch(makan, minum):
    total = 0
    packedfood = []
    for food in makan:
        packedfood.append(food)
        if(food == "nasi"):
            total = total + 2.20
            if(food == "sayur"):
                total = total + 2.80
    for food in minum:
        packedfood.append(food)
        if(food == "nescafe"):
            total = total + 3
            if(food == "air suam"):
                total = total + 0.50
    # can return single value
    # return total
    # can return multiple values
    return [packedfood, total]

    print("Thank You")  # will never get executed, 
                        # dont write any statement after return

# context -->> caller context

result = buylunch(["nasi", "sayur"], ["nescafe", "air suam"])
# we can do this
result[1] += 0.80
# print(f"Amount to be paid : RM {result:0.2f}")
print("Food to be paid:" , result)

# can i have more than 1 return keyword?
# yes, but one return only executed, after that come out of the fx
# exp:

def evenOrOdd(givenNumber):
    if(givenNumber % 2 == 0):
        return "Even Number"
        print("will not get executed")
    else:
        return "Odd Number"
        print("will not get executed")

print(evenOrOdd(5))
print(evenOrOdd(6))

# whenever python requires to convert the collection of data
# it will always use tuple

def returnNumbers(numbers):
    return 10, 20, 30, 40, 50   # -->> cannot return more than 1 value
                                # python will return tuple of 5 numbers
print(returnNumbers())

def calculateTotal(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# variable len args
# caller context

print(calculateTotal([10, 20, 30, 40, 50]))
print(calculateTotal([10, 20, 30, 40, 50, 60, 70]))
print(calculateTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

data = tuple()

# when caller context cannot send value in list
# to handle var length args problem they introduce *parameters
# when python see * to conv args to tuple and pass tuple to fx
# whenever python has to conv a collection it will use tuple


def findTotal(*numbers):
    total = 0
    for number in numbers:
        total += 1
    return total

print(findTotal(10, 20, 30, 40, 50))
print(findTotal(10, 20, 30, 40, 50, 60, 70))
print(findTotal(10, 20, 30, 40, 50, 60, 70, 80, 90))



# pass -->> when dunno what to write
def add(a,b):
    return a + b

def minus(a, b):
    return(a,b)

def arithmetic(keyword, a, b):
    if(keyword == 'add'):
        return add(a, b)
    elif(keyword == 'minus'):
        return minus(a,b)
    
print(arithmetic("add, 10, 20"))

# pass function

def multiplication(a, b):
    return a * b


# print(arithmetic(func, 10, 20))
print(arithmetic(multiplication, 10, 20)) # -->> True
# print(arithmetic(multiplication(10, 20)) -->> wrong

