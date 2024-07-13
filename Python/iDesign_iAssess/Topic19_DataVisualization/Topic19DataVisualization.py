# Problem 1
'''
MatPlotLib / Adding Elements to Line Plot

 

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Line Plot.

Generate a Line Plot with Team Name on the X-axis and Total Medals on the Y-axis. Save the plot in a file named “plot2.png”

 

Figure Specifications:

Set the following parameters of the plot

xlabel : Team Name
ylabel : Total Number of Medals
legend : location – ‘lower right’
title : Team-wise Total Medal Data
Figure Name : plot2.png
 
Styling specifications:

Line Style dotted and Line-color should be red
Add a circle marker with markerface color a black ('k').
Line width should be 3
 

About the Data Set:

The Data Set Medals.csv is provided as part of the template code.

The Medals.csv is a delimited text file containing the number of medals of the Top 10 teams in an Olympics. The file contains the following columns separated by the comma character.

Rank - Team’s Actual Rank in the Olympics
Team – Name of the Team / Country
Gold – Number of Gold Medals won
Silver – Number of Silver Medals won
Bronze – Number of Bronze Medals won
Total – Total Number of Medals won
Rank_By_Total – Team’s Rank in the Olympics considering the total number of medals won.
The Data Set is provided as part of the template code.

 

Sample Input and Output:

Input File

Medals.csv

Rank,Team,Gold,Silver,Bronze,Total,Rank_by_Total

1,China,14,6,9,29,2

2,USA,13,13,10,36,1

3,Japan,13,4,5,22,4

4,ROC,7,11,7,25,3

5,Australia,7,2,10,19,5

6,Great Britain,5,6,5,16,7

7,Korea,4,2,5,11,9

8,Germany,3,3,5,11,9

9,France,3,3,3,9,12

10,Italy,2,7,9,18,6
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Medals.csv')
# df = df.sort_values(by='Total', ascending=False)
# print(df)

teams = df['Team']
total_medals = df['Total']

# plt.figure(figsize=(10,6))

plt.plot(teams, total_medals, linestyle='--', color='red', marker='o', markerfacecolor='k', linewidth=3)

plt.xlabel("Team Name")
plt.ylabel("Total Number of Medals")
plt.title("Team-wise Total Medal Data")

plt.legend(['Team-wise Total Medal Data'], loc='lower right')

plt.savefig('plot2.png')

# Problem 2
'''
MatPlotLib / Histogram

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Histogram using Matplotlib.

Read the total medals received by each team and show it using the histogram to see the most common total medals range. Use the total medals range as [10,20,30,40]. Save the plot in a file named “plot6.png”

 

Figure Specifications:

Set the following parameters of the plot

xlabel : Total Medals Range
ylabel : Count
legend : location – ‘upper left’
title : Total Medals Histogram
Figure Name : plot6.png
 
Styling specifications:

The following styling specifications need to be set .

label = 'Total Medals Distribution'

 

About the Data Set:

The Data Set Medals.csv is provided as part of the template code.

The Medals.csv is a delimited text file containing the number of medals of the Top 10 teams in an Olympics. The file contains the following columns separated by the comma character.

Rank - Team’s Actual Rank in the Olympics
Team – Name of the Team / Country
Gold – Number of Gold Medals won
Silver – Number of Silver Medals won
Bronze – Number of Bronze Medals won
Total – Total Number of Medals won
Rank_By_Total – Team’s Rank in the Olympics considering the total number of medals won.
The Data Set is provided as part of the template code.

 

Sample Input and Output:

Input File

Medals.csv

Rank,Team,Gold,Silver,Bronze,Total,Rank_by_Total

1,China,14,6,9,29,2

2,USA,13,13,10,36,1

3,Japan,13,4,5,22,4

4,ROC,7,11,7,25,3

5,Australia,7,2,10,19,5

6,Great Britain,5,6,5,16,7

7,Korea,4,2,5,11,9

8,Germany,3,3,5,11,9

9,France,3,3,3,9,12

10,Italy,2,7,9,18,6

 

Output File

plot6.png



'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Medals.csv')
# df = df.sort_values(by='Total', ascending=False)
# print(df)

total_medals = df['Total']

bins = [10, 20, 30, 40]

plt.figure(figsize=(8, 6))

plt.hist(total_medals, bins=bins)

plt.legend(['Total Medal Distribution'], loc='upper left')

plt.xlabel("Total Medals Range")
plt.ylabel("Count")
plt.title("Total Medals Histogram")

