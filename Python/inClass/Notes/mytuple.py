# Tuple

# tuple is a data structure / sequence
# tupple is nothing but read only list
# tuple is denoted using sqr bracket []
# tuple allow duplicates
# tuple is not modifiable
# tuple is ordered (items inside tuple retain its position)
# tuple is indexed
# data inside the tuple is heterogeneous -->> data can be diff type
# the data can be of diff types

fruits = ("apple", "orange", "mango", "banana")
print(type(fruits))
print(fruits)

# indexing & selection -->> inClass\Notes\VariablesTwo.py

# no need appen, remove, pop, del

# del fruits[0] -->> cannot del item
del fruits # -->> can because del entire tuple

# since tuple has less methods, obv :
# 1) take less memory
# 2) faster than list
# when do data processing, we will convert the list to a tuple

# auto explode -->> feature which lists and tuple has

fruits = ["apple", "orange", "mango"]
f1 = fruits[0]
f2 = fruits[1]
f3 = fruits[2]
print(f1, f2, f3)


