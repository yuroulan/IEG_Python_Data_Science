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