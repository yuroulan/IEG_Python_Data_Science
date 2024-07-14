# iassess
# 1.
'''
Module: String Splitting
Akash wants to send a message to his colleague about his official team work. But he wants to maintain his message privacy, so he will encrypt his message and send that to his friend. Now his colleague wants to decode that message. Akash gave a hint to his colleague, like he has to decode his message by splitting his message with a particular character sent by him. Help Akash's colleague to decode the message by writing a program.

Input Format:
The first line of input consists of a string.
The next line of input consists of a character.

Output Format:
The output is a list of strings after splitting.
Every first letter of splitted word should be in capital.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
aaahggghbbb
h
Strings after splitting
Aaa
Ggg
Bbb

Sample Input and Output 2:
ahhg&hcg&fhgf90
&
Strings after splitting
Ahhg
Hcg
Fhgf90
'''
def decode(nStr, nChar):
    # Split the string using the specified character
    capLetter = [letter.capitalize() for letter in nStr.split(nChar)]
    
    # Print the formatted output
    print("Strings after splitting")
    for letter in capLetter:
        print(letter)

# Example usage:
print("Enter the message:")
nStr = input().strip()  # Read the message input
print("Enter the character for splitting:")
nChar = input().strip()  # Read the split character input

decode(nStr, nChar)