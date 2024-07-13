# Mon   10/6/2024

name = "David"
batch = 101
fee = 1245.6578

# traditionally how we do this :
inputstring = " Hello " + name + "welcome to python class" + str(batch)
print(inputstring)

inputstring = f"Hello {name:40} , welcome to python class {batch}"
print(inputstring)

# name : ^40 -->> align name to center
inputstring = f"Hello {name:^40} , welcome to python class {batch}"
print(inputstring)

# name : >40 -->> align name to right
inputstring = f"Hello {name:>40} , welcome to python class {batch}"
print(inputstring)

inputstring = f"Hello {name:*>40} , welcome to python class {batch}"
print(inputstring)

inputstring = f"Hello {name:>40} , welcome to python class {batch:10d}"
print(inputstring)

inputstring = f"Hello {name:>40} , welcome to python class {batch:<10d} in KL."
print(inputstring)

inputstring = f"Hello {name:>40} , welcome to python class {batch:<10d} in KL for RM {fee:10.2f}."
print(inputstring)

