# Polymorphism

class gender:
    def __int__(self):
        pass
    def doCarryObjs(self):
        pass

class male(gender):
    def __int__(self):
        pass
    def doCarryObjs(self):
        print("Carry heavy objects")

class female(gender):
    def __int__(self):
        pass
    def doCarryObjs(self):
        print("Carry light objects")

def getGender(name):
    if "A/L" in name:
        return male()
    else:
        return female()
    
# python dinamically set the data type for the gender var
# sometimes it becomes male obj
# sometimes it becomes female obj

gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjs()
print(type(gender))

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjs()
print(type(gender))












