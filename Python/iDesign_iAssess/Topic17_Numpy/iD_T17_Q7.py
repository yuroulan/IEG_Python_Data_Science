# Problem 7
'''
Reshaping Arrays

Write a Python program to convert a 1-D array to a 2-D array with m rows and n columns.

Create the 1-D array using the range function by passing 1 parameter that corresponds to the max value.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of 1-D array
6
1-D Array
[0 1 2 3 4 5]
Enter m value
3
Enter n value
2
2-D Array
[[0 1]
 [2 3]
 [4 5]]
'''
import numpy as np

size1DArray = int(input("Enter the size of 1-D array\n"))

array1D = np.arange(size1DArray)

print("1-D Array")
print(array1D)

m = int(input("Enter m value\n"))
n = int(input("Enter n value\n"))

if len(array1D) != m * n:
    print("The product of m and n does not match the size of the 1-D array")
else:
    array2D = array1D.reshape(m, n)

print("2-D Array")
print(array2D)