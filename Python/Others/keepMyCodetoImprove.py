class BankAccount:
    def __init__(self, accountNumber, customerName, dateOfOpening, openingBalance):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.openingBalance = openingBalance
        self.currentBalance = ""
        self.dateOfOpening = dateOfOpening
        

    def __str__(self):
        print("CUSTOMER BANK ACCOUNT DETAILS")
        print('-' * 50)
        return (f"Customer Account Number : {self.accountNumber}\n"
                f"Customer Name : {self.customerName}\n"
                f"Date of Opening : {self.dateOfOpening}\n"
                f"Opening Balance : {self.openingBalance}\n"
                f"Current Balance : RM {self.currentBalance}")
    

    def deposit(self, currentBalance, depoAmount):
        print(f"Your current balance now : RM{self.currentBalance}\n")
        if depoAmount > 0:
            self.currentBalance += depoAmount
            print(f"RM {depoAmount} is successfully deposited into your account.\n\
Your Current Balance : RM {self.currentBalance}\n")
        else:
            print(f"Current Balance : RM{self.currentBalance}")

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= self.currentBalance:
            self.currentBalance -= withdrawAmount
            print(f"RM {withdrawAmount} withdrew from your account.\n\
Your Current Balance : RM {self.currentBalance}\n")
        else:
            print("Insufficient Balance.")
        
    def checkBalance(self):
        return self.currentBalance
    
custBankInfo = [
    BankAccount("10115-1011-05-27850", "Siti Mahirah", "2018-03-20", 1800),
    BankAccount("10115-1012-05-27869", "Ahmad Hamid", "2020-05-03", 2100),
]
for info in custBankInfo:
    print(custBankInfo)

While True:
    print("WELCOME TO HONOUR BANK BERHAD.\n\
PLEASE CHOOSE YOUR OPTION\n\
0 - EXIT\n\
1 - ACCOUNT DETAILS\n\
2 - CHECK CURRENT BALANCE\n\
3 - INSERT DEPOSIT\n\
4 - WITHDRAW")