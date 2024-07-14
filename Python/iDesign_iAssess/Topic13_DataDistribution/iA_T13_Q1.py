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