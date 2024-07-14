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