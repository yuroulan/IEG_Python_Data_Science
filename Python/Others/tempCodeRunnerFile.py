
    def __init__(self):
        self.strFromUsers = input("Enter any words : ")
    def getStr(self):
        return self.strFromUsers
    def printStr(self):
        print(f"String from user : ", self.strFromUsers)

strInpUser = userStr()
strInpUser.printStr()
