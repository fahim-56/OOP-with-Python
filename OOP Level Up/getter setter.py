class employee:
    def __init__(self,name,age,salary):
        self._name = name 
        self._age = age
        self.__salary = salary

    def name(self):
        return self._name
    #getter with out setter read only
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__salary
    # setter
    @salary.setter
    def salary(self,value):
        if(value < 0):
            return f"Salary must be positive"
        self.__salary += value

fahim = employee("Fahim",23,80000)
print(fahim._name)
print(fahim._age)
# print(fahim.__salary) # private property

print(fahim.name())
print(fahim.age)
print(fahim.salary)

fahim.salary = 5000
print(fahim.salary)