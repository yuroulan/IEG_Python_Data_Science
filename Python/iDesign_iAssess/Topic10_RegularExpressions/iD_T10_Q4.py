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