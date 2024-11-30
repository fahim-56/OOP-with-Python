class laptop:
     
    def __init__(self,brand,memory,processor):
        self.brand = brand
        self.memory = memory
        self.processor = processor

    def run (self):
        return f"I am running..."
    
    def compute(self):
        return f"I am computing..."
    
class phone:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def run (self):
        return f"I am running..."
    
    def calling(self,number,):
        return f"I am calling {number}..."

class Camera:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def run (self):
        return f"I am running..."
    
    def capturing(self):
        return f"Captured..."
