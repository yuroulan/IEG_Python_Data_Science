# first method

import myModule

print(myModule.add(10,20))
print(myModule.minus(20,10))
print(myModule.mul(20,10))
print(myModule.div(20,10))

print('-' * 50)

# second method
from myModule import add, minus, mul, div

print(add(10,20))
print(minus(20,10))
print(mul(20,10))
print(div(20,10))

print('-' * 50)

# third method

from myModule import *

print(add(10,20))
print(minus(20,10))
print(mul(20,10))
print(div(20,10))

print('-' * 50)


