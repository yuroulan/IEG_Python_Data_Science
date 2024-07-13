# Given number is 76589
# Try to reverse the number
# Expected output = 98567

# Way 1
print('\n')
print("Mr.Jegan's Solution")
# givenNumber = 76589
# result = 0
# result = (result * 10) + (givenNumber % 10) = 9
# 1. givenNumber = givenNumber // 10 = 7658
# result = (result * 10) + (givenNumber % 10) = 98
# 2. givenNumber = givenNumber // 10 = 765
# result = (result * 10) + (givenNumber % 10) = 985
# 3. givenNumber = givenNumber // 10 = 76
# result = (result * 10) + (givenNumber % 10) = 9856
# 4. givenNumber = givenNumber // 10 = 7
# result = (result * 10) + (givenNumber % 10) = 98567

givenNumber = 76589
result = 0

print("The given number is :" , givenNumber)
result = (result * 10) + (givenNumber % 10)     # 9
print(result)

givenNumber = givenNumber // 10                 # givenNumber //= 10    #7658
print(givenNumber)
result = (result * 10) + (givenNumber % 10)     # 98
print(result)

givenNumber = givenNumber // 10
result = (result * 10) + (givenNumber % 10)     # 985
print(result)

givenNumber = givenNumber // 10
result = (result * 10) + (givenNumber % 10)     # 9856
print(result)

givenNumber = givenNumber // 10
result = (result * 10) + (givenNumber % 10)     # 98567
print(result)
print("-" * 50)

#-------------------------------------------------------------------#

# Irfan's Solution (1)

x = 76589
d = x // 10
r = x % 10

d1 = d // 10
r1 = d % 10

d2 = d1 // 10
r2 = d1 % 10

d3 = d2 // 10
r3 = d2 % 10

d4 = d3 // 10
r4 = d3 % 10

print(x)
print(d,r)
print(d1,r, r1)
print(d2,r,r1,r2)
print(d3,r,r1,r2,r3)
print(r,r1,r2,r3,r4)

# Irfan's Solution (2)

print('\n')
print("Irfan's Solution")
a0 = 76589 
result = 0 

a1 = a0 % 10 # 9 
a2 = a0 // 10 # 7658 
result = result * 10 + a1 # 9 
print('\n')
print(a1, a2, result)

a3 = a2 % 10 # 8
a4 = a2 // 10 # 765
result = result * 10 + a3 # 98
print(a3, a4, result)

a5 = a4 % 10 # 5
a6 = a4 // 10 # 76
result = result * 10 + a5 # 985
print(a5, a6, result)

a7 = a6 % 10 # 6
a8 = a6 // 10 # 7
result = result * 10 + a7 # 9856
print(a7, a8, result)

a9 = a8 % 10 # 7
a10 = a8 // 10 # 0
result = result * 10 + a9 # 98567
print( a9, a10, result)
print("Result :", result)
print('\n')

#-------------------------------------------------------------------#

# Akmal's Solution
print('\n')
print("Akmal's Solution")
x = 76589

reversed = (x % 10) * 10000                     # 9 * 1000 = 90000
reversed = ((x // 10) % 10) * 1000 + reversed   # 7658 8 8000 = 98000 
reversed = ((x // 100) % 10) * 100 + reversed
reversed = ((x // 1000) % 10) * 10 + reversed
reversed = (x // 10000) + reversed
 
print(reversed)


str_numbers = input()
str_numbers = str_numbers.split(",")
print(str_numbers)

numbers = [int(str_number) for str_number in str_numbers]
print(numbers)
numbers = map(int,str_numbers)
#print(list(numbers))

print(set(list(numbers)))

# list can have set inside
fruits = [{"apple", 10, 2.5}, {"orange", 10, 2.5}]
print("list when set inside", fruits)

# cannot have list inside set
fruits = {"apple", 10, 2.5, ("apple", "orange")}
print(fruits)

# fruits = {"apple", 10, 2.5, ["apple", "orange"]}
# print(fruits)

# to remove, change into set
nestedList = [
    [1,2,3],
    [3,4,5],
    [1,2,3]
]
nestedList = [tuple(item) for item in nestedList]
print(nestedList)
print(set(nestedList))

