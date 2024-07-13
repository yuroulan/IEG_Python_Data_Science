# Problem 1
'''
Password Extraction

Ebox Engineering college has lot of systems in various labs and libraries. Each system in college running with windows OS having different username with different passwords . Student can choose any non admin user from the system and have to extract password from the given hint. Password is always a number of any length or no password . From the hint given , user has to extract the maximum number and that extracted number will be used as password. If no number present in the hint then there is no password for that particular system user.

Help the students to find the password by writing a program.

Input and Output Format:

Input is single line string which is a hint. String contains only alphanumeric characters.

Output is a maximum number extracted from the input string.consider only positive numbers.print “No Password” without quotes when input has no number.

Refer sample input and output for formatting specifications

Sample Input 1:
hello123 abcd456 efgh99999
Sample Output 1:
99999

Sample Input 2:
abcdefgh
Sample Output 2:
No Password
'''
import re

def password(hint):
    nums = re.findall(r'\d+', hint)  # Find all sequences of digits
    if not nums:
        return "No Password"
    maxNum = max(int(num) for num in nums)  # Find the maximum number based on integer value
    return maxNum

def main():
    hint = input().strip()

    result = password(hint)
    print(result)

if __name__ == "__main__":
    main()

# Problem 2
'''
Swiggy Special Offer Code
Swiggy is an online food ordering and delivery platform. For Holi festival they planned to give special offer upto 50% based on offer code shared by the Swiggy team. Due to lot of offer code forgery they set a pattern to create an offer code. The pattern for offer code was , it should be a word which contains all vowels. If there is any word without all vowels then that offer code was rejected by the swiggy team.
 
Input and Output Format:
Input is a string .Only lower case allowed.
Output is a string . Print “Accepted “ if offer code is valid else “Not Accepted” without quotes.
Refer sample input and output for formatting specifications.


Sample Input 1:
tragedious
Sample Output 1:
Accepted

Sample Input 2:
hello everyone
Sample Output 2:
Not Accepted
'''
inpStr = str(input().strip())
inpChar = set(inpStr)
vowels = set('aeiou')   # put vowels in set

if vowels.issubset(inpChar):
    print("Accepted")
else:
    print("Not Accepted")

# Problem 3
'''
Block Spam Calls
 
In the digital world, it's easy to access contact details of individuals through online. Users give permission to third party apps to access basic details making it easy for spammers to get more contacts. Hackers are using this contact numbers for making Spam calls (irrelevant or inappropriate call sent over the phone) to annoy the users. So to handle this issue Cyber Crime Department need to analyze the valid and spam call mobile number pattern. The valid phone number pattern should contain following things:
1. It should start with "+91-" 
2. Followed by ten digits
If any mobile number violating the above rules can be blocked immediatley.

Input and Output Format:
Input is a string .
Output is a string . Refer sample input and output for formatting specifications.
 
Sample input 1:
+91-9876543210
Sample output 1:
Not a Spam Call
Sample input 2:
9876543210
Sample output 2:
Spam Call
'''
phoneNum = input().strip()

if phoneNum.startswith("+91-") and len(phoneNum) == 14 and phoneNum[4:].isdigit():
    print("Not a Spam Call")
else:
    print("Spam Call")

# Problem 4
'''
String Shuffling Pattern
Jack and Daniel are two army officers deployed in one under cover operation inside terrorist camp. They follow certain encryption strategy to communicate each other inside the camp . They follow string shuffling pattern as their encryption strategy. In this strategy, they can pass any message of any length, but only two words allowed. From that two words they need to find encrypted string which is a single word. Encryption principle followed here is to join first character of first word and last character of second word,then second character of first word and second last character of second string and so on to form a encrypted string. If there is no enough characters in any of string , add remaining characters in other string in encrypted string. 
Help the officers to automate the process by writing a program.
Note:
No need to consider the decryption process.
Input and Output Format:
Input consists of two strings and output is a shuffled string which is a encrypted string. Refer sample input and output for formatting specifications.
Sample input:
hello
hi
Sample output:
hiehllo
'''
def encryptStr(word1, word2):
    encryptStr =[]

    i, j = 0, len(word2) - 1    # to initialize two pointers

    while i < len(word1) and j >= 0:
        encryptStr.append(word1[i])
        encryptStr.append(word2[j])

        i += 1
        j -= 1

    while i < len(word1):
        encryptStr.append(word1[i])
        i += 1

    while j >= 0:
        encryptStr.append(word2[j])
        j -= 1

    return ''.join(encryptStr)

