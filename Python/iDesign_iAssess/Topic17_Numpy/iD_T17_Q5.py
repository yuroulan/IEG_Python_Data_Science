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