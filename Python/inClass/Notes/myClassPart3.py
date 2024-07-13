# encapsulation

'''
inside class, property. want to encapsulate them

-->> to encapsulate the properties inside the class

private, public, protected <<-- keywords for protect the properties
'''

# need to identify all the properties in the class, 
# but we cannot do that

'''
class circle:
    def __init__(self, radius):
        # change the properties --> using single underscore or __ double
        self._radius = 0 # -->> this will make the properties private
        if(isinstance(radius, int)):
            self._radius = radius # radius is parameter
        else:
            print("Invalid Radius")
    def area(self):
        return 3.14 * self._radius * self._radius
    def circum(self):
        return 2 * 3.14 * self._radius

    def __str__(self):
        return f"Radius of this circle is {self._radius}"
    
myCircle = circle(20)
print("1" , myCircle)
#myCircle = circle("abc")
#print("2", myCircle)
myCircle.radius = 30 # directly assigned, no way to -->> need to protect it from being access because we want only int
print("3", myCircle)
print("4", myCircle.area())
'''

# to ensure the value set to properties is tally
# must always get executed
# how:
# 1) change the properties 
# 2) introduce secretary -->> getter method, setter method

class circle:
    def __init__(self, radius):
        # change the properties --> using single underscore or double underscore (in latest ver.)
        self._radius = 0 # -->> will make the properties private by putting underscore
        if(isinstance(radius, int)): # -->> fx returns True if the spec. obj. is of the spec. type, otherwise False
            self._radius = radius # radius is parameter
        else:
            print("Invalid Radius")

    # getter method and setter method -->> after private, want to access back the private one
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        if(isinstance(radius, int)):
            self._radius = radius
        else:
            print("Invalid Radius")

    def area(self):
        return 3.14 * self._radius * self._radius
    
    def circum(self):
        return 2 * 3.14 * self._radius

    def __str__(self):
        return f"Radius of this circle is {self._radius}"
    
    # property is a class
    # calling/invoking the class by passing the method as args
    # getRadius has no ()
    # property class retuen property objects which assign to vars of radius
    # radius is an instance of property class
    radius = property(getRadius, setRadius)
    
myCircle = circle(20)
print("1" , myCircle)

myCircle = circle("abc")
print("2", myCircle)

myCircle.__radius = 30
print("3", myCircle)


myCircle.__radius ="abc" # directly assigned, no way to -->> need to protect it from being access because we want only int
print("4", myCircle)

myCircle.radius = 30
print("5", myCircle)

myCircle.radius = "abc"
print("6", myCircle)

print("7", myCircle.area())




















