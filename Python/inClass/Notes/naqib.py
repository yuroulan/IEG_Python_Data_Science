# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')

from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-----------")
        print("0  -  Exit")
        print("1  -  List")
        print("2  -  Add")
        print("3  -  Edit")
        print("-----------")
        choice = keyboardInput(int, "Choice(0,1,2,3): ", "Choice must be Integer")
        if (choice == 0):
            print("Thnx")
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)



filename = "fruits.txt"

# if not exists(filename):
#     open(filename, "xt")

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
             createTitle(filename)
        finally:
            filehandler.close()


def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
            print("Something went wrong when we create the title:", e)
    finally:
            filehandler.close()

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be interger")
        price = keyboardInput(float, "Price: ", "Price must be float")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index == 0):
                print(f"{"No:":<5}{product:20}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we print the products", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filerhandler:
            lines = filerhandler.readlines()
        data = []
        for line in lines:
           data.append(line.strip().split("|"))
        index = keyboardInput(int, "Index of Product:", "Index must be INT")
        if (index >= len(data)):
            print("Sorry not available :(")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if (confirm == "y"):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be string")
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be interger")
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float")
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products", e)


filename = "fruits.txt"
createFile(filename)
doMenu(filename)

# addProduct(filename)
# printProduct(filename)

# DELETE PRODUCT
def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer")
        if(index >= len(data)):
            print("Sorry product is not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity:{quantity}\nPrice:{price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                # delete the product by index
                del data[index]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)