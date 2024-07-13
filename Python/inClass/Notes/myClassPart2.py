
class student:

# init method is used to declare properties
# diff between the vars and properties:
# 1) prop are nothing but vars inside the class
# 2) prop always prefix by 1st para
# 3) if not declare with prefix, will bwcome just a vars inside the methods
# some of the props is just a compulsory
# cannot become a student w/o telling fname, lname, icnum
# the prog can be provided later
# should not allow object to be created w/o compulsory of props
# must take comp vals as para at the constructer 
# take parameter to assigned at properties
    def __init__(self, firstName, lastName, icNum):
        self.firstName = firstName
        self.lastName = lastName
        self.icNum = icNum
        self.program = ""
        self.address = ""    
    
    def attendClass(self):
        print(f"{self.firstName} {self.lastName} started attending class")
    
    def doProject(self, projectName):
        print(f"{self.firstName} {self.lastName} started doing the project : ", projectName)

    def attendExam(self, exam):
        grade = "A"
        return f"{self.firstName} {self.lastName} has attended the exam : {exam} and obtained the score {grade}"

    def info(self):
        print("First Name : ", self.firstName)
        print("Last Name : ", self.lastName)
        print("IC Number : ", self.icNum)
        
        # prog is a local var created isnide the method
        for program in self.program:
            print("Program: ", self.program)
            print("Address : ")
            print(self.address("Street"))
            print(self.address("Area"))
            print(self.address("Posscode"))
            print(self.address("State"))
            print(self.address("Country"))

    '''def __str__(self):
        print("IC Number : ", self.icNum)
        # prog is a local var created isnide the method
        for program in self.program:
            print("Program: ", self.program)
            print("Address : ")
            print(self.address("Street"))
            print(self.address("Area"))
            print(self.address("Posscode"))
            print(self.address("State"))
            print(self.address("Country"))'''

# how can we set val for the prop
# 1) using constructir -->> __inti__method
zul = student("Ahmad", "Zul", 980102121234)
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))
# How can i access the props of an object
# 2) can set val to prop using dot operator
zul.program = ["Python", "Data Science", "Machine Learning"]
zul.address = {
    "Street": "15, jalan SS2",
    "Area": "Subang Jaya 2",
    "Posscode": 43100,
    "State": "Selangor",
    "Country": "Malaysia"
}
zul.info()
print(zul)












