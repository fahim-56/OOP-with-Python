class customer:
    cart=[]

    def __init__(self,name):
        self.name=name
    def add_to_cart(self,item):
        self.cart.append(item)
        print(f"{item} added to cart")

customer1=customer("Fahim")
customer2=customer("Tonmoy")

customer1.add_to_cart("Sirah")
customer2.add_to_cart("Tafseer")

print(customer1.cart)
print(customer2.cart)