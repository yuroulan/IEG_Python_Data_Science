# Problem 4
'''
Write a program that prompts users to enter numbers till he enters one positive number. Whenever the user enters a negative number or a string , raise a ValueError exception and handle it appropriately and display the message shown in the sample output.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

 

Sample Input and Output 1:

Enter a positive integer

5

Good! You entered 5

 

Sample Input and Output 2:

Enter a positive integer

-6

You entered a negative number. Retry!

Enter a positive integer

-9

You entered a negative number. Retry!

Enter a positive integer

3

Good! You entered 3
'''
def getPositiveInt():

    while True:
        try:
            posInt = (input("Enter a positive integer\n"))

            num = int(posInt)

            if num <= 0:
                raise ValueError("You entered a negative number. Retry!")
            else:
                print(f"Good! You entered {num}")
                break

        except ValueError as e:
            print(e)
            print("")


getPositiveInt()