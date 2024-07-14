# Problem 7
'''
ate Difference
In Swaasthya hospital of Delhi, many patients coming for their treatment 
from all over India. The hospital management noticed the hospital visitors 
are facing difficulties for car parking. So they want to automate the parking 
system such that it prints the difference date between two dates, i.e. 
the first date when parked your vehicle, and second date when taking your vehicle.
Help the team to program this requirement which would get the difference in days, 
hours, minutes and seconds between 2 dates.

Note:
The format of the dates is like "Jul 1 2014 2:43 PM"(without quotes). 

Input Format:
The first line of the input is the first date.
The second line of the input is the second date. 
Output Format :
The output is a count of days separated by space with the difference 
in time in the format "53 days, 5:43:00"(without quotes).
Refer to sample input and output for further formatting specifications.

Sample Input and Output 1:
Jul 1 2014 2:43PM
Aug 23 2014 8:26PM
53 days, 5:43:00

Sample Input and Output 2:
Jan 1 2014 2:43PM
Jul 21 2014 12:43PM
200 days, 22:00:00
'''
from datetime import datetime

def date_difference(date1, date2):
    # Define the date format
    dateFormat = "%b %d %Y %I:%M%p"
    
    date1 = datetime.strptime(date1, dateFormat)
    date2 = datetime.strptime(date2, dateFormat)
    
    # to calculate the difference between the dates
    diff = date2 - date1
    
    # Extract days, seconds, hours, minutes from delta
    days = diff.days
    secs = diff.seconds
    hours, secs = divmod(secs, 3600)
    mins, secs = divmod(secs, 60)
    
    result = f"{days} days, {hours:02}:{mins:02}:{secs:02}"
    return result

# Input the start and end dates
date1 = input().strip()
date2 = input().strip()

# Calculate and print the date difference
result = date_difference(date1, date2)
print(result)