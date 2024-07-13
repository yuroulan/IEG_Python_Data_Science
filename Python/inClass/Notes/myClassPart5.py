# is-a relationship, inheration
# working on child

# making parents as parent in the child class
# 1) when create child obj, parent obj is created automatically
# 2) to initialize parent obj inside child obj, call init method using super() from init method of child

class student:  # parent, 1
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.icNum = 99101810

# alumni extends student class
class alumni(student):   # is-a student , child, 2
    
    def __init__(self, firstName, lastName, alumniNum):
        student.__init__(self, firstName, lastName) # -->> create instance of the parents
        pass                                        # -->> static calling
        # can use keyword 
        super().__init__(firstName, lastName)   # calling init method of parents, return obj of parent
        self.alumniNum = alumniNum


    def __str__(self):
        return f"First Name : {self.firstName}\n\
Last Name : {self.lastName}\n\
Ic NUmber : {self.icNum}\n\
Alumni Number : {self.alumniNum}"
    

# create obj of alumni class, only child obj
alumni = alumni("Parker", "Peter", 968835)
print(alumni)












#student("Anati", "Mahirah")
