# Problem 1
'''

Chebyshev distance - Similarity

In this problem, given two feature vectors as input , find the Chebyshev distance between the given vectors without using any inbuild python libraries.

Input format :
1st line of input is an integer ‘n’, which corresponds to the length of both the vectors
Next 2 lines of input consists of ‘n’ space separated integers, which corresponds to the 1st and 2nd input vectors .

Output Format :
Output corresponds to single integer value, which corresponds to the Chebyshev Distance between the vectors.

Note : print ‘Invalid Input’ , if the vectors length doesn’t match.

Sample Input :
Enter the length of the array
3
1 5 89
236 4 58

Sample Output :
235
'''
# to use function def for chebyshev distance
def chebDis(vect1, vect2):
    if len(vect1) != len(vect2):    # to check if vect1 and vect 2 has same lengths
        print("Invalid Input")
    else:
        return max(abs(a - b) for a, b in zip(vect1, vect2))   # <<-- to find chebyshev distance    
    
vectLength = int(input("Enter the length of the array\n"))    # let say user insert 3 lengths

vect1 = list(map(int, input().split()))   # to put input val as list of np.array, split by space
vect2 = list(map(int, input().split()))

result = chebDis(vect1, vect2)
print(result)

# Problem 2
'''
Mean-Std-Var-1

Write a python program to find the mean,std and var from pandas dataframe.

Input Format
Input is a file in CSV format.

Output Format
First line of output refers to mean of the column "pl"
Second line of output refers to variance of the column "pl"
Third line of output refers to standard deviation of the column "pl"

Use 2 precisions for float
Input File name-"iris.csv"

Sample Input
File Input(csv)

Sample Output

5.79 
0.64 
0.80
'''
# to use pandas
import pandas as pd

df =pd.read_csv("iris.csv")

meanPl = df['pl'].mean()
varPl = df['pl'].var()
stdPl = df['pl'].std()

print(f"{meanPl:0.2f}")
print(f"{varPl:0.2f}")
print(f"{stdPl:0.2f}")   

# Problem 3
'''
Mean-Std-Var-2

Write a python program to find the mean,std and var from pandas dataframe.

Input Format
Input is a file in CSV format.

Output Format
First line of output refers to mean of the column "cyl"
Second line of output refers to variance of the column "cyl"
Third line of output refers to standard deviation of the column "cyl"

Use 2 precisions for float
Input File name-"cars.csv"

Sample Input
File Input(csv)

Sample Output

6.50
2.40
1.55
'''
# to use pandas
import pandas as pd

df =pd.read_csv("cars.csv")

meanCyl = df['cyl'].mean()
varCyl = df['cyl'].var()
stdCyl = df['cyl'].std()

print(f"{meanCyl:0.2f}")
print(f"{varCyl:0.2f}")
print(f"{stdCyl:0.2f}")

# iassess
# 1
'''
Finding Statistics

Ramesh, the businessman had a list of data containing the overall transactions in a year. He wanted to calculate the statistics of his transactions i.e. calculating mean, median, and variance of his transactions to keep the track of his business growth over the years.

Let's help Ramesh to calculate the mean, median and variance of the list of transactions given by writing code according to his requirements.

Input format:

Input consists of an array containing the overall transactions done in a year.

Output Format:

The output displays the mean, median and standard deviation of the transactions.


Refer the sample Input and Output for formatting specifications

Sample Input and Output:

Enter the transactions done in each month for last year

4545
232
5565
1232
4512
-7878
-9698
-7785
6624
-5757
7597
-774848

Mean : -64638.25
Median : 732.00
Standard Deviation : 214218.97
'''
def meanTrans(trans):
    return sum(trans) / len(trans)

def medTrans(trans):
    transSorted = sorted(trans)
    n = len(transSorted)
    mid = n // 2
    if n % 2 == 0:
        med = (transSorted[mid - 1] + transSorted[mid]) / 2
    else:
        med = transSorted[mid]
    return med

def varTrans(trans, mean):
    return sum((x - mean) ** 2 for x in trans) / len(trans)

def stdTrans(varTrans):
    return varTrans ** 0.5  

def calculate():
    print("Enter the transactions done in each month for last year")
    transaction = []
    for i in range(12):
        try:
            trans = float(input())
            transaction.append(trans)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
    
    if len(transaction) == 0:
        print("No transactions provided.")
        return

    mean = meanTrans(transaction)
    med = medTrans(transaction)
    var = varTrans(transaction, mean)
    std = stdTrans(var)

    print(f"Mean : {mean:.2f}")
    print(f"Median : {med:.2f}")
    print(f"Standard Deviation : {std:.2f}")

# Call the calculate function to run the program
calculate()

#2
'''
Maximum and Minimum Turnovers
 
Ramesh is self-employed. it's been years after setting his business. With all the hardships he brought his business into the track. He got a thought to analyze his graph of progress from last year to the current year.  
He has a list of data containing the transactions done per month in a year, he wanted to calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

But unaware of any software he had to do it manually which was tedious work.  He asks Suresh, a Software Engineer to help him in this. Fortunately, Suresh was working on data science and thought he could easily help him. 
Assume yourself to be in Suresh's position and had to help Ramesh in tracking his growth from last year to current year. Given the data set of calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

Note: All positive values in the transactions are considered as the "Income" and All negative values are considered as "Investment".

Input Format:
Input consists of an array indicating the transactions done over the year.

Output Format:
The Output displays the months having the maximum turnover and the minimum turnover.

Refer sample input and output for formatting specifications.

Sample Input and Output: 

Enter the transaction done last year
10000
7898
7878
787878
787878
777
777878
77777
-5656556
45454
45455
4545454
Minimum Turnover : -5656556
Maximum Turnover : 4545454
Minimum Turnover Month : 8
Maximum Turnover Month : 11
'''

def calculate():
    print("Enter the transaction done last year")
    transaction = []
    for i in range(12):
        try:
            trans = float(input().strip())
            transaction.append(trans)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return transaction
    
    return transaction

def turnOver(trans):
    maxTurnOver = max(trans)
    minTurnOver = min(trans)

    maxMonth = trans.index(maxTurnOver)
    minMonth = trans.index(minTurnOver)
    return maxTurnOver, minTurnOver, maxMonth, minMonth

def main():
    transaction = calculate()
    if not transaction:
        return

    max_turnover, min_turnover, max_month, min_month = turnOver(transaction)


    print(f"Minimum Turnover : {min_turnover:.0f}")
    print(f"Maximum Turnover : {max_turnover:.0f}")
    print(f"Minimum Turnover Month : {min_month}")
    print(f"Maximum Turnover Month : {max_month}")

if __name__ == "__main__":
    main()

        


