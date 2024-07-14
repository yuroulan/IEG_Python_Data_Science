# Problem 5
'''
Seaborn / BarPlot

Bar Plot in Seaborn is used to show point estimates and confidence intervals as rectangular bars.

Write a Python Program to read in data from a csv file, load a Data Frame and generate a BarPlot using Seaborn.

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

Generate the barplot that shows the total_bill of the hotel tips based on day.
Use the following styling specifications : palette = 'PuRd',ci=None
Save the plot in a file named “splot3.png”

Output File
splot3.png
'''
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

plt.figure()
sns.barplot(x='day', y='total_bill', data=tips, palette='PuRd', ci=None)

plt.xlabel('day')
plt.ylabel('total_bill')

plt.savefig('splot3.png')
