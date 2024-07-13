# Problem 5

'''
Grades of Rides
“AquaticaCarnival” is the most successful event dedicated to children and families. The Event has more than 20 rides for children and adults and the organizers always ensure not to compromise on the safety of the visitors.
To ensure the safety of the rides, the organizers have graded the rides in the fair according to the following conditions:
Hurl Factor must be greater than 50.
Spin Factor must be greater than 60.
Speed factor must be greater than 100.

The grades are as follows:
Grade is 10 if all three conditions are met.
Grade is 9 if conditions (i) and (ii) are met.
Grade is 8 if conditions (ii) and (iii) are met.
Grade is 7 if conditions (i) and (iii) are met.
Garde is 6 if only one condition is met.
Grade is 5 if none of three conditions are met.
Write a program display the grade of the rides, given the values of hurl factor, spin factor and speed factor of the ride under consideration.

Input Format:
First line of the input consists of 3 integers that gives the Hurl Factor, Spin Factor and Speed Factor of the ride, each separated by a space.

Output Format:
Output should display the grade of the ride depending on Conditions.
Refer sample input and output for formatting specifications.

Sample Input 1:
51 89 150

Sample Output 1:
10

Sample Input 2:
45 69 102

Sample Output 2:
8
'''
factors = input()

factors = factors.split(" ")

strFact = []                           # str to int
for factor in factors:
    strFact.append(int(factor))

HF = strFact[0] > 50
SF = strFact[1] > 60
SPF = strFact[2] > 100

if(HF and SF and SPF):
    print("10")
elif(HF and SF):
    print("9")
elif(SF and SPF):
    print("8")
elif(HF and SPF):
    print("7")
elif(HF or SF or SPF):
    print("6")
else:
    print("5")