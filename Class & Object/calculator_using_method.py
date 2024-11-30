from operator import *

class calculator:
    brand="Casio"

    def add(self,*args):
        value = sum(args)
        return(value)
    def sub(self,num1,num2):
        value = sub(num1,num2)
        return value
    def mul(self,num1,num2):
        value=mul(num1,num2)
        return value
    def div(self,num1,num2):
        value=truediv(num1,num2)
        return value
    
    
calculate=calculator()

print(calculate.add(10,20,20))
print(calculate.sub(20,10))
print(calculate.mul(20,10))
print(calculate.div(15,10))