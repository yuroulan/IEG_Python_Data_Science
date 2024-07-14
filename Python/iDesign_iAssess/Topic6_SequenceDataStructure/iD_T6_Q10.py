# Problem 10
'''
Word Count
Harry studies in HNJ school and his medium of instruction is English. 
His English teacher taught him to form sentences. 
Harry loves Mathematics as well. He wants to link Mathematics with English. 
As a first step, he wishes to count the number of occurrences of words in a sentence.

Develop a python program to help Harry to finish the task.

Input Format:

Read a sentence from the user

Output Format:

Display the number of occurrences of words in the sentence. 

Refer sample output.

Sample Input 1:

the the function using dict dict

Sample Output 1:

{'the': 2, 'function': 1, 'using': 1, 'dict': 2}
'''

sentences = input()

words = sentences.split()

wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print(wordCount)

# iassess

# 1

inp1 = input().split(',')
inp2 = input().split(',')

set1 = set(map(int, inp1))
set2 = set(map(int, inp2))

# to check if set1 is a subset of set2
isSet1 = set1.issubset(set2)
print(isSet1)

# to check if set2 is subset of set1
isSet2 = set2.issubset(set1)
print(isSet2)

# to check set1 is superset of set 2
isSet1 = set1.issuperset(set2)
print(isSet1)

# to check set2 is superset of set1
isSet2 = set2.issuperset(set1)
print(isSet2)

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