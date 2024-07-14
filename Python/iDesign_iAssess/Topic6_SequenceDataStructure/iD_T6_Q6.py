# Problem 6
'''
Symmetric_Difference

Gokul have two different sets and he wants to find the Symmetric_Difference between two sets. 
The symmetric difference of two sets A and B is the set of elements that are in 
either of the sets A or B but not in both.

So can u please help to write a program to find the symmetric_Difference between two sets.
Input and Output format will be shown below.

Input Format Specifications:

Firstline contains to enter the elements to set1(integers).
Second-line contains to enter the elements to set2(integers).
Note that print the elements in sorted order.
Output Format Specifications:

Output Consists of Symmetric_difference between set1 and set2 (Integers)
If both set elements are equal to print ‘invalid set’.
 

Sample Input1:
1,2,3,4,5,6
2,3,5,7,8,9
Sample Output1:
{1, 4, 6, 7, 8, 9}

Sample input2:
1,2,3
1,2,3
Sample Output2:
invalid set
'''
list1 = input().split(',')
list2 = input().split(',')

set1 = set(map(int, list1))
set2 = set(map(int, list2))

# print(set1)
# print(set2)

setDiff = set1.symmetric_difference(set2)

if not setDiff:
    print("invalid set")
else:
    print(set(sorted(setDiff)))