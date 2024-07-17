# Problem 4
'''
Double Integration using SciPy's dblquad Function

Write a Python program to perform double integration of a function f(x,y) over a specified region using SciPy's dblquad function. The user is prompted to enter the function to be integrated in terms of x and y, as well as the lower and upper limits for x and y. Then compute the double integral of the function over the specified region and outputs the result along with the error estimate.

Input Format:

Enter the function to be integrated in terms of x and y.
The user is prompted to enter the lower and upper limits for x.
The user is prompted to enter the lower and upper limits for y.
Output Format:
Print the result of the double integration and the error estimate.

Sample Input and Output:

Enter the function to be integrated in terms of x and y:
x**2
Enter the lower limit for x:
0
Enter the upper limit for x:
1
Enter the lower limit for y:
0
Enter the upper limit for y:
2
Result of dblquad integration: 0.6666666666666667
Error estimate: 2.2108134835808843e-14
'''
import numpy as np
from scipy.integrate import dblquad

fx = input("Enter the function to be integrated in terms of x and y: ")

xLow = float(input("Enter the lower limit for x: "))
xUp = float(input("Enter the upper limit for x: "))

yLow = float(input("Enter the lower limit for y: "))
yUp = float(input("Enter the upper limit for y: "))

def integrand(y, x):
    return eval(fx, {"__builtins__": None, "np": np, "x": x, "y": y})

result, error = dblquad(integrand, xLow, xUp, lambda x: yLow, lambda x: yUp)

print(f"Result of dblquad integration: {result}")
print(f"Error estimate: {error}")
