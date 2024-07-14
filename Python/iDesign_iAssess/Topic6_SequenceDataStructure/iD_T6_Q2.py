# Problem 2
'''
Print Palindrome

James and Jones had a discussion on palindrome strings. They were assigned to a task 
in which they had to check if the given string is a palindrome or not and 
if not they had to make it as a palindrome.
The condition for the task was as follows:
• Input and output strings should be case sensitive.
Help them with a program to make their task easier.

Input format:
Input consists of a string.
output format:
the output will be a palindrome string.
Sample Input:
Tamil
Sample Output
TamaT

Sample Input:
Amphi
Sample Output
AmpmA
'''
inp = input()   # let say user input is Tamil, its not a palindrome
                # so i need to change into palindrome such as TamaT

# to check palindrome
isPal = inp == inp[::-1]
print(isPal)    # -->> will return True / False

if not isPal:
    revInp = inp[::-1]
    pal = inp[:len(inp)//2] + revInp[len(inp)//2:]
else:
    pal = inp   # if the input already a palindrome

print(pal)