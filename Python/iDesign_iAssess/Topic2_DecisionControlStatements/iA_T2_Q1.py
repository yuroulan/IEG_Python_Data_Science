# iassess
'''
Card Game
The Westland Game Fair is the premier event of its kind for kids interested in some intellectual and cognitive brain games. Alan, a middle school boy is visiting the fair where he is very much drawn by the Card game.

The game’s rules are:
A player needs to pick 3 cards from a big lot of cards. There are 4 types of Cards namely Spade(S), Heart(H), Club(C) and Diamond (D). If all the 3 cards that the player picks are of the same type and same number, they get a Double Bonanza. If all the 3 cards are of the same type or if they all have the same number, they get a Bonanza. Otherwise they do not get a Bonanza. Alan has now picked 3 cards and is awaiting to know if he has got a bonanza. Please help him to know if he has won the Bonanza or not.

Input Format:
There are 3 lines of input.
Each of the line consists of character and integer input, which corresponds to the type of the card and the number in it that Alan picked. The type of card and the number are separated by a single space.

Output Format:
Output should display "Double Bonanza" or "Bonanza" or "No Bonanza" based on the conditions given.
Refer sample input and output for formatting specifications.

Sample Input 1:
S 5
S 5
S 5

Sample Output 1:
Double Bonanza

Sample Input 2:
S 6
S 5
H 5

Sample Output 2:
No Bonanza
'''

cards1 = input()
cards2 = input()
cards3 = input()

cards1 = cards1.split(" ")
cards2 = cards2.split(" ")
cards3 = cards3.split(" ")

# types of card (S, H, C, D)

type1, num1 = cards1[0] , cards1[1]
type2, num2 = cards2[0] , cards2[1]
type3, num3 = cards3[0] , cards3[1]

if(type1 and type2 and type3):
    print("Double Bonanza")
elif(type1 or type2 or type3):
    print("Bonanza")
else:
    print("No Bonanza")