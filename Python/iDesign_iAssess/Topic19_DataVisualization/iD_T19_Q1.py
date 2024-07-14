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