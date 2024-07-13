# looping statements
# for - to iterate over the sequence types (go thru one by one) 
# while - a general looping logics

# 1. for loop

# range - generate sequences -->> range(start, end, stepsize)
# start included, end excluded stepsize is jumpsize

# exp -->> range(10, 20, 2) 

# to print multiple of 5 between 50 t0 100
# range(50, 101, 5) -->> 50 55 60 65 70 75 80 85 90 95 100 

# to print multiple of 5 but negative from 100 to 75
# range(100, 74, -5) -->> 100 95 90 85 80 75

for i in range(100, 74, -5):        # 100 95 90 85 80 75
    print(i)
print('-' * 50)

for i in range(100, 75, -5):        # 100 95 85 80
    print(i)
print('-' * 50)

for i in range(100, 80, -5):        # 100 95 90 85
    print(i)
print('-' * 50)

# to increment stepsize to 1 
# range(50, 60, 1) or range(50, 60)

for i in range(50, 60, 1):          # 50 51 52 53 54 55 56 57 58 59
    print(i, end=" ")
print()
print('-' * 50)

for i in range(50, 60, 2):          # 50 52 54 56 58
    print(i, end=" ")
print()
print('-' * 50)

for i in range(50, 60):             # 50 51 52 53 54 55 56 57 58 59
    print(i, end=" ")
print()
print('-' * 50)

# range(end)
# to pull out value before n in range(n)

for i in range(5):                  # 0 1 2 3 4 
    print(i)
print('-' * 50)

#-------------------------------------------------------------------#

'''
    0       1       2       3       4
0  0.0     0.1     0.2     0.3     0.4
1  1.0     1.1     1.2     1.3     1.4
2  2.0     2.1     2.2     2.3     2.4
3  3.0     3.1     3.2     3.3     3.4
'''

# to represent the above in for loop

r = 4
c = 5

for i in range(r):                  # 0 1 2 3 
    for j in range(c):              # 0 1 2 3 4
        print(i, j, sep=".", end=" ")
    print()

'''
4           # r = 4, c = 4

0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3

5           # r = 5, c = 5

0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''

# to print the above

n = int(input("Enter n : "))

for i in range(n):                  # 0 1 2 3 ... n
    for j in range(n):              # 0 1 2 3 ... n
        print(j, end=" ")
    print()
print('-' * 50)

'''
5

1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5
'''

# to print the above

n = int(input("Enter n : "))

for i in range(1, n + 1):           # 1 2 3 4 5
    for j in range(1, i + 1):       # 1 # 1 2 # 1 2 3 and etc.
        print(j, end=" ")
    print()
print('-' * 50)
'''
7
    0   1   2   3   4   5   6
  0 *   #   #   #   #   #   *
  1 #   *   #   #   #   *   #
  2 #   #   *   #   *   #   #
  3 #   #   #   *   #   #   #
  4 #   #   *   #   *   #   #
  5 #   *   #   #   #   *   #
  6 *   #   #   #   #   #   *
'''

# to print the above
# i + j = n - 1

n = int(input("Enter n : "))

for i in range(n):
    for j in range(n):
        if(i == j or i + j == n - 1):
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
print('-' * 50)

'''
7

* # # # # # *
$ * # # # * $
$ $ * # * $ $
$ $ $ * $ $ $
$ $ * # * $ $
$ * # # # * $
* # # # # # *
'''
# i + j == n - 1
# to print the above

n = int(input("Enter n : "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        elif i < j and i + j < n - 1:
            print("#", end=" ")
        elif i > j and i + j > n - 1:
            print("#", end=" ")
        else:
            print("$", end=" ")
    print()

'''
6

*
* *
* * *
* * * *
* * * * *
* * * * * *
'''

# to print the above

n = int(input("Enter n : "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
print('-' * 50)

'''
6

# # # # # #
# # # # #
# # # #
# # #
# #
#
'''
# to print the above

for i in range(n):
    for j in range(n - i):
        print("#", end=" ")
    print()
print('-' * 50)

'''
6

* # # # # # #
* * # # # # #
* * * # # # #
* * * * # # #
* * * * * # #
* * * * * * #

'''

# to print the above
# first way

n = int(input("Enter any value to print symbols : "))

for i in range(n):
    for j in range(n):
        if(j <= i):                
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
print('-' * 50)

# sec way

n = int(input("anything : "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(n - i):
        print("#", end=" ")
    print()
    
#-------------------------------------------------------------------#

'''
South Africa flag

green -->> *
black -->> -
red -->> #
blue -->> $

7

* # # # # # #
- * # # # # #
- - * # # # #
- - - * * * *
- - * $ $ $ $
- * $ $ $ $ $
* $ $ $ $ $ $

'''
# to print the above

#-------------------------------------------------------------------#

# while loop
# I - initialization
# C - condition
# U - updation

# find the sum of the digits of given integer
'''
given = 1234        # prompt
sum = 0             # initialization

# expression to be repeated until given number

d = n%10 = 1234%10 = 4
s = s + rem     # s += d
n = n//10   # 123

n = 123
d = 3
s = 7             # 4 + 3 = 7

n = 12
d = 2
s = 9             # 7 + 2 = 9

n = 1
d = 1
s = 10            # 9 + 1 = 10

total = 1 + 2 + 3 + 4 == 10

'''

n = int(input("Enter any value : "))    # I # 1234
s = 0

while n != 0:   # C
    d = n % 10  # to get remainder
    s += d      # 0 + remainder
    n //= 10    # U 

print("sum = ", s)          # sum = 10
print('-' * 50)

# to use for loop

n = 6

for i in range(n):      # 0 1 2 3 4 5
    if(i == 4):
        break
    print(i)            # 0 1 2 3
else:
    print("inside else, reached 4")     # is not executed because  i == 4 is True
print('-' * 50)

n = 6

for i in range(n): # 0 1 2 3 4 5
    print(i)            
else:
    print("inside else, reached end of for loop.") # if 6
print('-' * 50)

# while loop for above

n = 6
i = 0
while i<n:      # 0 1 2 3 4 5
    print(i)
    i += 1
print("outside loop", i)        # for 6
print('-' * 50)

#-------------------------------------------------------------------#

# prime number :
# natural numbers
# 2 divisors

# composite :
# - natural number
# - more than 2 factors

'''
7
2 3 4 5 6

15
2 3 4 5 6 7 8 9 10 11 12 13 14

'''

n = int(input())
for i in range(2, n):
    if(n % i == 0):
        print("Composite.")
        break
else:
    print("Prime.")
print('-' * 50)

n = int(input())
for i in range(2, n):
    if(n % i == 0):
        flag = 1
        print("Composite.")
        break
if(flag == 0):
    print("Prime.")

















































