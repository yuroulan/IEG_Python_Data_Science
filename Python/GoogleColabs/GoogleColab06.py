# Problem 1
'''
Write a python function that takes a number as parameter and 
prints the multiplication table of that number
'''

num = range(1, 13)

def mult(num, userMulInp):
    for mul in num:
        result = mul * userMulInp
        print(f"{mul} x {userMulInp} = ", result)

userMulInp = int(input('Enter any number to form a multiplication table : '))
mult(num, userMulInp)

# Problem 2
'''
Write a simple python function that returns twin primes less than 1000. 
If two consecutive odd numbers are both prime then they are known as twin primes.

Pairs of primes that differ by 2. 
For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 are twin primes.
'''

# to print twin primes which when added by 2, it will form next prime number.
# example, 3 + 2 = 7, print(3 and 7)
# limit less than 1000

# to find prime number under 1000
def prime(limit):
    primes = [] # 2,3,5,7,11 ... 997
    for i in range(2, limit):
        primeNum = True
        for divisor in range(2, i):
            if(i % divisor == 0):
                primeNum = False
                break
        if primeNum:
            primes.append(i)
    return primes

def primeTwin(limit):
    primes = prime(limit)
    for i in range(len(primes)-1):
        prime1st = primes[i]
        prime2nd = primes[i + 1]
        if(prime2nd - prime1st ==2):
            print(f"{prime1st} and {prime2nd}")
        
primeTwin(1000)

# Problem 3
'''
Write a simple python function that takes a number as parameter and 
returns the prime factors of that number. Prime Factorization is finding 
which prime numbers multiply together to make the original number.

Example: prime factors of 56 - 2, 2, 2, 7
'''
# let say user input is 56
# i want to let the value be divided by 2 and make sure its equal to zero
# then if its not equal to zero, will divide to next odd number which is , 3, 5, 7 and etc...

# to factorized input number
def div(divNum):    # empty list to store prime factors
    divFact = []    
    while divNum % 2 == 0:  # to check if it can be divided by 2 or not
        divFact.append(2)   # if yes, it will append into empty list
        divNum //= 2    # process will repeat until cannot be divided by 2

    factors = 3 # to check odd prime factors 
    while divNum != 1:  # as long as not equal to 1, the loop will continue
        while divNum % factors == 0:    # will check if it can be divided by current factors
            divFact.append(factors)
            divNum //= factors 
        factors += 2    # add two to get next odd number
    
    return divFact

userInp = int(input("Enter number to return the prime numbers : "))
print(f"The prime factors of {userInp} is : ", div(userInp))

# Problem 4
'''
Write a function that inputs a number and returns the product of digits of that number.
'''
# to multiple each digit of the input number
# let say, input number, 432 -->> 4 x 3 x 2 = 24

def prodNum(x):
    strx = str(x)
    product = 1
    for i in range(len(strx)):
        product *= int(strx[i])
    return product
    
prodInp = int(input("Enter a number to returns the product of digits of the number : "))
print(f"The products of digits for {prodInp} is : {prodNum(prodInp)}")

# Problem 5
'''
Write a function that takes a number as parameter. 
The function finds the proper divisors of that number and 
then finds the sum of proper divisors. Proper divisors of a number are those 
numbers by which the number is divisible, except the number itself.

For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
'''
# to find a proper divisors of a given number
# to calculate the sum of these proper divisors
# let say user input = 36 -->> 1, 2, 3, 4, 6, 9, 12 and 18

# let say user input is 20 -->> supposed to be 1, 2, 4, 5, 10

def PropDiv(userInp):
    sumNum = 0
    sumList = []
    for i in range(1, userInp):
        if(userInp % i == 0):
            sumNum = sumNum + i
            sumList.append(i)
    print(f"The list of proper divisors for {userInp} is : ", sumList)
    return sumNum

userInp = int(input("Enter any number to finds the sum of proper divisors of that number : "))
print(f"The sum of proper divisors of {userInp} is : {PropDiv(userInp)}")

# Problem 6
'''
A number is called perfect if the sum of proper divisors of that number is equal to the number. 
For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect 
numbers in a given range.
'''
# 1st way

def propDiv(userInp):
    sumNum = 0
    sumList = []
    for i in range(1, userInp):
        if(userInp % i == 0):
            sumNum = sumNum + i
            sumList.append(i)
    if(sumNum == userInp):
        return True
    else:
        return False

def perfNumGen(maxInp):
    perfNumList = []
    num = 2
    while len(perfNumList) < maxInp:
        if(propDiv(num)):
            perfNumList.append(num)
        num += 1
    for perf in perfNumList:
        print(perf)


userInp = int(input("Enter the maximum number to generate perfect number (max 4): "))
if(userInp > 4):
   print("Cannot exceed 4. Please enter value lower than 4.")
