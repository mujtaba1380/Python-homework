class Laptop:
    def __init__(self,Brand,Model,Price):
        self.__brand = Brand
        self.__model = Model
        self.__price = Price
    def Discount(self,discount):
        if 0 <= discount <= 100:
            discount_amount = self.__price * (discount/100)
            print("discount amount : ",discount_amount)
        else:
            print("discount can be between 0 to 100!")
    def disply(self):
        print("Brand  ", "Model  ", "Price")
        print(self.__brand,"| ",self.__model,"| ",self.__price)

lap = Laptop("dell","xps 15",300)
lap.disply()