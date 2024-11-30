class CPU:
    def __init__(self,core):
        self.core = core

class RAM:
    def __init__(self,size):
        self.size = size

class Harddrive:
    def __init__(self,capacity):
        self.capacity = capacity


# computer has a CPU    
# computer has a RAM    
# computer has a Harddrive
    
class Computer:
    def __init__(self,core,capacity,size):
        self.cpu = CPU(core)
        self.ram = RAM(size)
        self.harddrive = Harddrive(capacity)
mycomputer = Computer(7,512,16)