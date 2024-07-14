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