class Bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("amount can be positive!")
    def withdrawn(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("not exist enough money!")
    def check(self):
        print("Your Balance is:",self.__balance)

account = Bankaccount(2324,3000)
account.deposit(2000)
account.withdrawn(1000)
account.check()
