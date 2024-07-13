'''
1) required arguments
2) keyword arguments
3) default arguments
4) variable-lengthed arguments
'''

'''
def sum(a, b):
    print("a =", a)
    print("b =", b)
    c = a + b
    return c

x = 5
y = 10
d = sum(a=x, b=y)
print(d)
'''

'''
def sum(a, b = 10):
    c = a + b
    return c

x = 5
c = sum(x)
print("sum = ", c)
d = sum(x, 20)
print("sum = ", d)
'''

'''def sum(a = 5, b = 10, d = 20, e = 30):
    c = a + b + d + e
    return c

print(sum())
print(sum(50))
print(sum(50, 100))
print(sum(50, 100, 200))
print(sum(50, 100, 200, 300))

65
110
200
380
650
'''

'''def sum(a = 5, b = 10, d = 20, e = 30):
    c = a + b + d + e
    return c

print(sum())
print(sum(50, b = 50))
print(sum(50, e = 100))
print(sum(50, 100, 200))
print(sum(50, 100, 200, 300))

65
150
180
380
650
'''
'''
def sum(b, c, *a):
    print(a)
    print(type(a))
    print("b = ", b)
    print("c = ", c)
d = sum(1,2,3,4,5,6,7,8,9,10)
print("d = ", d)

(3, 4, 5, 6, 7, 8, 9, 10)
<class 'tuple'>
b =  1
c =  2
d =  None
'''

'''
def sumMarks(rno, name, *marks):
    print("roll number : ", rno)
    print("Name : ", name)
    print("Marks : ", marks)
    print(type(marks))
    print("Total : ", sum(marks))

d = sumMarks(1, "JK", 90, 95, 94, 99, 100)
print("d = ", d)
'''

'''
def fun(l1):
    l1 = [3,4,5,6]
    print(l1)
    return l1

l = [1,2,3,4]
print(l)
fun(l)
print(l)

[1, 2, 3, 4]
[3, 4, 5, 6]
[1, 2, 3, 4]

def fun(l1):
    l1 = [3,4,5,6]
    print(l1)
    return l1

l = [1,2,3,4]
print(l)
l = fun(l)
print(l)

[1, 2, 3, 4]
[3, 4, 5, 6]
[3, 4, 5, 6]
'''

def fun(l1):
    l1.append(7)
    print(l1)

l = [1,2,3,4]
print(l)
fun(l)
print(l)

[1, 2, 3, 4]
[1, 2, 3, 4, 7]
[1, 2, 3, 4, 7]
















