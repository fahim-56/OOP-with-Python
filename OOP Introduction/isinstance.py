class parrent:
    def __init__(self):
        pass

class child(parrent):
    def __init__(self):
        super().__init__()

class child2:
    def __init__(self):
        pass
P = parrent()
C = child()

print(isinstance(child,parrent)) 
print(isinstance(child2,parrent))
print(isinstance(parrent,child))

print(isinstance(P,child))
print(isinstance(P,parrent))