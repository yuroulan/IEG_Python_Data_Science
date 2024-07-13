'''
fx is 2 things:
    1) parameter
    2) return
'''
# how to return a function
# fx can have inner fx -->> can be called from the outer fx
# cannot call fx inner fx from main context
def authenticate(username, password):
    def simpleInterest(principle, period, rate):
        def something():
            pass
        return (principle * period * rate)
    if(username == "admin" and password == "pwd123"):
        #print("Interest amount : ", simpleInterest(1000, 1, 6))
        return simpleInterest   # returning the adress location where simpleInterest fx is

def sum(a, b):
    return a + b

# authentication fx will get bloated
# may come across few statements copied
# pasted it multiple times inside the fx
# good to convert those statements into inner fx

func = authenticate("admin", "pwd123")
print("Interest amount : ", func(1000, 1, 6))

# fx w/o name is also called anonynomous fx
# if fx dont have name, we cant call / invoke them
# based on diagram, can we write fx as :

# simpleInterest() -->> cannot be called outside of the fx (from main context)
# still can call if outer fx returns the inner fx

'''# lambda fx -->> execute to main context itself (generally for any other language too)

add = (a, b) => {
    return a + b
}
'''
'''
# this is cannot
sum = def(a, b):
        return a + b
'''

# functional Programming
# 1) passing fx as an args
# 2) creating inner fx
# 3) returning inner fx from outer fx
# 4) fx executed in the main context
# 5) closures

x = 10
def sayX():
    print(x)

sayX()

# however py still have lambda fx but only can have one stmnts
def add(x, y):
    return x + y
# step 1 : convert fx into anonynomous fx
    # fx without name
'''def (x, y): return x + y'''

# Step 2 : we cannot call the no name or anonynomous fx 
# assign fx to vsariable
'''sum = def(x, Y): return x + y'''

# Step 3 : rename def with lambda
'''sum = lambda(x, Y) : return x + y'''

#Step 4 : parenthesis "()" and "return" keyword not necessary
sum = lambda x, y :  x + y   # sum is a variable
print(sum(10, 20))

prices = [10, 20, 30, 40, 50]
pricewithsst = []
for price in prices:
    pricewithsst.append(price + (price * 0.06))
print("copy using for loop:", pricewithsst)

pricewithsst = map(lambda value : (price + (price * 0.06)), prices)
print(list(pricewithsst))















