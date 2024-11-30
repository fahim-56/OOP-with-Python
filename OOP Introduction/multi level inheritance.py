class vehicle:
    def __init__(self,company_name,number):
        self.company_name = company_name
        self.number = number

    def trip(self,starting,ending):
        return f"A trip from {starting} to {ending}"
            
    def __repr__(self):
        return f"To confirm your rent please pay first..."
    
    
class bus(vehicle):
    def __init__(self, company_name, number,capacity, rent_price):
        self.capacity = capacity
        self.rent_price =rent_price
        super().__init__(company_name,number)

    def available_seat(self,passenger):
        return f"{self.capacity - passenger} Seat are available..."
    
    def __repr__(self):
        return super().__repr__()

class delivary_truck(vehicle):
    def __init__(self, company_name, number,weigt_capacity):
        self.weigt_capacity = weigt_capacity
        super().__init__(company_name,number)

    def delivary_information(self,recieved_address,unload_address,prduct):
        self.recieved_address =recieved_address
        self.unload_address = unload_address
        self.product = prduct

    def __repr__(self):
        return super().__repr__()

class student_bus(bus):
    def __init__(self, company_name, number, capacity, rent_price,bus_number):
        self.bus_number = bus_number
        super().__init__(company_name, number, capacity, rent_price)
    
    def __repr__(self):
        return super().__repr__()
    

our_bus = student_bus("Jani na","21DH21",50,50000,4)

print(our_bus.available_seat(30))
print(our_bus)