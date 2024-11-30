class singleton:
    __instance = None
    def __init__(self):
        if singleton.__instance == None:
            singleton.__instance = self

        else:
            raise Exception("Already have an instance")
    
    @staticmethod
    def get_instance():
        if singleton.__instance == None:
            return singleton()
        else:
            return singleton.__instance
        
first = singleton.get_instance()
second = singleton.get_instance()
third = singleton.get_instance()

print(first)
print(second)
print(third)

any = singleton()