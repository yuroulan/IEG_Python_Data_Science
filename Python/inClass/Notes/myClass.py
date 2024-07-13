'''principle = 1000
period = 1
rate = 6
simpleInterest = (principle * period * rate) / 100
print("Simple Interest = ", simpleInterest)'''

'''def calcultateSimpInt(principle, period, rate):
    simpleInterest = (principle * period * rate) / 100
    return simpleInterest

def calculateTotalAmntToPrint(principle, simpleInterest):
    return principle + simpleInterest

principle = 1000
period = 1
rate = 6
result = calcultateSimpInt(principle, period,rate)
newResult = calculateTotalAmntToPrint(principle, result)

print("Simple Interest = ", result)
print("Total amount to be paid = ", newResult)'''

# lets create a simple class
# class is a blueprint which contain vars and fx inside a class
# the vars inside the class is called properties
# the fx inside the class is called methods
class student:

# cannot declare a properties (variable) w/o assignning the value
# special method (function) called constructer

# method get called/invoke/executed everytime object of the class(instance) created

# get call everytime when we create object (instance) of this class
# since it is a special method it must have double "_" followed by init
# diff between method and fx
# 1) method - a fx inside a class
# 2) method have at least one parameter
# 3) no need to pass args for first parameter
# 4) 1st parameter of the method is special
# 5) value of the parameter is handled by python itself
# 6) usually parameter is called self

    def __init__(self):
        print("object is created")
    
    # 1st method/fx inside the stident class
    # method must have at least one parameter
    def attendClass(self):
        print("Object started attending class")
    
    def doProject(self, projectName):
        print("Object started doing the project : ", projectName)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam : {exam} and obtained the score {grade}"
# let us create first class
zul = student()

# how to invoke/call the method
# since the method has single parameter
# for 1st will be handle by python, dont need to pass
# pass args into 2nd parameters (projectName)
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))















