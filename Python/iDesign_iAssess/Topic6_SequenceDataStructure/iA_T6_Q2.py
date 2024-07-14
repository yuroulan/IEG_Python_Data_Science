# 2
class Client:
    def __init__(self, name, email, passportNum):
        self.name = name
        self.email = email
        self.passportNum = passportNum

    def __str__(self):
        return f"{self.name}--{self.email}--{self.passportNum}"

inp = int(input("Enter the number of clients"))
clients = {}

for i in range(1, inp + 1):
    print(f"Enter the details of the client {i}")
    name = input().strip()
    email = input().strip()  # Ensure to input the email correctly
    passportNum = input().strip()
    clients[passportNum] = Client(name, email, passportNum)

passNum = input("Enter the passport number of the client to be searched")

if passNum in clients:
    print("Client Details")
    print(clients[passNum])
else:
    print("Client not found")