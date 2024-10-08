# Problem 7
'''
Write a program to calculate maximum and minimum number from the given user input.

Note : Use built-in function only.

Input and Output Format :

(Refer sample input and output)

[All text in bold corresponds to input and rest others are output]

Sample Input and Output :

Enter the values:

1 4 6 12 73 92 134

The maximum value is : 134

The minimum value is : 1
'''

def maximumMinimum(nums):

    listNum = list(map(int, nums.split()))

    maxVal = max(listNum)    # max and min is a builtin fx
    minVal = min(listNum)

    print(f"The maximum value is : {maxVal}")
    print(f"The minimum value is : {minVal}")

print("Enter the values:")
userInp = input()
maximumMinimum(userInp) # tuple