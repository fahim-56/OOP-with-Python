class parrent:
    def __init__(self):
        pass

class child(parrent):
    def __init__(self):
        super().__init__()

class child2:
    def __init__(self):
        pass


print(issubclass(child,parrent)) 
print(issubclass(child2,parrent))
print(issubclass(parrent,child))