'''
Object Oreiented Programming

object -->> instance of class

class -->> blueprint
- define how obj looks like (properties)
-- characteristics / data member / state
-- functionality / member function / behaviour

self - to pointing the specific object

'''
class Person:
    def __init__(self, age, gender, height, weight):    # constructor
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

p1 = Person(25, 'M', 178, 82)
print(p1)