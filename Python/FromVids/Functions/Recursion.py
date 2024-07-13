# Recursion

'''
# function never call itself. so
Recursion - a function calling (a copy) itself

code looks simple

def fun(args):
    if(base/exit condition):
        * can have stmnts
        return
    return recursive call(s) # if dont have return, fx will go None

- factorial 

n! = n * n(n-1)!

5! = 5*4*3*2*1  5 * 4!
4! = 4*3*2*1    = 4 * 3!
3! = 3*2*1  = 3 * 2!
2! = 2*1    = 2 * 1!
1! = 1  -->> base case

0! = 1
'''

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n*fact(n-1)

n = int(input())
f = fact(n)
print(f)

'''
- fibonacci

0 1 1 2 3 5 8 13 21...
0 1 2 3 4 5 6 ...

n == 0 0
n == 1 1
f(n) = f(n-1) + f(n-2)
'''
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 0 or n == 1: return n


def fib(n):
    if(n == 0 or n == 1):
        return n
    return fib(n-1) * fib(n-2)

n = int(input())
print(fib(n))

'''
combination
nCr = n! / r!* (n-r)!
nCr = (n-1)Cr + (n-1)C(r-1)

6C4 = 5C4 + 5C3
15 = 5 + 10

nCn = 1 -->> always 1
nC1 = n
nC0 = 1
'''

def comb(n,r):
    if(r == n or r == 0): return 1
    if(r == 1): return 1
    return comb(n-1, r) + comb(n-1, r-1)
    
n = int(input())
r = int(input())

print(comb(n,r))








