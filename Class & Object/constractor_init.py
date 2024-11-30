class person:
    
    type = "user"
    def __init__(self,name,address,age):
        self.name = name
        self.address = address
        self.boyos = age

    def send_Mail(self,number,mail):
        print(f"Sent {mail} to {number}")

me = person("Fahim Chowdhury","Rahbari",22)
abbu=person("Ashraf Hossain Chowdhury","Rajbari",65)

print("Amr details",me.name,me.boyos,me.address)
print(f"Abbur details {abbu.name} {abbu.boyos} {abbu.address}")