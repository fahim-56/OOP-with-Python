class shoping:
    # static attribute
    cart =[]
    origin ="Bangladesh"
    def __init__(self,mall_name,location):
        self.mall_name = mall_name # instance attribute
        self.location = location
    def parcheses(self,item,price):
        print (f"You have parcheses {item} for {price} taka")
   

