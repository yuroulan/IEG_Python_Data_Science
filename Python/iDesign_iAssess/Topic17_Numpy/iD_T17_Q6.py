# Problem 6
'''
Dice Rolls

A six sided die was rolled many times and the results of the rolls were saved to a numpy array called dice_rolls. How many times was a roll greater than 2 rolled? In other words, how many of the integers in the dice_rolls array are greater than 2?Can you write a Python program to solve the above problem?

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :
Enter the number of dice rolls
3
Enter the value of each dice roll
1
2
3
Dice rolls greater than 2
1
'''
import numpy as np

diceRoll = int(input("Enter the number of dice rolls\n"))

print("Enter the value of each dice roll")

rolls = []
for _ in range(diceRoll):
    roll = int(input())
    rolls.append(roll)

rolls = np.array(rolls)

greaterRolls = np.sum(rolls > 2)

print("Dice rolls greater than 2")
print(greaterRolls)