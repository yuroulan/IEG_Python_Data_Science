'''
always one parent :

relationship, composition
is - a 
# single inheritence
# multi-level inheritence
# hierarchial inheritence

has - a 
'''
# has - a -->> become a property
# cust has-a passport




class passport: # parents, property of customer, 2
    def __init__(self, country, passportNum):
        self.country = country
        self.passportNum = passportNum

    def __str__(self):
        return f"Country : {self.country} \nPassport Number : {self.passportNum}"

class customer: # child, 1
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.icNum = ""
        self.passport = None

    def __str__(self):
        message = f"First Name : {self.firstName}\n"
        message = message + f"Last Name : {self.lastName}\n"
        message = message + f"IC Number : {self.icNum}\n"
        if(self.passport != None):
            message = message + f"{self.passport}"
        return message

# 1) create instance of parent obj
# 2) create instance of child obj
# 3) assign child object on the property in the parent object
peter = customer("Parker", "Peter")
passport = passport("United Kingdom", "E0202932")
peter.passport = passport

print(peter)

# convert python obj to dict
print(peter.__dict__)
