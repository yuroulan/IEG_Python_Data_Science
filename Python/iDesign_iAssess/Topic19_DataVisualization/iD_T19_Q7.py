# Problem 7
'''
Seaborn / Histogram

Histograms represent the data distribution by forming bins along with the range of the data and then drawing bars to show the number of observations that fall in each bin. In Seaborn, we use distplot() function to plot histograms.

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Histogram using Seaborn.

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

Generate the histogram for total_bill and set kde=True. Save the plot in a file named “splot2.png”

Output File
splot2.png

'''
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips', cache=True, data_home=r'\temp' )

plt.figure()
sns.histplot(tips['total_bill'], kde=True)

plt.xlabel('total_bill')
plt.ylabel('Count')

plt.savefig('splot2.png')
