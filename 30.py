class Room:
    def __init__(self,room_number):
        self.room_number = room_number
        self.is_occupied = False

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"Room {self.room_number}: {status}"
class Hotel:
    def __init__(self,name):
        self.name = name
        self.rooms = []
    def add_room(self,room):
        self.rooms.append(room)
    def book_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_occupied:
                    room.is_occupied = True
    def checkout_room(self,room_number):
        for room in self.rooms:
            if room.is_occupied:
                room.is_occupied = False
    def disply_rooms(self):
        for room in self.rooms:
            print(room)
room1 = Room(101)
room2 = Room(102)
room3 = Room(103)

hotel = Hotel("Grand Hotel")
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)
hotel.disply_rooms()
hotel.book_room(101)
hotel.book_room(102)
hotel.disply_rooms()
hotel.checkout_room(101)
hotel.checkout_room(102)
hotel.disply_rooms()