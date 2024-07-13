def keyboardInp(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def calSimpInt():
    principle = keyboardInp(int, "Principle amount : ", "Principle amount must be integer.")
    period = keyboardInp(float, "Period in years : ", "Period must be float.")
    rate = keyboardInp(float, "Rate in percentage : ", "Rate must be float.")

    interest = (principle * period * rate) / 100

    print("Interest amount : ", interest)
    print("Total amount to be paid : ", principle + interest)


calSimpInt()

# myList = ['1', '2', '3']
# map(int, myList)

















try:
    principal = int(input("Principle: "))    # usually an input
except ValueError:
    # will only get executed when error occurs
    print("Principle amount must be integer. exp = 1000")
except Exception as e:
    print("Something went wrong : ", e)
else:
    # the code inside the else block gets executed 
    # only when there is no error
    print("All is well.")
finally:
    # The code inside this block will always get executed
    # regardless of wether an error occurs or not
    print("Thank You.")

period = int(input("period: "))
rate = int(input("Rate: "))
interest = (principal * period * rate) / 100
print(interest)