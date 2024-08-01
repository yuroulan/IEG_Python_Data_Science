# Problem 1
'''
Create DF from List of Lists

Write a Python program to create a Pandas Data Frame from a List of Lists and print the Data Frame.

List of Lists is specified as part of the template code.
'''
import pandas as pd

data = [
    [5.1, 3.5, 1.4, 0.2, "IrisSetosa"],
    [4.9, 3.0, 1.4, 0.2, "IrisSetosa"],
    [4.9, 3.0, 1.4, 0.2, "IrisVersicolor"],
    [6.4, 3.2, 4.5, 1.5, "IrisVersicolor"],
    [6.3, 3.3, 6.0, 2.5, "IrisVirginica"],
    [5.8, 2.7, 5.1, 1.9, "IrisVirginica"]
]

columns = ["sepal_length", "sepal_width", "petal length", "petal width", "species_type"]

df = pd.DataFrame(data, columns=columns)

print(df)

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

# Problem 5 
'''
Write a Python program to rename a specific column in a Data Frame.

Import the given CSV file as a Data Frame.

Print the column names using columns attribute.

Rename the column “species_type” to “SpeciesType”

Print the column names using columns attribute.

Print the entire contents of the Data Frame

 

The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.
'''
import pandas as pd

# columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"]

# df = pd.read_csv('iris_with_header.csv', header=None, names=columns)

df = pd.read_csv('iris_with_header.csv')

print("Column Names")
print(df.columns)

df.rename(columns={'species_type' : 'SpeciesType'}, inplace=True)

print('Column Names after renaming')
print(df.columns)

print("DataFrame")
print(df)

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

# iassess
# 1
'''
Merge 2 Data Frames

Write a Python program to merge 2 Data Frames.

The 2 Data Frames to be merged are given as part of the template code

Print the First Data Frame

Print the Second Data Frame

Merge the 2 Data Frames and rearrange the columns in the order student_name , department , sem1_cgpa, sem2_cgpa

Print the entire contents of the merged Data Frame
'''
#Merge DataFrames, Change column order

import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])

print("DataFrame1")
print(df1)

df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

print("DataFrame2")
print(df2)

mergedf = pd.merge(df1, df2, on='student_name')

mergedf = mergedf[['student_name', 'department', 'sem1_cgpa', 'sem2_cgpa']]

print("Merged DataFrame")
print(mergedf)

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