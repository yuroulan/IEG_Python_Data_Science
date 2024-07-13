'''# in every class that will be many properties 
# and very few properties are common to all the objects
# good to keep this properties at the class level 
# rather than keep at the object (instance) level

class participants:
    batch = 2024 # -->> not local bcause it is outside method inside class (class var)
    # assume participants are goint ot take one particular program
    # called python data science
    # class var are inside the class but outside the method
    # class var destroyed when the class is destroy
    # to access class var, use class as prefix
    course = "Python Data Science" # -->> local var
    # def __init__(self, firstName, lastName):
    #     # the properties that created ta the object level
    #     # every obj being created will allocate space
    #     # to keep these value
    #     self.firstName = firstName
    #     self.lastName = lastName
        # count = 1
        # print(self.firstName, self.lastName, count)
        # inside method canhave 2 types of var:
        # 1. instance var prefix with (self)
        #   - instance var live until the object is destroy
        # 2. local var not prefix with the word (self)
        #   - local var will die after the method execution
        #   - created inside the method

    def __init__(self, firstName, lastName):
        # the properties that created ta the object level
        # every obj being created will allocate space
        # to keep these value
        self.firstName = firstName
        self.lastName = lastName
        # count = 1
        salutation = "Mr." # -->> local var
        self.firstname = salutation +" "+ self.firstName

    def getFullName(self): 
        print("Name : ", self.firstName, self.lastName)
        print(f"Hello, {self.firstname} {self.lastName}")

khairi = participants("Khairi", "Abu Bakar")
khairi.getFullName()
# khairi = salutation.() -->> cannot/ not right
# del khairi # -->> destroy khairi

# to access instance var must prefix with obj
# print(khairi.firstName)

# to access class var must prefix with class
print("Your Course is :", participants.course)

# print(participants.batch)

# 1. class
# 2. constructor -->> def __init__(self)
# 3. method
# 4. properties :
# - local var 
# - instance var -->> owned by instance of class, instance var are diff for each object
# - class var -->> instance var defined within methods
# 5. objects(instance of participants class) -->> Khairi = apa2

instance method -->> __init__(self)
class method -->> 
'''
# basic Object-Oriented Programming

























