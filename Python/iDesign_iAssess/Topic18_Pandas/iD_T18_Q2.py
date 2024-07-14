# Problem 2
'''
Import CSV file as DF

Write a Python program to import the given CSV file as a Pandas Data Frame.
The input file to be used is iris.csv file. Note that there is no header row in the input file.

The input file is given as part of the template code.
'''

import pandas as pd

columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"]

df = pd.read_csv('iris.csv', header=None, names=columns, skiprows=1)

print(df)