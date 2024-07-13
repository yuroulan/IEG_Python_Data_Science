# multiple inheritence

class card:
    def __init__(self):
        pass

    def doSomething(self):
        print("Inside Card class")

class atmCard(card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside ATM Card Class")

class creditCard(card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside Credit Card Class")

class debitCard(card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside Debit Card Class")


class bankCard(atmCard, creditCard, debitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside Bank Card Class")
        super().doSomething()

# we have cerated 5 classess
# in all 5 classess we have doSomething method
# it is implemented (got code inside which is print())

# lets create instance for the last card

bankCard = bankCard()
bankCard.doSomething()

# now remove print statement from bankCard.doSomething
# replace with super().doSomething

# comment doSomething method which is inside the ATM card Class
# comment doSomething method which is inside the Credit card Class
# comment doSomething method which is inside the Debit card Class

# python scan from left to right
# and identify the base classes and call the method accordingly
# also called as method resolution order (MRO)

#print(bankCard.__mro__)

# every class created in python is inherited from a class called obj

# class object:
#   def __init__(self):
#       pass
#   def __str__(self):
#       print(memory address)

class objects:
    pass
    #def __str__(self):
      #return "address"

class range(objects):
    pass

myRange = range()
print(myRange)

# what if idw my class to inherit from the base class called object
# bcause you will lose all of the default feature of a class

class myClass:
    pass

# myClass().will list more method
# those methods from the base class called obj
# dont want class to be inherited

class noObjClass():
    pass

test = noObjClass()
print(test)
















