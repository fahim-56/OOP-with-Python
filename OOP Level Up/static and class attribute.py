class shoping:
    # static attribute
    cart =[]
    origin ="Bangladesh"
    def __init__(self,mall_name,location):
        self.mall_name = mall_name # instance attribute
        self.location = location
    def parcheses(self,item,price):
        print (f"You have parcheses {item} for {price} taka")
    @staticmethod
    def check_out(amount,price):
        reminder = amount - price
        print(f"Your reminder {reminder}")
    @classmethod
    def veiw(self,item):
        print(f"Tell me about the quality of {item} of {self.origin}")
    

shoping.parcheses(2,"Cake",30)
#class methood
shoping.veiw("Lungi")
#static medhood
shoping.check_out(1000,500)