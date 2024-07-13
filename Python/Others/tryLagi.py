# '''
# Write a simple Python function that takes a number(n) as a parameter. 
# Then the function prints out the first n rows of Pascal's triangle. 
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
# '''

# # n as input parameter
# # n = int(input("Enter number, n : "))

# '''pattern = 5
# for i in range(1, pattern + 1):
#     for j in range(1, i + 1):
#         print("o", end=" ")
#     print()'''

# # will print :
# '''
# o
# oo
# ooo
# oooo
# ooooo
# '''

# '''n = int(input("Enter any value to print symbols : "))

# for i in range(n):
#     for j in range(n):
#         if(j <= i):                
#             print("*", end=" ")
#         else:
#             print("#", end=" ")
#     print()
# print('-' * 50)'''

# # def writer():
# #         title = 'Sir'
# #         name = (lambda x:title + ' ' + x)
# #         return name   
# #         who = writer()
# #         print(who('Arthur'))




# fo = open("foo.txt", "wb")
# print("Name of the file: ", fo.name)
# fo.flush()
# fo.close()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data.csv')

# Understand the dataset
print(df.info())
print(df.describe())

# Handling missing values
missing_values = df.isnull().sum()
print(missing_values)
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Visualize data distribution
df['numerical_column'].hist()
plt.show()

# Box plot to identify outliers
sns.boxplot(x='numerical_column', data=df)
plt.show()

# Scatter plot to visualize relationships
df.plot.scatter(x='feature1', y='feature2')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# Heatmap of correlation matrix
sns.heatmap(correlation_matrix, annot=True)
plt.show()
