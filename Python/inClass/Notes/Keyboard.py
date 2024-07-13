# input is a built on fx
# takes single paramater (caption/question)
# Input fx displays the caption to the user
# and wait for the keyboard input
# user will provide the input and press enter key
# the input is always "string"

firstNumber = input ("Enter the first number :")
secondNumber = input("Enter the second number :")

print(firstNumber)
print(type(firstNumber))

firstNumber = int(firstNumber)
secondNumber = int(input("Enter the second number :"))

print(firstNumber + secondNumber)
