class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}: $ {self.price:.2f}"
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
    def disply_item(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart Item:")
            for item in self.items:
                print(f"-{item}")
item1 = Item("Apple",0.99)
item2 = Item("Banana",0.59)
item3 = Item("Milk",1.49)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
cart.disply_item()
cart.remove_item("Banana")
cart.disply_item()
cart.remove_item("orange")
cart.disply_item()
