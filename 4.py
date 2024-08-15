class Circle:
    def __init__(self,radius):
        self.radius = radius
    def compute_area(self):
        return (3.14 * self.radius ** 2)
circle1 = Circle(5)
area = circle1.compute_area()
print("The circle area is:",area)