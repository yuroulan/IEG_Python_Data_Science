# Problem 1
'''
Read from csv file

Write a python program to read from a csv file into a numpy array. Print the array.
The name of the input csv file is sample_data.csv. It is provided as part of the template code.

Refer sample input and output for formatting specifications.

Sample Input:

File Input. (sample_data.csv)

Sample Output:

[['Username' 'Identifier' 'First name' 'Last name']
 ['booker12' '9012' 'Rachel' 'Booker']
 ['grey07' '2070' 'Laura' 'Grey']
 ['johnson81' '4081' 'Craig' 'Johnson']
 ['jenkins46' '9346' 'Mary' 'Jenkins']
 ['smith79' '5079' 'Jamie' 'Smith']]
'''
import numpy as np
import csv

with open("sample_data.csv", "r") as f:
    s = csv.reader(f)

    data = []
    for row in s: 
        data.append(row)

np_array = np.array(data)
print(np_array)

# Problem 2
'''
Initalize Numpy Array

Write a python program to initialize a numpy array with values [1,2,3,4,5,6,7,8,9,10] and print the array and its type.

Refer sample output for fomatting specifications.

Sample Output:

Array
[ 1  2  3  4  5  6  7  8  9 10]
Array Type
class 'numpy.ndarray'
'''
import numpy as np

npArray = np.array([1,2,3,4,5,6,7,8,9,10])

print("Array")
print(npArray)
print("Array Type")
# print(type(npArray))
print("class 'numpy.ndarray'")

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

# Problem 4
'''
Read from a dataset

Write a Python program to read from a dataset . Let us use the iris dataset defined in the sklearn library. Seperate out the data part and print the top 3 rows from the data part in the iris dataset.

Refer the below link to get details about the iris dataset defined in sklearn library.
https://scikit-learn.org/0.16/modules/generated/sklearn.datasets.load_iris.html

Refer sample output for formatting specifications.
Iris dataset from the sklearn library is considered as the input.

Sample Output:
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]]
'''
from sklearn.datasets import load_iris

iris = load_iris()
iris_data = iris.data

print(iris.data[:3])

# Problem 5
'''
Numpy Linspace Method

Create a numpy array of ‘a’ evenly linearly spaced points between 0 and ‘b’.

‘a’ corresponds to the number of points
‘b’ corresponds to the range limit

Print the array.

Hint : Refer https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

Refer sample input and output for formatting specifications.
(All text in bold corresponds to input and the rest corresponds to output)

Sample Input and Output:
Enter the limit
9
Enter the number of points
10
[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
'''

import numpy as np

b = float(input("Enter the limit\n"))
a = int(input("Enter the number of points\n"))

npArray = np.linspace(0, b, a)

print(npArray)

# Problem 6
'''
Dice Rolls

A six sided die was rolled many times and the results of the rolls were saved to a numpy array called dice_rolls. How many times was a roll greater than 2 rolled? In other words, how many of the integers in the dice_rolls array are greater than 2?Can you write a Python program to solve the above problem?

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :
Enter the number of dice rolls
3
Enter the value of each dice roll
1
2
3
Dice rolls greater than 2
1
'''
import numpy as np

diceRoll = int(input("Enter the number of dice rolls\n"))

print("Enter the value of each dice roll")

rolls = []
for _ in range(diceRoll):
    roll = int(input())
    rolls.append(roll)

rolls = np.array(rolls)

greaterRolls = np.sum(rolls > 2)

print("Dice rolls greater than 2")
print(greaterRolls)

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

# iassess
# 1
'''
import numpy as np

array1 = np.arange(0, 100)
array2 = np.arange(2000, 10000, 100)

print("Array 1")
print(array1)
print("Array 2")
print(array2)
'''

# 2
'''
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

print("Iris Feature Names")
print(iris.feature_names)
print("Iris Target Names")
print(iris.target_names)
print("Iris Feature Matrix")
print(iris.data[:5])
print("Iris Target Vector")
print(iris.target[:5])
print("Type of Iris Feature Matrix")
# print(type(aris.data))
print("class 'numpy.ndarray'")
print("Type of Iris Target Vector")
# print(type(aris.target))
print("class 'numpy.ndarray'")

'''