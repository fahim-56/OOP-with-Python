## encaptulation means hiding the infor mations...

class Islami_Bank_account:
    accounts_list = []

    def __init__(self,name,diposite,password):
        self.bank_name = 'Islami Bank'     #public
        self._name = name                  #protected (imagine)
        self.__balance = diposite          #private
        self.__password = password         #private
        self.id = len(self.accounts_list) + 10001
        self.accounts_list.append(self._name)
        
    def deposite(self,amount):
        self.__balance += amount
        
    def withdraw(self,id,password,amount):
        if(self.__balance < amount):
            return f"Your account balance is not sufficient."
        if self.id == id and self.__password == password:
            self.__balance -= amount

customer1 = Islami_Bank_account("Fahim",10000,"password1")
customer2 = Islami_Bank_account("Kawshik",10000,"password2")

customer1.deposite(10000)

customer2.deposite(15000)
customer2.withdraw(20000)
