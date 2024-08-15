class Ticket:
    def __init__(self,movie_name,seat_number,price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
    def disply_details(self):
        print("Movie Name:",self.movie_name,"\nSeat Number:",self.seat_number,"\nPrice:",str(self.price) + "$")
    def apply_discount(self,discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = self.price * (discount_percentage/100)
            self.price -= discount_amount
        else:
            return "please chose discount percentage between 0 to 100"
ticket1 = Ticket("inception","A12",15.00)
ticket1.apply_discount(20)
ticket1.disply_details()