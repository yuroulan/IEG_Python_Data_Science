import pickle

myVar = [
    {'Name': "Television", 'Quantity': 20, 'Price': 1455.99},
    {'Name': "Computer", 'Quantity': 10, 'Price': 1865.99}
]

try:
    with open('KedaiElektronik2.bin', 'wb') as filehandler:
        pickle.dump(myVar, filehandler)

except Exception as e:
    print("Something went wrong:", e)

try:
    filehandler = open('KedaiElektronik2.bin', 'rb')
    data = pickle.load(filehandler)
        
    for product in data:
        print(product["Name"])
        print(product["Quantity"])
        print(product["Price"])

except Exception as e:
    print("Something went wrong:", e)