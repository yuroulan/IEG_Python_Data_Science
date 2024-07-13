# concept of Adam number is when value put reversed, 
# the square of value and reversed value is same

print("Please put any value to check Adam number.")

num = int(input("Your value is : "))

num1 = num ** 2                                                 # 169
print(f"The square value for {num} is : " , num1)

if(num >= 100 and num <= 999):       # for 3 digits
    # let say num = 113
    # to reverse num = 311

    num1 = num ** 2                                        # 12769
    divNum1 = num // 10                                    # 113 // 10 = 11
    remNum1 = (num % 10) * 100                             # 113 % 10 * 100 = 300
    
    divNum2 = (divNum1 // 10)                               # 11 // 10 = 1
    remNum2 = (divNum1 % 10) * 10                           # 11 % 10 * 10 = 10

    divNum3 = (divNum2 // 10)                               # 1 // 10 = 0
    remNum3 = (divNum2 % 10)                                # 1 % 10 = 1

    remNum = remNum1 + remNum2 + remNum3                    # 300 + 10 + 1
    print(f"The reverse value for {num} is : " , remNum)    # 311                                       # 311

    # sqrRevNum = 311 ** 2 = 96721
    sqrRevNum = remNum ** 2                                    # 311 ** 2 = 96721
    print(f"The square value for {remNum} is : " , sqrRevNum)  # 96721

    adNum = 0

    # To re-reverse the sqrRevNum = 96721 = 12769
    reRevNum1 = sqrRevNum // 10                                 # 9672
    # print(reRevNum1)
    reRevRem1 = (sqrRevNum % 10) * 10000                        #  1 = 10000
    # (0 * 10) + (96721 % 10) = 1
    # print(reRevRem1)

    reRevNum2 = reRevNum1 // 10                                 # 967
    # print(reRevNum2)
    reRevRem2 = (reRevNum1 % 10) * 1000                         # 2 = 2000
    # print(reRevRem2)

    reRevNum3 = reRevNum2 // 10                                 # 96
    # print(reRevNum3)
    reRevRem3 = (reRevNum2 % 10) * 100                          # 7 = 700
    # print(reRevRem3)

    reRevNum4 = reRevNum3 // 10                                 # 9
    # print(reRevNum3)
    reRevRem4 = (reRevNum3 % 10) * 10                           # 6 = 60
    # print(reRevRem4)

    reRevNum5 = reRevNum4 // 10                                 # 0
    # print(reRevNum3)
    reRevRem5 = (reRevNum4 % 10)                                # 9
    # print(reRevRem5)

    reRevNum = reRevRem1 + reRevRem2 + reRevRem3 + reRevRem4 + reRevRem5
    # = 10000 + 2000 + 700 + 60 + 9

    print(f"The reverse square for {sqrRevNum} is : " , reRevNum)

    print(f"""The square of {num} and square of reverse of {num} are reverse of each other. 
Therefore {num} is Adam number.""")
else:
    print(f"The {num} is not Adam Number.")