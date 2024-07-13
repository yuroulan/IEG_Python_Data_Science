def outer():
    def inner():
        def innerInner():
            print("Hello World!")
        return innerInner
    return inner

func01 = outer()
func02 = func01()
func02()    # Hello World

func02()
outer()()()
print('-' * 50)

def organize(* funcs):
    for func in funcs:
        func()
        print('-' * 50)

def add():
    print(20 + 10)
    print('-' * 50)

def minus():
    print(20 - 10)
    print('-' * 50)

def mul():
    print(20 * 10)
    print('-' * 50)

def div():
    print(20 / 10)
    print('-' * 50)

# can pass any order to be executed
organize(add, minus, mul, div)
print('-' * 50)

organize(minus, mul, add, div)
print('-' * 50)