plt.savefig('plot6.png')

# Problem 3
'''
MatPlotLib / Pie Chart

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Pie Chart using Matplotlib.

Calculate total medal data won by the top 10 teams of each medal type (Gold, Silver, Bronze) and show it using a Pie chart. Save the plot in a file named “plot7.png”

 

Figure Specifications:

Set the following parameters of the plot
labels = ['Gold', 'Silver', 'Bronze']
legend : location – ‘lower right’
title : Medals data
axis : equal
Figure Name : plot7.png
 

Styling specifications:

The following styling specifications need to be set .

labels = ['Gold', 'Silver', 'Bronze']

autopct='%1.1f%%'

 

About the Data Set:

The Data Set Medals.csv is provided as part of the template code.

The Medals.csv is a delimited text file containing the number of medals of the Top 10 teams in an Olympics. The file contains the following columns separated by the comma character.

Rank - Team’s Actual Rank in the Olympics
Team – Name of the Team / Country
Gold – Number of Gold Medals won
Silver – Number of Silver Medals won
Bronze – Number of Bronze Medals won
Total – Total Number of Medals won
Rank_By_Total – Team’s Rank in the Olympics considering the total number of medals won.
The Data Set is provided as part of the template code.

 

Sample Input and Output:

Input File

Medals.csv

Rank,Team,Gold,Silver,Bronze,Total,Rank_by_Total

1,China,14,6,9,29,2

2,USA,13,13,10,36,1

3,Japan,13,4,5,22,4

4,ROC,7,11,7,25,3

5,Australia,7,2,10,19,5

6,Great Britain,5,6,5,16,7

7,Korea,4,2,5,11,9

8,Germany,3,3,5,11,9

9,France,3,3,3,9,12

10,Italy,2,7,9,18,6

 

Output File

plot7.png

'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Medals.csv')

totalGold = df['Gold'].sum()
totalSilver = df['Silver'].sum()
totalBronze = df['Bronze'].sum()

medalCounts = [totalGold, totalSilver, totalBronze]
labels = ['Gold', 'Silver', 'Bronze']

plt.pie(medalCounts, labels=labels, autopct='%1.1f%%')

plt.title("Medals Data")
plt.legend(['Total Medal Distribution'], loc='lower right')
plt.axis('equal')

plt.savefig('plot7.png')

# Problem 4
'''
MatPlotLib / Scatter Plots

 

Write a Python Program to read in data from a csv file, load a Data Frame and generate a Scatter Plot using Matplotlib.

Generate a Scatter Plot with Rank on the X-axis and Rank_by_Total on the Y-axis. Save the plot in a file named “plot4.png”

 

Figure Specifications:

Set the following parameters of the plot

xlabel : Rank
ylabel : Rank_by_Total
legend : location – ‘upper left’
title : Rank Comparison
Figure Name : plot4.png
 

Styling specifications:

Label need to be set for the plot as ‘Rank Comparison’

 

About the Data Set:

The Data Set Medals.csv is provided as part of the template code.

The Medals.csv is a delimited text file containing the number of medals of the Top 10 teams in an Olympics. The file contains the following columns separated by the comma character.

Rank - Team’s Actual Rank in the Olympics
Team – Name of the Team / Country
Gold – Number of Gold Medals won
Silver – Number of Silver Medals won
Bronze – Number of Bronze Medals won
Total – Total Number of Medals won
Rank_By_Total – Team’s Rank in the Olympics considering the total number of medals won.
 

The Data Set is provided as part of the template code.

 

Sample Input and Output:

Input File

Medals.csv

Rank,Team,Gold,Silver,Bronze,Total,Rank_by_Total

1,China,14,6,9,29,2

2,USA,13,13,10,36,1

3,Japan,13,4,5,22,4

4,ROC,7,11,7,25,3

5,Australia,7,2,10,19,5

6,Great Britain,5,6,5,16,7

7,Korea,4,2,5,11,9

8,Germany,3,3,5,11,9

9,France,3,3,3,9,12

10,Italy,2,7,9,18,6

 

Output File

plot4.png

'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Medals.csv')
df = df.head(10)

rank = df['Rank']
rankByTotal = df['Rank_by_Total']

plt.figure(figsize=(8, 6))
plt.scatter(rank, rankByTotal)

plt.title('Rank Comparison')
plt.xlabel('Rank')
plt.ylabel('Rank_by_Total')
plt.legend(['Rank Comparison'], loc='upper left')

plt.savefig('plot4.png')

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
