def outer_function():
    print("Outer function start")
    def inner_function():
        print("Inner function start")
        
    return inner_function()

outer_function()

def outer_function2():
    print("Outer function2 start")
    def inner_function2():
        print("Inner function2 start")
        
    return inner_function2

outer_function2()()

def do(work):
    print("Ready")
    work()
    print("Ending")
def coding():
    print("Coding")

do(coding)