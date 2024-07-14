# Problem 4
'''
Write a Python program to perform the following tasks :

Import the given csv file as Data Frame
Display the entire contents of the Data Frame
Display the Shape of the Data Frame
Display the data types of the different columns in the Data Frame
Display the number of columns under each data type in the Data Frame
Display the Summary Statistics of the Data Frame
 

The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.
'''
import pandas as pd

df = pd.read_csv('iris_with_header.csv')

print("DataFrame")
print(df)

print("shape")
print(df.shape)

print("Data Types")
print(df.dtypes)

print("Column Count under each dtype")
print(df.dtypes.value_counts())

print("Summary Statistics")
print(df.describe())