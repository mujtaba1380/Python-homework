class Vehicle:
    def Drive(self):
        print("this drive method in vehicle class.")
class Bike(Vehicle):
    def Drive(self):
        print("Riding the bike!")
class Truck(Vehicle):
    def Drive(self):
        print("Driving the truck!")
bike = Bike()
bike.Drive()
truck = Truck()
truck.Drive()
