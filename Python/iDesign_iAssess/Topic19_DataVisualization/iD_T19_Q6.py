# Problem 6
'''
Styling in Seaborn

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Scatter Plot using Matplotlib. Apply styling using Seaborn.

The dataset to be used is car_crashes dataset available as part of seaborn library. The columns in the car_crashes dataset are
total
speeding
alcohol
not_distracted
no_previous
ins_premium
ins_losses
abbrev
The dataset can be imported and loaded using the following command
sns.load_dataset('car_crashes', cache=True, data_home='\temp')

Generate a scatter plot with speeding on the X-axis and alcohol on the Y-axis. Save the plot in a file named “splot1.png”
Set seaborn style using the following parameters.
"whitegrid", {'grid.color': '.5', 'grid.linestyle': '-',}


Output File
splot1.png
'''
import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset('car_crashes', cache=True, data_home='\temp')

sns.set(style='whitegrid', rc={'grid.color': '.6', 'grid.linestyle' : '-'})

plt.figure()
plt.scatter(car_crashes['speeding'], car_crashes['alcohol'])

plt.savefig('splot1.png')