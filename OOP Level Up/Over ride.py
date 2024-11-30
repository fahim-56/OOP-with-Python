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

fahim = programer("Fahim",22,78,90,"Python")
fahim.sleep()
fahim.eat()