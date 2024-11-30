# inhariting the code of Gadget file
class device:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def run (self):
        return f"I am running..."
    
class laptop(device):
    def __init__(self, brand, price, memory,processor,ssd):
        self.memory = memory
        self.processor = processor
        self.ssd = ssd
        super().__init__(brand, price)

class phone(device):
    def __init__(self, brand, price, number):
        self.number = number
        super().__init__(brand,price)
    
    def calling(self,number,):
        return f"I am calling {number}..."

class Camera(device):
    def __init__(self, brand, price,pixel):
        self.pixel = pixel
        super().__init__(brand, price)
    
    def capturing(self):
        return f"Captured..."

myphone = phone("Sony",55000,"+8801...")


print(myphone.brand)

print(myphone.calling("+8801..."))

print(myphone.run())