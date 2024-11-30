class person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.wieght = weight
        pass
    def sleep(self):
        print("Sleep at night.")

    def eat(self):
        raise NotImplementedError

class programer(person):

    def __init__(self, name, age, height, weight, skill):
        self.skill = skill
        super().__init__(name, age, height, weight)

    def sleep(self):
        print("Sleep before contest.")

    def eat(self):
        print("eat regular food")

    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.height * other.height
    
    def __len__(self):
        return self.height
    
    def __gt__(self,other):
        return self.age > other.age

fahim = programer("Fahim",22,6,90,"Python")
tonmoy = programer("Tonmoy",23,6,90,"Python")

# + over loading
print(5+2)
print("Fahim"+" Chowdhury")
print([2,3]+[4,5,6])

print(fahim+tonmoy)
print(fahim*tonmoy)
print(len(fahim))
print(fahim<tonmoy)