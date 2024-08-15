class Shape:
    def area(self):
        print("this is the shape area.")
class Square(Shape):
    def area(self,side):
        print("the square area is:",side * side)
class Tringle(Shape):
    def area(self,base,height):
        print("the tringle area is:",(base * height)/2)

square = Square()
square.area(4)
tringle = Tringle()
tringle.area(4,6)