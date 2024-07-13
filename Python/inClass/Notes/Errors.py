# Errors :
# 1. Syntax Error -->> cannot execute code

# indentation 
# x = 10
# if(x % 2 == 0):
# print("Even Number")

# 2. Logical Error -->> end user will come and complain

# if(x % 2 == 0):
#     print(f"Given Number is {x}")
# print("Even Number)


# 3. Runtime Error -->> data input , user input 
# input supposed to be int, but user put 'RM'int
# user input data from storage
# must place the code inside Try Except block
# program not terminated abnormally

# try to connect into database
# installed something, it terminated/corrupted the database


try:
    principal = int(input("Principle: "))    # usually an input
except ValueError:
    # will only get executed when error occurs
    print("Principle amount must be integer. exp = 1000")
except Exception as e:
    print("Something went wrong : ", e)
else:
    # the code inside the else block gets executed 
    # only when there is no error
    print("All is well.")
finally:
    # The code inside this block will always get executed
    # regardless of wether an error occurs or not
    print("Thank You.")

period = int(input("period: "))
rate = int(input("Rate: "))
interest = (principal * period * rate) / 100
print(interest)

try:
    # put file open code here
    principal = int(input("Principle: "))    # usually an input
    # throw errors 
except ValueError:
    print("Principle amount must be integer. exp = 1000")
except Exception as e:
    print("Something went wrong : ", e)
else:
    # read content from file
    print("Content")
finally:
    # close file
    print("Close file.")

period = int(input("period: "))
rate = int(input("Rate: "))
interest = (principal * period * rate) / 100
print(interest)