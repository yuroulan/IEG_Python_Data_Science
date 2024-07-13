import json

try:
    with open('KedaiElektronik2.json', 'r') as filehandler:
        data = json.load(filehandler)
        print(type(data))
        
        for product in data:
            print(product["Name"])
            print(product["Quantity"])
            print(product["Price"])

except Exception as e:
    print("Something went wrong:", e)