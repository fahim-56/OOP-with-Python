class paternal_famaly:
    def __init__(self,surnameP):
        self.surnameP = surnameP

    def legacy_from_PF(self):
        print(f"You Got Everything from {self.surnameP} family...")
    

class maternal_family:
    def __init__(self,surname):
        self.surname = surname

    def legacy_from_MF(self):
        print(f"You Got Nothing from {self.surname} family...")

class child(paternal_famaly,maternal_family):
    def __init__(self, paternal_famaly_surname,maternal_family_surname):
        paternal_famaly.__init__(self,paternal_famaly_surname)
        maternal_family.__init__(self,maternal_family_surname)

    def Family_Identity(self,name,surname1,surname2):
        return (f"You are {surname2} {name} {surname1}")


me = child("Chowdhury","Khandokar")

print(me.Family_Identity("Fahim","Chowdhury","Khandokar"))

me.legacy_from_PF()
me.legacy_from_MF()