else:
    perfNumGen(userInp)
    
# 2nd way

def prime():
    num = 30
    primePrime = []
    for i in range(2, num):
        isPrime = True
        for div in range(2, i):
            if(i % div == 0):
                isPrime = False
                break
        if(isPrime == True):
            primePrime.append(i)
    return primePrime

# to generate perfect numbers
# using math formula

def perfNum(perfMax):
    primePrime = prime()
    perfNumNum = []
    count = 0

    for num in primePrime:
        if(count >= perfMax):
            break
        q = 2 ** num - 1
        qPrime = True
        for divisor in range(2, q):
            if(q % divisor == 0):
                qPrime = False
                break
        if(qPrime == True):
            perfNum = q * 2 ** (num -1)
            perfNumNum.append(perfNum)
            count += 1
    for p in perfNumNum:
        print(p)

userInp = int(input("Enter the maximum range value to generate perfect numbers (max 7): "))
if(userInp > 7):
   print("Cannot exceed 7. Please enter a value lower than that.")
else:
    perfNum(userInp)

# Problem 7
'''
Write a python function that takes 2 parameters lower and upper (range). 
Let the function returns pairs of amicable numbers in that range.

Two different numbers are called amicable numbers if the sum of the 
proper divisors of each is equal to the other number. For example 220 and 284 are amicable numbers.

For example if we call that function: amicableNumbers(1, 1000)

The function must return: [220, 284]

Why they are amicable numbers ?

Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284

Sum of proper divisors of 284 = 1+2+4+71+142 = 220
'''
# to generate proper divisor
def PropDiv(userInp):
    sumNum = 0
    for i in range(1, userInp):
        if(userInp % i == 0):
            sumNum = sumNum + i
    return sumNum

def amicableNum(lower, upper):
    amicableList = []
    for i in range(lower, upper +1):
        sumPropDiv = PropDiv(i)
        if(sumPropDiv > i):
            sumPropDivDiv = PropDiv(sumPropDiv)
            if(sumPropDivDiv == i and sumPropDiv != sumPropDivDiv):
                amicableList.append(i)
                amicableList.append(sumPropDiv)
    return amicableList

print(amicableNum(1, 1000))

# Problem 8
'''
Write a python function that takes variable length parameters and 
returns maximum and minimum number in the parameter numbers.

For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)

The function must return: [10, 50]
'''
def maximumMinimum(*varLen):

    maxVal = max(varLen)    # max and min is a builtin fx
    minVal = min(varLen)

    return[minVal, maxVal]

fx = maximumMinimum(10, 20, 30, 40, 50) # tuple
print(fx)

# Problem 9
'''
Write a simple Python function that takes a number(n) as a parameter. 
Then the function prints out the first n rows of Pascal's triangle. 
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
'''
'''
1st - to generate this pattern
j   0   1   2   3   4   5
i
0   1   
1   1   1
2   1   2   1
3   1   3   3   1
4   1   4   6   4   1
5   1   5   10  10  5   1 
2nd - to shift the index of the digit at j (row)
row -->> shift j , use " " * n - i - 1, end=" "
         end = " " -->> will add space after a number
         to perform the triangle pattern
         when at row 1, n = input will minus with i and 1
         - let say, input = 5
            5 - 0 - 1 = 4
         so, " " * 4 will take index from 0 to 4 and '1' will appear at index 5
         - then, 5 - 1 - 1 = 3
         so, " " * 3 will take index from 0 to 3 and '1' will appear at index 4
j   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
i
0  " "  -   -   -   -   1
1  " "  -   -   -   1       1
2  " "  -   -   1       2       1   
3  " "  -   1       3       3       1
4  " "  1       4       6       6       4       1
5   1       5       10      12      10      5       1
column -->> remain the i
'''
def pasTri(n):
    a = []  # empty list for a
    for i in range(n):
        a.append([])
        for j in range(i + 1):
            if j == 0 or j == i:    # to make sure start and end of the row list is '1'
                a[i].append(1)
            else:
                a[i].append(a[i - 1][j] + a[i - 1][j - 1]) 
    return a
    
def pattern(a):
    n = len(a)  # calculates the number in rows
    for i in range(n):
        print(" " * (n - i - 1), end=" ")   # to make spaces
        for j in range(i + 1):
            print(a[i][j], end=" ")
        print()

n = int(input("Enter number, n : "))
triangle = pasTri(n)
pattern(triangle)

# Problem 10
'''
Write a simple python function that accepts a hyphen-separated sequence of words as parameter 
and returns the words in a hyphen-separated sequence after sorting them alphabetically.

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''
def hypSep(n):
    sepWord = n.split("-")
    sepWord.sort() 
    return "-".join(sepWord)


n = (input("Enter a hypen-separated sentences : "))
print(hypSep(n))