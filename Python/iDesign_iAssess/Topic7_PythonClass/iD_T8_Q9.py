# Problem 9
'''
College Details (Overloading)
Write a program to illustrate Method Overloading in Python for the following College class.

 

Create a class named College.

There are no attributes in this class.

 
Invoke the __str__() function two times with different different arguments to implement function overloading, as below:

1.  __str__(). print the College Id,College name ,city,state,pincode of a particular College.
2.  __str__(). print the College name, contactNumber and emailId of a particular College.

Input and Output Format:

Refer sample input and output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.


Sample Input and Output:

1. Enter College address and Display
2. Enter  the contact details and Display
3. exit
Enter your choice
1
Enter the College id
Bit01
Enter the College name
Bit Meshra
Enter the City
Ranchi
Enter the State
Jharkhand
Enter the Pincode
822101
id : Bit01,Name : Bit Meshra,City : Ranchi,State : Jharkhand,Pincode : 822101

Enter your choice
2
Enter the name of the College
Nit jamshedpur
Enter the contact number
9876543210
Enter the email id
nit@ideal.in
Name : Nit jamshedpur,Contact Number : 9876543210,Email : nit@ideal.in

Enter your choice
3
'''

class College:
    def __init__(self, collId=None, collName=None, city=None, state=None, pincode=None, contactNum=None, email=None):
        self.collId = collId
        self.collName = collName
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNum = contactNum
        self.email = email
    
    def __str__(self):
        if self.collId and self.city and self.state and self.pincode:
            return f"id : {self.collId}\nName : {self.collName}\nCity : {self.city}\nState : {self.state}\nPincode : {self.pincode}\n"
        elif self.contactNum and self.email:
            return f"Name : {self.collName}\nContact Number : {contactNum}\nEmail : {email}\n"
        else:
            return "No details"
        
print("1. Enter College address and Display\n\
2. Enter  the contact details and Display\n\
3. exit")

while True: 
    userOption = int(input("Enter your choice"))

    if userOption == 1:
        collId = input("Enter the College id\n")
        collName = input("Enter the College name\n")
        city = input("Enter the City\n")
        state = input("Enter the State\n")
        pincode = input("Enter the Pincode\n")
        d1 = College(collId=collId, collName=collName, city=city, state=state, pincode=pincode)
        print(d1)

    elif userOption == 2:
        collName = input("Enter the name of the College\n")
        contactNum = input("Enter the contact number\n")
        email = input("Enter the email id\n")
        d2 = College(collName=collName, contactNum=contactNum, email=email)
        print(d2)

    elif userOption == 3:
        break

    else:
        print("Invalid Choice")