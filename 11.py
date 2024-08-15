class Account:
    def __init__(self,initial_balance = 0):
        self.__balance = initial_balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("deposite amount:",amount)
        else:
            print("can be positive!")
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("with drawn:",amount)
        else:
            print("not exist enough amount")
    def get_balance(self):
        return self.__balance
account = Account(1000)
account.deposit(200)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())