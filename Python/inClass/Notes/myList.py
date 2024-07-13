# list is a data structure / sequence
# list is denoted using sqr bracket []
# list allow duplicates
# list is modifiable
# list is ordered (items inside list retain its position)
# list is indexed
# data inside the list is heterogeneous
# the data can be of diff types

# create a list
fruits = ["apple", "orange", "mango", "banana", "grape"]    
# fruits (var) that can hold more than one value
# fruits also an object, instance of a lists (class) 
# instance in class, called as object
# Jegan, John are objects, instance of Human (class)
# Jegan has 2 eyes (properties (what he has))
# Jegan can teach, walk, etc. (method(what he can do))

quantity = [10, 20, 30 ,40, 50]

# indexing and Selection (refer inClass\VariablesTwo.py)

# can add more item to the existing list
# method (what lists can do)
# mthod -->> append

fruits.append("durian")
print(fruits)

# you can insert items into existing list
# insert another method we have in list class
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3, "cempedak")
print(fruits)

# how to modified existing items?
# banana -->> mangosteen

fruits[5] = 'mangosteen'
print(fruits)

# to remove grape
fruits.remove("grape")  # remove only first instance of grape
                        # if have two  will only remove the 1st grape
print(fruits)

# how can i remove item using index?
# no method to do this
# however can use del keyword 
# del keyword will delete anything from memory permanently
# del, delte everything

del fruits[3]
print(fruits)

myName = "Jegan"
del myName
# print(myName) # not defined anymore 

# to clear all items in the list
fruits.clear()
print(fruits)
del fruits
# print(fruits)  # not defined anymore


fruits = ["apple", "orange", "mango", "banana", "orange", "grape"] 
# ["apple", "orange", "mango", "banana", "orange", "grape"] fruits becomes an object/
# instance of list class
if("orange" in fruits):
    print(fruits.index("orange"))
    print(fruits[fruits.index("orange")+1:].index("orange") + fruits.index("orange") +1)

# fruits.index("orange") -->> 1
# fruits.index("orange")+1 -->> 2
# fruits[2:] -->> ["mango", "banana", "orange", "grape"] 
# fruits[2:}.index("orange") -->> 2.....(2)]

# built in fx named enumerate
# enumerate is fx used to find index of every item in the list
enumeratedfruits = enumerate(fruits)
print(enumeratedfruits)
# enumerate object is also an iterable object
# fruits is a list
# fruits must be iterable object
# print fx donno how to iterate, print adress location of object
# we can typecast any iterable object to a list
# using a class list
fruitlist = list(enumeratedfruits)
print(fruitlist)

# list[(tuple)]tuple -->> read only list
# each tuple has 2 values : 1) index, 2) item
# index of item in the list


for item in fruitlist:
    if item[1] == "orange" :
        print(item[0])

# shallow copy - effect

x = [10, 20, 30, 40, 50, 60, 70]
y =x    # dont do this
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# deep copy

x = [10, 20, 30, 40, 50, 60, 70]
y = x.copy()    # list, tuple, set, dic, numpy, series, panda, everything
# y =x    # dont do this
y = []  # instead create new list

for i in x:
    y.append(i)
print('-' * 50)

print(x)
print(y)
x[2] = 35
print(x)
print(y)

# parenthesis () is confusing
# to call/invoke anything in python we use the operator () round bracket
# to call/invoke a builtin fx print(), id(), range()



