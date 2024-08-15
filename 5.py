class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def compute_area(self):
        return self.lenght * self.width
rect = Rectangle(5,3)
area = rect.compute_area()
print("the rectangle area is:",area)