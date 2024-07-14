# Problem 8
'''
Set Operations

Write a Python program to perform the following Set Operations on Numpy Arrays.
1) Union of A and B
2) Intersection on A and B
3) A difference B

Get the array size and elements as input from the user. Consider 1-D float array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of 1st array
2
Enter the elements of first array
1
2
Enter the size of 2nd array
2
Enter the elements of second array
2
3
Union Array
[1. 2. 3.]
Intersection Array
[2.]
Difference Array
[1.]
'''
import numpy as np

# Get the size and elements of the first array
array1stSize = int(input("Enter the size of 1st array\n"))

print("Enter the elements of first array")

elements1stArray = []
for _ in range(array1stSize):
    elementsArray1st = float(input())
    elements1stArray.append(elementsArray1st)

array1st = np.array(elements1stArray)

# Get the size and elements of the second array
array2ndSize = int(input("Enter the size of 2nd array\n"))

print("Enter the elements of second array")

elements2ndArray = []
for _ in range(array2ndSize):
    elementsArray2nd = float(input())
    elements2ndArray.append(elementsArray2nd)

array2nd = np.array(elements2ndArray)

# Perform set operations
print("Union Array")
unionArray = np.union1d(array1st, array2nd)
print(unionArray)

print("Intersection Array")
intersectionArray = np.intersect1d(array1st, array2nd)
print(intersectionArray)

print("Difference Array")
diffArray = np.setdiff1d(array1st, array2nd)
print(diffArray)