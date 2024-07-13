# should not hard code data inside the program such as:
# fruits = ["apple", "orange", "mango"]
# must keep those fruits in txt , csv or, exc file
# must write a python to read data in file to do things
# data must be separated from the program

# create a file using python code
# can use the keyword 'open'

# open('fruits.txt')

# have to give instruction to python
# if file not exist, create it
# call such extra instruction as mode

# modes :
# 1. x --> create file if it doesnt exist
#           open('file name', 'mode')
# 2. t -->> going to be txt file
# 3. b -->> binary file
# 4. w -->> to write inside file
#           - will clear the existing content inside existing file
#           - need to rewrite the content inside the file
#           - whenever want to update content
# 5. a -->> append inside the file

# open('fruits.txt', 'xt')
# # get error if the file already exist
# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')
from os.path import exists
# exists('filename')

def keyboardInp(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = (input(caption))
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1 # cannot use True/Falsemore than 2 values
    while choice != 0:
        print("--------------")  
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("--------------")  

        choice = keyboardInp(int, "Choice [0, 1, 2, 3, 4] : ", "Choice must be integer")    

        if choice == 0:
            print("Thank you for using our system.")
            break
        elif choice == 1:
            printProduct(filename)
        elif choice == 2:
            addProduct(filename)
        elif choice == 3:
            editProduct(filename)
        elif choice == 4:
            deleteProduct(filename)
    
def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, 'xt')
        except Exception as e:
            print("Something when wrong when we create the file -->> ", e)
        else:
            createTitle(filename)
        finally:
            # filehandler is an obj/ instance of file class
            # has many methods like read, write, close
            filehandler.close()

def createTitle(filename):
    try:
        # syntax when dealing with resources -->> automatically close the program (safest method)
        # when come out of block, the resource will be close
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product | Quantity | Price") # -->> | pipe char as delimiter                                  
    except Exception as e:                                  # to split the line into multiple data
        print("Something when wrong when we create the header -->> ", e)

# 2. Get Input and Append file
def addProduct(filename):
    try:
        product = keyboardInp(str, "Product: ", "Product must be string.")
        quantity = keyboardInp(int, "Quantity : ", "Quantity must be integer.")
        price = keyboardInp(float, "Price : ", "Price must be float.") 
        with open(filename, 'at') as filehandler:
            filehandler.write(f"\n{product} | {quantity} | {price}")
    except Exception as e:
        print("Something when wrong when we add the product -->> ", e)

# 4. to read file
def printProduct(filename):
    try:
        lines = None
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if(index == 0):
                print(f"{"No.":5}{product:<30}{quantity:<20}{price:>20}")
                print('=' * 80)
            else:
                print(f"{index:<5}{product:<30}{quantity:>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something when wrong when we print the product -->> ", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
            # take index
        index = keyboardInp(int, "Please keyin the index of product : ", "Index must be integer.")
        if(index >= len(data)):
            print("Sorry, product not available.")
        else:
            product, quantity, price = data[index]
            print(f"Product : {product}\nQuantity : {quantity}\nPrice : {price}")
            print()
            confirm = keyboardInp(str,"Are you sure you want to edit this product? (y/n)\n", "Response must be string.")
            if confirm == 'y':
                newProduct = keyboardInp(str, f"Product [ {product} ] : ", "Product must be string.", product)
                newQuantity = keyboardInp(int, f"Quantity [ {quantity} ] : ", "Quantity must be integer.", quantity)
                newPrice = keyboardInp(float, f"Price [ {price} ] : ", "Price must be float.", price) 
                data[index] = [newProduct, newQuantity, newPrice]
                
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"    # join
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, 'wt') as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something when wrong when we edit the product -->> ", e)
              
def deleteProduct(filename):
    try:
        lines = None
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
            # take index
        index = keyboardInp(int, "Please keyin the index of product : ", "Index must be integer.")
        if(index >= len(data)):
            print("Sorry, product not available.")
        else:
            product, quantity, price = data[index]
            print(f"Product : {product}\nQuantity : {quantity}\nPrice : {price}")
            confirm = keyboardInp(str,"Are you sure you want to delete this product? (y/n)\n", "Response must be string.")
            if confirm == 'y': 
                # to delete products by index
                del data[index] 
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"    # join
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, 'wt') as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something when wrong when we edit the product -->> ", e)

filename = "KedaiElektronik.txt"
createFile(filename)
doMenu(filename)


# addProduct(filename)
# printProduct(filename)


# to make title, for add column
# then want to open file to make write mode





# content = input("Fruit name : ")
# # open built-in fx open the file and return the handler
# # which we can use to read-write inside the file
# filehandler = open(filename, '')

































