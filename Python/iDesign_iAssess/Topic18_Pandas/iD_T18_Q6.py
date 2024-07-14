# Problem 6
'''
Sort Rows

 

Write a Python program to filter rows from a Data Frame based on a condition.

Load iris data from the input file.

Print the original Data Frame.

Sort rows based on Sepal Length in ascending order and display the Data Frame.

The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.

'''
import pandas as pd

df = pd.read_csv('iris_with_header.csv')

print("Original DataFrame")
print(df)

print("Sorted DataFrame")
print(df.sort_values('sepal_legth', ascending=True))