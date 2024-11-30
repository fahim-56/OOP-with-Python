import math 
import time

def timer(func):
    def fun(*args,**kargs):
        print(time.time())
        func(*args)
        print(time.time())
    return fun

@timer
def factorial(n):
    print(math.factorial(n))

factorial(5)