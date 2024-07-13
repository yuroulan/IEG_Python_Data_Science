import mysql.connector as mysql

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

# 2 - Ask choice
def doMenu(connection):
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
            printProduct(connection)
        elif choice == 2:
            addProduct(connection)
        elif choice == 3:
            editProduct(connection)
        elif choice == 4:
            deleteProduct(connection)

# 3 Call this fx
def dbConnect():
    connection = mysql.connect(
        host="localhost", user="root", password= "", database="peneraju")
    return connection

# 2. Get Input
def addProduct(connection):
    try:
        Products = keyboardInp(str, "Product: ", "Product must be string.")
        Description = keyboardInp(str, "Description:", "Description must be String")
        Quantity = keyboardInp(int, "Quantity : ", "Quantity must be integer.")
        Price = keyboardInp(float, "Price : ", "Price must be float.") 
        SQL = f"""INSERT INTO Products(Name, Description, Quantity, Price) VALUES
                ('{Products}','{Description}',{Quantity},{Price})"""

        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()

    except Exception as e:
        print("Something when wrong when we add the product -->> ", e)

# 4. to read file
def printProduct(connection):
    SQL = f"SELECT Id, Name, Description, Quantity, Price FROM Products"
    cursor = connection.cursor()
    cursor.execute(SQL)

    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    for Id, Name, Description, Quantity, Price in cursor:
        print(f"{Id:<6d}|{Name:20s}|{Description:40s}|{Quantity:20d}|{Price:<20.2f}")

def editProduct(filename):
    try:
        Id = keyboardInp(int, "Please key-in the Product Id:", "Index must be Integer")
        SQL = f"SELECT Id, Name, Description, Quantity, Price FROM Products WHERE id = {Id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        Id, Name, Description, Quantity, Price = cursor.fetchone()

    except:
        print("Product for this id does not exists")

    else:
        print(f"Product: {name}\nDescription:{Description}\nQuantity:{Quantity}\nPrice:{Price}")
        confirm = keyboardInp(str, 'Are you sure you want to edit this product? y/n"')
        if confirm == 'y':           
                newProduct = keyboardInp(str, f"Product [ {product} ] : ", "Product must be string.", product)
                newDescription =keyboardInp(str, )
                newQuantity = keyboardInp(int, f"Quantity [ {Quantity} ] : ", "Quantity must be integer.", quantity)
                newPrice = keyboardInp(float, f"Price [ {Price} ] : ", "Price must be float.", price) 
                SQL = """UPDATE Products SET Name = {newProduct}, Description = '{newDescription}', Quantity """
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

connection = dbConnect()
doMenu(connection)


