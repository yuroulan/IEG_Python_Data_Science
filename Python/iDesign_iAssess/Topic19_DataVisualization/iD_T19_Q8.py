# Problem 8
'''
Seaborn / Count Plot

The count plot can be thought of as a histogram across a categorical variable.

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Count Plot using Seaborn.

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

Generate the count plot using day. Use sex as hue.
Use the following styling specifications : palette = 'magma'
Save the plot in a file named “splot6.png”

Output File
splot6.png

'''
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

plt.figure()
sns.countplot(x='day', hue='sex', data=tips, palette='magma')

plt.xlabel('day')
plt.ylabel('count')
plt.legend(loc='upper left')

plt.savefig('splot6.png')
