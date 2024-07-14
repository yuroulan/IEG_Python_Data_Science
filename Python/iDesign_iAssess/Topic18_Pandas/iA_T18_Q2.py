# 2
'''
Remove Duplicates from a Data Frame

Write a Python program to rename a specific column in a Data Frame.

Import the given CSV file as a Data Frame.

Print the entire contents of the Data Frame

Remove the Duplicate Rows from the Data Frame

Print the entire contents of the Data Frame


The input file to be used is iris_duplicates.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.
'''
import pandas as pd

df = pd.read_csv('iris_duplicates.csv')

print("Original DataFrame")
print(df)

dropdf = df.drop_duplicates()

print("DataFrame after removing duplicates")
print(dropdf)