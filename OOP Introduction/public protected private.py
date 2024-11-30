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
        return f"{amount} taka added to your account successfully.\nYour current account balance is {self.__balance} taka"
        
    def withdraw(self,id,password,amount):
        if(self.__balance < amount):
            return f"Your account balance is not sufficient."
        if self.id == id and self.__password == password:
            self.__balance -= amount
            return f"Withdraw {amount} taka Successfully. \nYour current account balance is {self.__balance} taka"
        return f"Wrong information..."
    
    def balance_check(self,id,password):
        if self.id == id and self.__password == password:
            return(f"Your current account balance is {self.__balance}taka")
        return f"Wrong information..."

customer1 = Islami_Bank_account("Fahim",10000,"password1")
customer2 = Islami_Bank_account("Kawshik",10000,"password2")

# print(customer1.__password) # dekhte parbo na

# print(customer1.balance_check(10001,"password"))
print(customer1.balance_check(10001,"password1"))
print(customer1.deposite(10000))
print(customer1.balance_check(10001,"password1"))

print(customer2.balance_check(10001,"password2"))
print(customer2.deposite(15000))
print(customer2.balance_check(10002,"password2"))