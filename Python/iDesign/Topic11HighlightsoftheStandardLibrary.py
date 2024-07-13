# 1

def date_decoder():
    date_str = input()
    year, month_abbr, day = date_str.split("-")
    year = int(year)
    if year <= 21:
        year += 2000
    else:
        year += 1900
    
    month_dict = {
        "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
        "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
    }
    month = month_dict[month_abbr]
    
    return year, month, int(day)

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year, month, day = date_decoder()
    is_leap = leap_year(year)
    
    print(f"({day:02}, {month:02}, {year}) is {'a leap year' if is_leap else 'not a leap year'}")

if __name__ == "__main__":
    main()

# 2
'''
Different Sum Operations

Suresh playing a numbers game. The game description is  Suresh picks random numbers and calculate the sum of all numbers, and the problem is some times the sum of the numbers will be float value and he wants to modify that sum by using Floor(), Ceil(), Round() functions and finally, he wants to calculate the difference of these 3 functions.



 

Input Format specifications:

Input consists of a list of values separated by space.
Output Format Specifications:

The first line of output should be the difference between floor()sum - ceil()sum.
Secondly of output should be the difference between the ceil()sum - round()sum.
The third line of output should be the difference between floor()sum - round()sum.
Constraints:

Use only floor() and ceil() round() function Python


Sample Input 1:
23.34 12 25

Sample Output 1:
-1.0
1.0
0.0

Sample Input 2:
-21.23 -18.23 -12

Sample Output 2:
-1.0
0.0
-1.0
'''
import math

numbers = list(map(float, input().split()))

total_sum = sum(numbers)

floor_sum = math.floor(total_sum)
ceil_sum = math.ceil(total_sum)
round_sum = round(total_sum)

diff1 = floor_sum - ceil_sum
diff2 = ceil_sum - round_sum
diff3 = floor_sum - round_sum

print(f"{diff1:.1f}")
print(f"{diff2:.1f}")
print(f"{diff3:.1f}")