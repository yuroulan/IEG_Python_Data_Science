# Problem 4
'''
Module: Word Count
Teacher organize a debate competition, In order to check the student's talking skills, she will write a list of topics in cards, student has to pick one of the cards then she wants to group the student based on the topics they have selected  and she will name the group based on the topic's name.
Now help her to find a number of students in each group.

Input Format:
The first line of input is a string consists of lower case letter words  (each word will indicate topics selected by the student)


Output Format:
The output consists of a count of each word.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output:
mother father mother GST father GST facebook facebook GST
facebook-2
father-2
gst-3
mother-2
'''
def main():
    inpStr = input("Enter the String\n").lower().split()
    toCount = {}

    for topic in inpStr:
        if topic in toCount:
            toCount[topic] += 1
        else:
            toCount[topic] = 1

    for topic in sorted(toCount):
        print(f"{topic}-{toCount[topic]}")

if __name__ == '__main__':
    main()