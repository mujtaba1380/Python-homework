class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}: $ {self.price:.2f}"
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = []
    def add_item(self,item):
        self.menu.append(item)
    def remove_item(self,item_name):
        for item in self.menu:
            if item.name == item_name:
                self.menu.remove(item)
                print(f"Removed {item_name} from the menu.")
    def disply_menu(self):
        print(f"Menu of {self.name}:")
        for item in self.menu:
            print(f"-{item}")
item1 = Item("Pasta",8.99)
item2 = Item("Pizza",12.50)
item3 = Item("Salad",6.75)
restaurant = Restaurant("Naseeb Restaurant")
restaurant.add_item(item1)
restaurant.add_item(item2)
restaurant.add_item(item3)
restaurant.disply_menu()
restaurant.remove_item("Pizza")
restaurant.disply_menu()