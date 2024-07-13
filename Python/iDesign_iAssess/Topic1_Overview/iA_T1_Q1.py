'''
WonderWorks Magic Show
The Magic Castle, the home of the Academy of Magical Arts at California has organized the great ‘WonderWorks Magic Show’. 3 renowned magicians were invited to mystify and thrill the crowd with their world’s spectacular magic tricks. At the end of each of the 3 magicians’ shows, the audience were requested to give their feedback in a scale of 1 to 10. Number of people who watched each show and the average feedback rating of each show is known. Write a program to find the average feedback rating of the WonderWorks Magic show.

Input Format:
First line of the input is an integer value that corresponds to the number of people who watched show 1.
Second line of the input is a float value that corresponds to the average rating of show 1.
Third line of the input is an integer value that corresponds to the number of people who watched show 2.
Fourth line of the input is a float value that corresponds to the average rating of show 2.
Fifth line of the input is an integer value that corresponds to the number of people who watched show 3.
Sixth line of the input is a float value that corresponds to the average rating of show 3.

Output Format:
Output should display the overall average rating for the show. Display the rating correct to 2 decimal places.
Refer sample input and output for formatting specifications.
'''

show1 = int(input("Enter the number of people who watched show 1"))
avg1 = float(input("Enter the average rating for show 1"))
show2 = int(input("Enter the number of people who watched show 2"))
avg2 = float(input("Enter the average rating for show 2"))
show3 = int(input("Enter the number of people who watched show 3"))
avg3 = float(input("Enter the average rating for show 3"))

totAvg1 = show1 * avg1
totAvg2 = show2 * avg2
totAvg3 = show3 * avg3

AllAvgTot = totAvg1 + totAvg2 + totAvg3

print("The overall average rating for the show is {AllAvgTot:0.2f}")