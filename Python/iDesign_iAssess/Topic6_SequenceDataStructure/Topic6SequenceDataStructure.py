# Problem 1
'''
Character Deletion in a String
Sita and Gita were no so good friends and had a fight while doing tasks 
o one of them decided to teach a lesson to other and deleted one of the 
characters from her name entered in the company’s database.
                
Input format:
First line of the Input is a string indicating the name.
Second line of the input is an integer ‘n’( a value less than the string length).
Output Format:
The output contains a string with a character being deleted at ‘nth’ index of the input.
Sample input 1:
Andrews
2
Sample output 1:
Adrews
Sample input 2:
Jack
4
Sample output 2:
Jac
'''
def toDelete(name, n):
    nameLength = len(name)
    # print(nameLength)

    if 1<= n <= nameLength:
        toDelete = n - 1
        result = name[:toDelete] + name[toDelete + 1:]
        return result
    else:
        return False

name = input()
n = int(input())

print(toDelete(name, n))

# Problem 2
'''
Print Palindrome

James and Jones had a discussion on palindrome strings. They were assigned to a task 
in which they had to check if the given string is a palindrome or not and 
if not they had to make it as a palindrome.
The condition for the task was as follows:
• Input and output strings should be case sensitive.
Help them with a program to make their task easier.

Input format:
Input consists of a string.
output format:
the output will be a palindrome string.
Sample Input:
Tamil
Sample Output
TamaT

Sample Input:
Amphi
Sample Output
AmpmA
'''
inp = input()   # let say user input is Tamil, its not a palindrome
                # so i need to change into palindrome such as TamaT

# to check palindrome
isPal = inp == inp[::-1]
print(isPal)    # -->> will return True / False

