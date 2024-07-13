# Problem 1
'''
Supporting Documents
averageLength.txt
Average Length
Maths teacher Mr. Chulbul Pandey teaching the concept of average to his 3rd class students. Now he wants to take the test to check that students are clear about average concept. So he given some words on the black board and ask the students to find the average length of the words written on the board.

Help the students find the average word length, by writing a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens). 

Note :   
Read the input from the file and print the output in the console. 
Input File should be named as averageLength.txt. 

Input File Fomat :  
Sentences or sequence of words.   

Output Format:   
Print an integer value which corresponds to the average word length of a text in a file. 

Sample Output:  
4
'''
with open("averageLength.txt", "r") as f:
    s = f.read()
    # print(s)

sSplit = s.split()
# print(sSplit)

totWords = 0
wordCount = 0
for word in sSplit:
    totWords += len(word)
    wordCount += 1

# print(totWords)
# print(wordCount)

avgWords = totWords // wordCount
print(avgWords)

# Problem 2
'''
Sum of the Integers in the file
Consider an input file "sample.txt" with integer values. Write a program to open the file and read the content to find the sum of all values in the file.

Rule:
The file name should be sample.txt.

Input format:
Give the input as a file which contains the integer values.

Output format:
The output will be the integer which is the sum of the integers. Display the output in the console.

Sample Input file (sample.txt):
1
2
3
4
5

Sample Output:
The sum of the integers in the file sample.txt is:15
'''
with open("sample.txt", "r") as f:
    s = f.read()
    # print(s)

sSplit = s.split()
# print(sSplit)

sumNum = 0

for num in sSplit:
    sumNum += int(num)

print(f"The sum of the integers in the file sample.txt is:{sumNum}")

# Problem 3
'''
Number Of Lines in the file
Write the program to open an input file and read the number of lines in the input file.

Input format:
Input is a file. Filename: input.txt

Output format:
The output will be the integer which is the number of lines in the file. Display the output in the console.

Sample Input file (input.txt):
C was invented to write an operating system called UNIX.
C is a successor of B language which was introduced around 1970
The language was formalized in 1988 by the American National Standard Institue (ANSI).
By 1973 UNIX OS almost totally written in C.
Today C is the most widely used System Programming Language.
Most of the state of the art software have been implemented using C.
Easy to learn
Structured language
It produces efficient programs.
It can handle low-level activities.
It can be compiled on a variety of computers.

Sample Output 1:
The file has 11 lines
'''
with open("input.txt", "r") as f:
    s = f.readlines()

sLines = len(s)

print(f"The file has {sLines} lines")

# Problem 4
'''
Reverse the File
Write the program to reverse the given text file.

Rule:
The input file name should be input.txt and the output file name should be output.txt.

Sample Input File(input.txt):
A computer is a machine which helps us to calculate, simulate and store different scenarios. For example, in order to write an e-mail, instead of paper and pen first we use a software (or program) called wordprocessor which helps us enter sentences through keyboard (Input), computer's screen (output) to read, and modem (output/input) to send it to a distant relative, friend, etc.

Sample Output File(output.txt):
.cte ,dneirf ,evitaler tnatsid a ot ti dnes ot )tupni/tuptuo( medom dna ,daer ot )tuptuo( neercs s'retupmoc ,)tupnI( draobyek hguorht secnetnes retne su spleh hcihw rossecorpdrow dellac )margorp ro( erawtfos a esu ew tsrif nep dna repap fo daetsni ,liam-e na etirw ot redro ni ,elpmaxe roF .soiranecs tnereffid erots dna etalumis ,etaluclac ot su spleh hcihw enihcam a si retupmoc A
'''
with open("input.txt", "r") as f:
    s = f.read()
    # print(s)


sReverse = s[::-1]
print(sReverse)

with open("output.txt", "w") as of:
    of.write(sReverse)

# Problem 5
'''
Supporting Documents
SalariesDataSet.csv
Salary Sheet


Imran is working as an accountant in St. Mount College. During the salary payment there was some error with MS Excel software and he was unable to view the  amount to be credited to the faculties' account. So help him by writing a program that would read the file and print it in the console.

Note :
Read the input from the file and print the output in the console.

Input file name: SalariesDataSet.csv

Input File Fomat :
List of Professors along with their details. Find below the sample file format.

S.No,Rank,Discipline,Years since phd,Years service,Sex,Salary
1,Prof,B,19,18,Male,139750
2,Prof,B,20,16,Male,173200
3,AsstProf,B,4,3,Male,79750
4,Prof,B,45,39,Male,115000
5,AssocProf,B,6,6,Male,97000

Output Format:
Output is a list of “n” items which is read from the input file.

Sample Input and Output:
S.No;Rank;Discipline;Years since phd;Years service;Sex;Salary
1;Prof;B;19;18;Male;139750
2;Prof;B;20;16;Male;173200
3;AsstProf;B;4;3;Male;79750
4;Prof;B;45;39;Male;115000
5;AssocProf;B;6;6;Male;97000
'''
with open("SalariesDataSet.csv", "r") as f:
    s = f.read()
    print(s)

