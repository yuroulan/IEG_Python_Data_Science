# Question 5

''' 
Tile Game
In connection to the National Mathematics Day celebration, the Regional Mathematical Scholars Society had arranged for a Mathematics Challenge Event where school kids participated in large number. Many interesting math games were conducted, one such game that attracted most kids was the tile game where the kids were given 'n' square tiles of the same size and were asked to form the largest possible square using those tiles.

Help the kids by writing a program to find the area of the largest possible square that can be formed, given the side of a square tile (in cms) and the number of square tiles available.

Input Format:
First line of the input is an integer that corresponds to the side of a square tile (in cms).
Second line of the input is an integer that corresponds to the number of square tiles available.

Output Format:
Output should display the area of the largest possible square that can be formed (in square cms) with the available tiles.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output :
Enter the side in cm of a square tile
5
Enter the number of square tiles available
8
Area of the largest possible square is 100sqcm 
'''

# to know the largest possible square using tiles given
# let say sides of tile is 5cm 
# when tiles has 4, the sides is 5 + 5 = 10cm
# 10 cm (vertical) , 10cm (horizontal)

sideSqr = int(input("Enter the side in cm of a square tile"))   # 5cm
numTiles = int(input("Enter the number of square tiles available"))  # 8 tiles
sqrt = int(numTiles  ** (1/2))

sides = int((sideSqr * sqrt) ** 2)

print(f"Area of the largest possible square is {sides} sqcm")