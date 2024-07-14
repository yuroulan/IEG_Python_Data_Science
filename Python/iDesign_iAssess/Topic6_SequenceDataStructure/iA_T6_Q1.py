# iassess

# 1

inp1 = input().split(',')
inp2 = input().split(',')

set1 = set(map(int, inp1))
set2 = set(map(int, inp2))

# to check if set1 is a subset of set2
isSet1 = set1.issubset(set2)
print(isSet1)

# to check if set2 is subset of set1
isSet2 = set2.issubset(set1)
print(isSet2)

# to check set1 is superset of set 2
isSet1 = set1.issuperset(set2)
print(isSet1)

# to check set2 is superset of set1
isSet2 = set2.issuperset(set1)
print(isSet2)
