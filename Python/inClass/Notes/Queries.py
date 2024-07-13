# any / all
'''
take boolean list as parameter
[True, True, True, False, True, False, False]

# any -->> will return True (Any == or)
All -->> will return False  (All == and)
        - require everything to be true

'''
givenNum = 11
divisors = range (2, givenNum)

if (len([myNum for myNum in divisors if givenNum % myNum == 0])):
    print("Prime NUmber")
else:
    print("Not Prime Number")
''
if any ([givenNum % myNum == 0 for myNum in divisors]):   # -->> Will return True
    print ("Prime number")
else:
    print ("Not a prime number")
