# Mon       10/6/2024

# use 0b -->> to make computer read one one one zero zero one zero zero one
# instead of read as 111million and etc.
# filepermission = 711
# change into bin

filepermission = 0b111101001
# print(filepermission)         # automatically convert bin to dec and print it
print(bin(filepermission))     

# filepermission holds a binary number 
# interested in one bit not all
# interested in permission belongs to the group only (001)
# 4, 5, 6 bits only

# Feature Engineering (massaging the data) -->> get ready for machine to learn

mask = 0b000111000

# original data     111101001
# mask data         000111000
# result            000101000
# the '&' operator use to extract the bits interested 

# to shift from 000101000 into 000000101, use '>> 3'

print(bin((filepermission & mask) >> 3))

# to set 4, 5, 6 bits to 1
# the other bits remain then use or '|' operator  -->> add
# using | cannot set bits to 0
# original data     111010101
# mask data         000111000
# result            111111101

filepermission = 0b111010101
mask = 0b000111000
print(bin((filepermission | mask)))

# xor operator
#      and  or  xor
# 0 0   0   0    0
# 0 1   0   1    1
# 1 0   0   1    1
# 1 1   1   1    0

# to encrypt j using s

content = 0b10101010        # j
key = 0b00111100            # s

encryptedcontent = content ^ key
print(bin(encryptedcontent))  # -->> diff because dont have s

decryptedcontent = encryptedcontent ^ key

print(bin(decryptedcontent))

# 1's compliment = flip the bit from 1 to 0, or 0 to 1

givennumber = 5         # bin - 0101
print(bin(~givennumber)) # 1010
print(~givennumber)

# 2's compliment -->> get the 1's compliment and add 1
print(bin(~givennumber + 1))

#-------------------------------------------------------------#

# Tue 11/6/2024

# 1,2,3,4,5,6,7,8,9  A,  B,  C,  D,  E,  F, 10,11,12,13,14
#0,1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16
hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# 0,1,2,3,4,5,6,7,10,12,13,14,15,16,17,20
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))















