# Problem 3
'''
Write a Python program to import specific columns from a given CSV file as a Pandas Data Frame.

The 2 columns to be imported are sepal_length and sepal_width.

 

The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.
'''
import pandas as pd

onlyColumns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"]

df = pd.read_csv('iris_with_header.csv', header=None, names=onlyColumns, skiprows=1)

newdf = df[["sepal_length", "sepal_width"]]

print(newdf)