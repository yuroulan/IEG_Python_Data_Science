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