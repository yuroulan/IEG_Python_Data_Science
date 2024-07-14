# Problem 5
'''
Type Error Exception
Saurav is coach of ABC school cricket team. His team captain not performing well from last few matches. So, coach wants to find the batting average of his captain.
Thus, write a program to find the batting average of his captain, for given 'n' matches.

This program may generate Type Error exception, if there is a type mismatch when rating is got as input. Use exception handling mechanisms to handle this exception. 
  
Input and Output Format: 
Refer sample input and output for formatting specifications.
Batting average should be rounded off to two decimal places.

Note: All text in bold corresponds to input and the rest corresponds to output. 
  
Sample Input and Output 1: 
Enter the number of matches
4 
Enter the scores
34
12
24
20
Batting average: 22.50

Sample Input and Output 2: 
Enter the number of matches
2 
Enter the scores
10
r 
Type Error Exception
'''
try:
    matchesNum = int(input("Enter the number of matches\n"))  
    
    print("Enter the scores")
    scores = []
    for _ in range(matchesNum):
        score = input()
        scores.append(int(score))

    totRuns = sum(scores)
    battAvg = totRuns / matchesNum

    print(f"Batting average: {battAvg:.2f}")  

except ValueError:
    print("Type Error Exception")
except TypeError:
    print("Type Error Exception: Invalid type conversion")
except Exception as e:
    print(e)