# Functions

'''
- reusability
- program become modular

- inbuilt
- user-defined

def - definition

def (function.name) -->> follow same rule as variable name (no space, no symbols and etc)

exp = def sumOfTwoNumbers
      def sum_of_two_numbers(a, b): -->> a,b argument parameters

one indentation after def

return 

function waorks with stack model
- Last In First Out model
'''

# declare before main program

def sum_of_two_numbers(a, b):   # function definition   # a,b belongs to sum func (2nd arg)
    print("inside sum function")                        # a,b shall have same value but not numeric
    c = a + b
    return c    # default return value is None

# belongs to main program

print("inside main")    # will be executed first
a = 5
b = 10
c = sum_of_two_numbers(a,b) # function call # a,b -->> belongs to main program (1st arg)
print("sum = ", c)

print('-' * 50)

#-------------------------------------------------------------------#

# if the def is written after the main program
'''
print("inside main")    
a = 5
b = 10
c = sum_of_two_numbers(a,b) # not defined
print("sum = ", c)

def sum_of_two_numbers(a, b):
    print("inside sum function")
    c = a + b
    return c    

print('-' * 50)
'''
# not gonna works, because the c = sum_of_two_numbers(a,b) is not defined
#-------------------------------------------------------------------#

# what if a and b is input by user

'''def sum_of_two_numbers(a, b):
    print("inside sum function")
    c = a + b
    return c    # default return value is None

# belongs to main program

print("inside main")    # will be executed first
a = int(input("a : "))
b = int(input("b : "))
c = sum_of_two_numbers(a,b)
print("sum = ", c)
'''
#-------------------------------------------------------------------#

# to make a func call to multiply

def mul(x,y):
    print("inside mul func")
    f = x * y
    return f
    
def sum_of_two_numbers(a, b):   # function definition   # a,b belongs to sum func (2nd arg)
    print("inside sum function")                        # a,b shall have same value but not numeric
    c = a + b
    print(c)
    d = mul(c,b)
    return d    # default return value is None

# belongs to main program

print("inside main")    # will be executed first
a = 5
b = 10
c = sum_of_two_numbers(a,b) # function call # a,b -->> belongs to main program (1st arg)
f = mul(c, b)
print("sum = ", c)

print('-' * 50)










