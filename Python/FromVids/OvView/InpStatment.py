
'''
# This is the data we give to the machines
age = 25
print(age)
print(type(age))

name = "JK"
print(name)
print(type(name))

age = "twenty five"
print(age)
print(type(age))
'''

# This is when user can put their data (input)

age = int(input("Please put your age : "))
print(age)
print(type(age))              

print('-' * 50)

# to give classes

'''
input = 23 34 45
a = 23
b = 34
c = 45
'''

a = input()
al = a.split(" ")
print(a)
print(al)

# using map

a = input()
al = a.split(" ")
print(a)
print(al)
e, f, g = map(int, al)
print(e, f, g)
print(type(e))

input().split(" ")
map(int, input().split(" "))
e, f, g = map(int, input().split(" "))

print('-' * 50)

# format specifier

'''
int - %d
float - %f
str - %s
'''

a = 12.3445
b = 123
c = "hi"
print("%f"%a)   # 12.34500
print("%.2f"%a) # 12.34
print("%d - %.3f : %s"%(b,a,c))

print('-' * 50)