if not isPal:
    revInp = inp[::-1]
    pal = inp[:len(inp)//2] + revInp[len(inp)//2:]
else:
    pal = inp   # if the input already a palindrome

print(pal)

# Problem 3
'''
Pattern Printing

It was a fun week in Rita's college.Many competitions were organized for the students.
Rita was very interested in pattern printing competition. She was given an integer 
indicating a number of '\' or'/' she had to print in the given pattern. 

Though she was good in it she is finding it difficult to print the given pattern. 
Help Rita by writing a python code for the given input specifications.

/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\

Input and output format:
Input consists of an integer indicating a number of ‘/’ and ‘\’ Output 
consists of the pattern with specified number of backward and forward slashes.

All the texts in bold refer Input and rest refer output.
Sample Input:
5
Sample Output:
/////\\\\\/////\\\\\
/////\\\\\//////\\\\\
/////\\\\\/////\\\\\
/////\\\\\//////\\\\\
 
Sample Input:
10
Sample Output:
//////////\\\\\\\\\\//////////\\\\\\\\\\
//////////\\\\\\\\\\//////////\\\\\\\\\\
//////////\\\\\\\\\\//////////\\\\\\\\\\
//////////\\\\\\\\\\//////////\\\\\\\\\\
'''
inp = int(input())

# Constructing the pattern line with forward slashes, backslashes, and repeating it
pattern = "/" * inp + "\\" * inp + "/" * inp + "\\" * inp

# Printing the constructed pattern 'inp' times
print(pattern * 4)

# Problem 4
'''
Concatenation of Strings
Fun with “Strings” at Chicago technologies.
The official heads of chicago technologies thought only working would tire the 
employees so they arranged some game for relaxation.
Game 1:
Rules were as follows:
• String 1 should define the person and the first letter of the string 1 
should be same as the first letter of String 2
• String 2 should be the person’s name.
• Output String should be the concatenation of both the input strings.

Sample Input and Output 1:
Enter the first string:
Sleepy
Enter the second string:
Subhash
Sleepy Subhash

Sample Input and output 2:
Enter the first string:
Prem
Enter the second string:
Kabir
Invalid Input
'''
str1 = str(input("Enter the first string:"))
str2 = str(input("Enter the second string:"))

splitChars1 = [char for char in str1]
splitChars2 = [char for char in str2]

# print(splitChars1, splitChars2)

firstChar1 = splitChars1[0]
firstChar2 = splitChars2[0]

if firstChar1 == firstChar2:
    print(str1, str2)
else:
    print("Invalid Input")

# Problem 5
'''
Birthday Gift

Ace is celebrating his birthday  next month. He got bored by cutting cakes 
like his previous birthdays. He said to his father not to bring him a cake for his birthday,
he wants to use that cake money for good purpose. This time he is planning to 
celebrate his birthday in a unique way.
He asked his friends to give some good ideas for celebrating his birthday. 
One of his friends suggested donating books to students.

Ace was very happy about this idea. He decided to donate books to schools.  
In his place there is N number of schools. He went to those schools and collected 
the information about how many students are there in each school.
Price of  single book is Rs. X. Help him to find a total number of books required 
and total cost of required books by writing a code.

Input Format:
First line of the input is an integer, which corresponds to the total number of school, 'n'.
Next 'n' line of inputs are integers, which corresponds to the total number of students 
in each school.
Last line of input is an integer indicates the price of a book.

Output Format:
The output consists of a total number of books required and total cost.

Sample Input:
5
20
50
60
45
25
20
Sample Output:
Total number of books required : 200
Total cost: 4000
'''

schools = int(input())

totStudents = 0

for i in range(schools):
    students = int(input())
    totStudents += students

print(totStudents)

price = int(input())

totCost = totStudents * price

print("total: ", totCost)

# Problem 6
'''
Symmetric_Difference

Gokul have two different sets and he wants to find the Symmetric_Difference between two sets. 
The symmetric difference of two sets A and B is the set of elements that are in 
either of the sets A or B but not in both.

So can u please help to write a program to find the symmetric_Difference between two sets.
Input and Output format will be shown below.

Input Format Specifications:

Firstline contains to enter the elements to set1(integers).
Second-line contains to enter the elements to set2(integers).
Note that print the elements in sorted order.
Output Format Specifications:

Output Consists of Symmetric_difference between set1 and set2 (Integers)
If both set elements are equal to print ‘invalid set’.
 

Sample Input1:
1,2,3,4,5,6
2,3,5,7,8,9
Sample Output1:
{1, 4, 6, 7, 8, 9}

Sample input2:
1,2,3
1,2,3
Sample Output2:
invalid set
'''
list1 = input().split(',')
list2 = input().split(',')

set1 = set(map(int, list1))
set2 = set(map(int, list2))

# print(set1)
# print(set2)

setDiff = set1.symmetric_difference(set2)

if not setDiff:
    print("invalid set")
else:
    print(set(sorted(setDiff)))

# Problem 7
'''
ate Difference
In Swaasthya hospital of Delhi, many patients coming for their treatment 
from all over India. The hospital management noticed the hospital visitors 
are facing difficulties for car parking. So they want to automate the parking 
system such that it prints the difference date between two dates, i.e. 
the first date when parked your vehicle, and second date when taking your vehicle.
Help the team to program this requirement which would get the difference in days, 
hours, minutes and seconds between 2 dates.

Note:
The format of the dates is like "Jul 1 2014 2:43 PM"(without quotes). 

Input Format:
The first line of the input is the first date.
The second line of the input is the second date. 
Output Format :
The output is a count of days separated by space with the difference 
in time in the format "53 days, 5:43:00"(without quotes).
Refer to sample input and output for further formatting specifications.

Sample Input and Output 1:
Jul 1 2014 2:43PM
Aug 23 2014 8:26PM
53 days, 5:43:00

Sample Input and Output 2:
Jan 1 2014 2:43PM
Jul 21 2014 12:43PM
200 days, 22:00:00
'''
from datetime import datetime

def date_difference(date1, date2):
    # Define the date format
    dateFormat = "%b %d %Y %I:%M%p"
    
    date1 = datetime.strptime(date1, dateFormat)
    date2 = datetime.strptime(date2, dateFormat)
    
    # to calculate the difference between the dates
    diff = date2 - date1
    
    # Extract days, seconds, hours, minutes from delta
    days = diff.days
    secs = diff.seconds
    hours, secs = divmod(secs, 3600)
    mins, secs = divmod(secs, 60)
    
    result = f"{days} days, {hours:02}:{mins:02}:{secs:02}"
    return result

# Input the start and end dates
date1 = input().strip()
date2 = input().strip()

# Calculate and print the date difference
result = date_difference(date1, date2)
print(result)

# Problem 8
'''
Duplicate Attendance

XYZ College of Technology conducted a workshop on “Machine learning” in an auditorium. 
It is a big auditorium with 150 as its maximum capacity.  
Faculties felt difficult to take attendance, so they planned to circulate 
n attendance sheets to the students to mark their attendance. But few students 
unknowingly marked attendance more than one time in a sheet.  Now it is difficult 
for the faculty to find the duplicate entries of a student.

Help the faculty to remove the duplicate  attendance entry.

Note: Use tuple to solve the above problem

Input and Output Format:

First line of input consists of an integer n, which coresponds to the number of sheet.

Next n set of input correspond to students register number
Display Initial Attendance sheet with/without duplicate register numbers. 
Each inner tuple is considered as a single attendance sheet.
Display the unique register numbers.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to the input and the rest corresponds to the output.]

Sample Input and Output:
Enter total Number of sheets: 
6
1
2 3 1
4 5 6
2 3 4 5 6 7
2
3 4
Attendance Sheets with Register Number: ((1,), (2, 3, 1), (4, 5, 6), 
(2, 3, 4, 5, 6, 7), (2,), (3, 4))
Final sheet: (1, 2, 3, 4, 5, 6, 7)
'''
sheets = int(input("Enter total Number of sheets:"))

attendanceSheets = []

for sheet in range(sheets):
    sheet = tuple(map(int, input().split()))
    attendanceSheets.append(sheet)

print("Attendance Sheets with Register Number:", tuple(attendanceSheets))

diffNum = set()

for sheet in attendanceSheets:
    diffNum.update(sheet)

print("Final sheet:", tuple(sorted(diffNum)))   

# Problem 9
'''
Second Highest Mark of Student
You have a record of students. Each record contains the student's name 
and their marks in Maths, Physics, Chemistry, and computer science. 
The marks can be floating values. The user enters some integer followed by 
the names and marks of students. You are required to save the record in a 
dictionary data type. The user then enters a student's name. The output is 
the second-highest mark obtained by that student.
                                
 

Problem Constraints:

Use dictionary {} to store the data.

Use the Dictionary concept to solve the problem.
 
Input format:
The first line contains the integer, which indicates the number of students, 'n'.
The next 'n' lines contain the name and marks obtained by that student separated by a space.
The final line contains the name of a particular student to find the second-highest 
mark of him.

Output format:
The output is the second-highest mark obtained by the particular student. 
If he scored the same marks in all subjects, then print a message as shown sample I/O.
If the student name does not exist then print  "Student doesn't exist". [Refer Sample I/O]

Sample Input 1:
4
Sandy 78 67 89 100
John 45 46 48 23
Cherry 78 78 78 78
Ratan 78 90 89 56
Sandy
Sample Output 1:
Second Highest mark of Sandy: 89
 

Sample Input 2:
2
sath 100 100 100 100
jan 67 56 34 89
sath
Sample Output 2:
sath scored same marks in all subjects: 100
Sample Input 3:
2
Ratan 78 90 89 56
Sandy 78 67 89 100
pooja
Sample Output 3:
Student doesn't exist
'''

students = int(input())

records = {}

for marks in range(students):
    nameWithMarks = input().split()
    name = nameWithMarks[0]
    marks = list(map(float, nameWithMarks[1:]))
    records[name] = marks

studName = input()

def secHighestMark(marks):
    diffMarks = list(set(marks))
    if len(diffMarks) < 2:
        return None
    diffMarks.sort(reverse=True)
    return int(diffMarks[1])

if studName in records:
    marks = records[studName]
    secHigh = secHighestMark(marks)
    if secHigh is not None:
        print(f"Second Highest mark of {studName}: {secHigh}")
    else:
        print(f"{studName} scored same marks in all subjects: {int(marks[0])}")
else:
    print("Student doesn't exist")

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