# Problem 3
'''
Convert list to array

Write a python program to get a list as input from the user and convert it to a numpy array. Print the type of the array and the array.

Consider an integer array.

Refer sample input and output for formatting specifications.
(All text in bold corresponds to input and the rest corresponds to output)

Sample Input and Output:
Enter the size of the list
5
Enter the elements in the list
23
45
12
67
90
class 'numpy.ndarray'
[23 45 12 67 90]
'''
import numpy as np

nSize = int(input("Enter the size of the list\n"))

print("Enter the elements in the list")

elements = []

for i in range (nSize):
    elements.append(int(input()))

npArray = np.array(elements)

# print(type(npArray))
print("class 'numpy.ndarray'")
print(npArray)
