class student:
    def __init__(self,name,id,batch):
        self.name= name
        self.id= id
        self.batch = batch
    
    def __repr__(self):
        return f"Name : {self.name} ID : {self.id} Batch : {self.batch}"

        

class Teacher :

    def __init__(self,name,dept,id):
        self.name = name
        self.id = id 
        self.dept = dept

    def __repr__(self):
        return f"Name : {self.name} ID : {self.id} Batch : {self.dept}"

class University:

    def __init__(self,name):
        self.name = name
        self.teachers =[]
        self.students =[]

    def add_Teacher(self,name,dept):
        id = len(self.teachers)+101
        teacher = Teacher(name,dept,id)
        self.teachers.append(teacher)
        print(f"{name}'s Joined {self.name}... {name}'s id is {id}")


    def enroll_student(self,name,fee):
        if(fee<50000):
            print( f"{name}'s payment is not sufficient")
            return
        id = len(self.students)+2215100
        self.students.append(student(name,id,51))
        print(f"{name}'s Enrollment done... {name}'s id is {id}")
        return
    
    def __repr__(self):
        print("\n\nName of University ",self.name,"\n")
        print("---Our Teachers---\n")
        for i in self.teachers:
            print(i)
        print("\n---Our Students---\n")
        for i in self.students:
            print(i)
        return f"All Valid Entities"


uni= University("UITS")

uni.add_Teacher("Sakib Sir","IT")
uni.add_Teacher("Imteaj Sir","CSE")


uni.enroll_student("Fahim",60000)
uni.enroll_student("kawshik",20000)
uni.enroll_student("Tonmoy",50000)

print(uni)