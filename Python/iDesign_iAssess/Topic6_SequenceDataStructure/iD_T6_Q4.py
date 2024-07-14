# Problem 4
'''
Concatenation of Strings
Fun with “Strings” at Chicago technologies.
The official heads of chicago technologies thought only working would tire the 
employees so they arranged some game for relaxation.
Game 1:
Rules were as follows:
• String 1 should define the person and the first letter of the string 1 
should be same as the first letter of String 2
• String 2 should be the person’s name.
• Output String should be the concatenation of both the input strings.

Sample Input and Output 1:
Enter the first string:
Sleepy
Enter the second string:
Subhash
Sleepy Subhash

Sample Input and output 2:
Enter the first string:
Prem
Enter the second string:
Kabir
Invalid Input
'''
str1 = str(input("Enter the first string:"))
str2 = str(input("Enter the second string:"))

splitChars1 = [char for char in str1]
splitChars2 = [char for char in str2]

# print(splitChars1, splitChars2)

firstChar1 = splitChars1[0]
firstChar2 = splitChars2[0]

if firstChar1 == firstChar2:
    print(str1, str2)
else:
    print("Invalid Input")