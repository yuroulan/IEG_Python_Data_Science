# Problem 1
'''
Character Deletion in a String
Sita and Gita were no so good friends and had a fight while doing tasks 
o one of them decided to teach a lesson to other and deleted one of the 
characters from her name entered in the company’s database.
                
Input format:
First line of the Input is a string indicating the name.
Second line of the input is an integer ‘n’( a value less than the string length).
Output Format:
The output contains a string with a character being deleted at ‘nth’ index of the input.
Sample input 1:
Andrews
2
Sample output 1:
Adrews
Sample input 2:
Jack
4
Sample output 2:
Jac
'''
def toDelete(name, n):
    nameLength = len(name)
    # print(nameLength)

    if 1<= n <= nameLength:
        toDelete = n - 1
        result = name[:toDelete] + name[toDelete + 1:]
        return result
    else:
        return False

name = input()
n = int(input())

print(toDelete(name, n))