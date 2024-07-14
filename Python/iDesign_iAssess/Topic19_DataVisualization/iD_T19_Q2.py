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