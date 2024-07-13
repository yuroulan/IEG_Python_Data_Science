# use any of built in python module,
# import inside program
# does not loaded automatically when python gets loaded
# must import if want to use
# import modulename
# cmd line argument always string type

import sys
print(sys.argv)

for value in sys.argv:
    print(value)

# how many argument (use len)
print(len(sys.argv) - 1)

# to perform addition
total = 0
for value in sys.argv[1:]:
    total = total + int(value)
print("Total : " , total)

# parsing








