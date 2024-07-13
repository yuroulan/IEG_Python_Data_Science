# assign multiple values to multiple variables 

fruit = "apple"
fruit01, fruit02 = "apple" , "orange"

fruits = ["apple", "orange", "mango", "banana", "grapes"]

# indexing and selection
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# items in the list = 5  (max item)
# use fx len for how many items in the list
print(len(fruits))

# index in the list = 4  (max index)
print(len(fruits) - 1)

# negative index
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])

# max index for (-) is (-5) same as number of item

# pull out orang, mango, banana

# range 
# start_index:end_index  
# start index -->> included
# end index -->> not included
# also called as slicing

print(fruits[1:3]) # 3 is excluded
print(fruits[1:4])
print(fruits[:4]) # start index not mention, will start from zero (index)
print(fruits[0:]) # end index not mentioned, will go until last item
print(fruits[:])
print('-' * 100)

# the range also have 3rd argument, step up argument
# passing 3rd argument to the range

fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]
print(fruits[0:8])
print(fruits[0:8:2])
print(fruits[0:8:3])
print('-' * 100)

# start index must be less than end index
print(fruits[-5:-1])
print(fruits[-1:-5])  # empty list, default step up value is 1 
print(fruits[-1:-5:-1]) # reverse order

print(fruits[::-1]) # reverse all













