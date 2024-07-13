# methods are noting but fx inside class
# methods take at least 1 parameter (self)
# use to pass instance

from typing import Any


class calculator:
    # this method take self as parameter (instance args)
    # want to access properties
    # also called as instance method
    def __init__(self, x, y): # -->> instance method
        self.x = x
        self.y = y
    
    def add(self): # -->> instance method
        return self.x + self.y
    def substract(self): # -->> instance method
        return self.x - self.y

mycalculator = calculator(10, 20) # -->> value capped in instance var
print(mycalculator.add())
print(abs(mycalculator.substract()))
    
# class that has many method, no properties
# dont take self as parameter anymore
# no need to create objects
# this method attached to the class not obj
# called class methods

# more easily done using module

class uitility:
    def add(x, y):
        return x + y
    def min(x, y):
        return x - y

print(uitility.add(10,20))

# some use cases, the class has properties but 1 or 2 methods inside class
# not require to access the properties
# those methods can be created w/o self parameter
# there are class method

# this one doesnt make sense

# instance method
class customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
# class method
# usually its a utility fx
    def getfullName(firstName, lastName):
        return firstName + lastName
# instance method
    def __str__(self):
       return customer.getfullName(self.firstName, self.lastName)

cust = customer("John", "Doe")
print(cust)






