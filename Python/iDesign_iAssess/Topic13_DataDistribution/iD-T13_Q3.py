# Problem 3
'''
Mean-Std-Var-2

Write a python program to find the mean,std and var from pandas dataframe.

Input Format
Input is a file in CSV format.

Output Format
First line of output refers to mean of the column "cyl"
Second line of output refers to variance of the column "cyl"
Third line of output refers to standard deviation of the column "cyl"

Use 2 precisions for float
Input File name-"cars.csv"

Sample Input
File Input(csv)

Sample Output

6.50
2.40
1.55
'''
# to use pandas
import pandas as pd

df =pd.read_csv("cars.csv")

meanCyl = df['cyl'].mean()
varCyl = df['cyl'].var()
stdCyl = df['cyl'].std()

print(f"{meanCyl:0.2f}")
print(f"{varCyl:0.2f}")
print(f"{stdCyl:0.2f}")