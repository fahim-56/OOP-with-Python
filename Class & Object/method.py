class person():
    name="Fahim"
    age=22
    address="Rajbari"

    def can_do_coding(self): #default parameter
        print("Yes,I can")
    def mailing(self,number,text):
        print(f'Sent {text} to {number}')

Me=person()
print(Me.name)  
print(Me.address)  
Me.can_do_coding()
Me.mailing('0191027456',"Assalamualaikum...")