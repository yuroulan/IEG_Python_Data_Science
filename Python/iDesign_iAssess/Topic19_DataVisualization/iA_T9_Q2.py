# 2
'''
Seaborn / Box Plot

The box plot, also called the box and whisker diagram is used for depicting groups of numerical data through the quartiles. It is known as the box and whisker diagram because it is composed of a box and whiskers. Boxplot is also used for detecting the outlier in a data set.

A box plot is composed of a summary of 5 different data points: the minimum, first quartile, median, third quartile, and maximum.
Minimum
First Quartile or 25%
Median (Second Quartile) or 50%
Third Quartile or 75%
Maximum

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Box Plot using Seaborn.

The dataset to be used is tips dataset available as part of seaborn library.
According to the tips dataset documentation, the Tips dataset is a data frame with 244 rows and 7 variables which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant. In all the waiter recorded 244 tips.
The columns in the tips dataset are
total_bill
tip
sex
smoker
day
time
size
The dataset can be imported and loaded using the following command
sns.load_dataset('tips’, cache=True, data_home='\temp')

Generate the Box plot using day on the x-axis and total_bill on the y-axis .

Save the plot in a file named “splot9.png”

Output File
splot8.png

'''

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

plt.figure()
sns.boxplot(x='day', y='total_bill', data=tips)

plt.xlabel = 'day'
plt.ylabel = 'total_bill'

plt.savefig('splot8.png')
