# only in py can access variable declare in the main context
x = 10
def sayX():
    print(x)    # usually x is initialized than then only used
    # in this case fx can see x 

sayX()  # 10

def modifyX():
    x = 20
    # whenever you modify the variable which in global context
    # the variable initialized locally
    # in this case x automatically become local variable
    print(x) # 20

modifyX()   # 20
print(x)    # 10

# what if i dont want to create x as local variable
# after call the fx, global variable changes value
def changeX():
    global x # variable x refer the main context -- x = 20
                # dont create x as local variable
    print(x)    # 10
    x = 20
    print(x)    # 20

changeX()   # 20
print(x)    # 20

# by using global keywords inside fx, fx able to change value of x
# which is in global context

def authenticate(): # outer fx
    result = 1111
    def simpleInterest():   # inner fx
        nonlocal result # strictly use this result declared in the outer fx
        result = 2222 # become local variable
        print(result)   # looking at variable in outer fx
    simpleInterest()
    print(result)

authenticate()
















