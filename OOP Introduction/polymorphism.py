from math import pi

class shape:

    def __init__(self):
        pass

    def area(self):
        return f"You haven't declear any shape yet!"

class rectangle(shape):

    def __init__(self, length ,width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.length * self.width

class circle(shape):

    def __init__(self, redius):
        self.redius = redius
        super().__init__()

    def area(self):
        return pi * self.redius**2

class triangle(shape):

    def __init__(self, base, height ):
        self.base = base
        self.height = height

    def area(self):
        return (1/2)* self.base * self.height

rt = rectangle(5,4)
print(rt.area())

cr = circle(10)
print(cr.area())

tr = triangle(5,4)
print(tr.area())