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