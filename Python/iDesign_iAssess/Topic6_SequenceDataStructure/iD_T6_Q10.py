# Problem 10
'''
Word Count
Harry studies in HNJ school and his medium of instruction is English. 
His English teacher taught him to form sentences. 
Harry loves Mathematics as well. He wants to link Mathematics with English. 
As a first step, he wishes to count the number of occurrences of words in a sentence.

Develop a python program to help Harry to finish the task.

Input Format:

Read a sentence from the user

Output Format:

Display the number of occurrences of words in the sentence. 

Refer sample output.

Sample Input 1:

the the function using dict dict

Sample Output 1:

{'the': 2, 'function': 1, 'using': 1, 'dict': 2}
'''

sentences = input()

words = sentences.split()

wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print(wordCount)