s1 = input()
s2 = input()

encryptedStr = encryptStr(s1, s2)

print(encryptedStr)

# Problem 5
'''
Income Tax PAN Validation
Tax Information Network (TIN) is an initiative by Income Tax Department of India (ITD) for the modernization of the current system for collection, processing, monitoring and accounting of direct taxes using information technology. The network will check the eligible entities based on Permanent Account Numbers (PAN).PAN contains ten-digits in which first five characters are letters, next four numerals, last character is a letter and all characters in PAN number is always uppercase.If the PAN given by the user follow the above format then it is a Valid PAN Number other wise Invalid PAN Number.
write a program to validate the PAN number.
 
Input and Output Format:
Input is string of any length of any case.
Output is string ,should print “Valid PAN Number” without quotes if input fits the PAN rules otherwise “Invalid PAN Number” without quotes.
Refer sample input and output for formatting specifications.
Sample Input 1:
ABCDE1234F
Sample Output 1:
Valid PAN Number

Sample Input 2:
12345ABCD3
Sample Output 2:
Invalid PAN Number
'''
import re

pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

def validatePAN(pan):
    if re.match(pattern, pan):
        return "Valid PAN Number"
    else:
        return "Invalid PAN Number"
    
inp = str(input())

print(validatePAN(inp))

# iasses
# 1
'''
Extract Names

Jack was a little boy, who was playing the game word puzzle. The jack brother gave him a task to find the nouns in a given set of lines. Try to help jack to finish his task.


Problem Constraints:
Use the re  module for Regular Expression
Use the findAll method

Extract all names from the given text. Use metacharacter
Rules:
1) only alphabets
2) starts with upper-case
3) may contain surnames
4) may contain initials

Input format:
A single line input string consists of capitalized words in it.

Output format:
The output will be the words which are obeying the mentioned rules


Sample Input 1:
S.Vinoth Kumar and John Watson are friends with James
Sample output 1:
S.Vinoth Kumar 
John Watson 
James

Sample Input 2:
there were two friends named Sam and Jason
Sample output 2:
Sam
Jason
'''
import re

def extractNames(text):
    pattern = r'\b([A-Z][a-z]*(?:\.[A-Z][a-z]*)*(?:\s[A-Z][a-z]+)*)\b'

    names = re.findall(pattern, text)

    return names

inp = str(input())

print("\n".join(extractNames(inp)))

# 2
'''
Ceaser Cipher Encryption


Ishan playing aa simple game with alphabets. the procedure will be Ishan choose aa random number in between (0-26) and then he changed the alphabets in Ceaser chipper(Each letter 'shifted'  wrt chosen number).
Image result for Caesar Cipher
So can you please help Ishan to write aa program for Ceaser cipher Encryption. Input and Output format Specifications are shown below.

Input Format Specifications:

The first line of Input contains a String.
The next line of input contains Integer N, N is the shifted positions number.
Replace all characters with the nth character from the current character.
 Must use "re.sub()".
Note: [" ord() expected a character, but a string of length 2 found" if the error shows like this then you use the lambda function ].

Output Format Specifications:

Output Consists of String.
if character addition is going greater than 127 then print ‘invalid’.
Sample Input and Output showed below.
Sample Input 1:
amphisoft
3
Sample Output 1:
dpsklvriw

Sample Input 2:
krishnamohan
27
Sample Output 2:
invalid
'''
def rotate(txt, key):
    def cipher(i, key):
        if i in range(32, 127):  # Considering all printable ASCII characters
            i = (i + key)
            if i > 127:
                return 'invalid'
        return chr(i)
    
    result = ''.join([cipher(ord(s), key) for s in txt])
    
    if 'invalid' in result:
        print('invalid')
    else:
        print(result)

txt = input()
key = int(input())
rotate(txt, key)

