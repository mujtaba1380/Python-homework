class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
class Fight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []
    def add_passenger(self,person):
        self.passengers.append(person)
    def remove_passenger(self,person_name):
        for person in self.passengers:
            if person.name == person_name:
                self.passengers.remove(person)
    def disply_passengers(self):
        print(f"Passengers of flight {self.flight_number} to {self.destination}:")
        for person in self.passengers:
            print(f"-{person}")
person1 = Person("Ahmad",20)
person2 = Person("Mujtaba",23)
person3 = Person("Eqbal",27)
flight = Fight("AB123","New York")
flight.add_passenger(person1)
flight.add_passenger(person2)
flight.add_passenger(person3)
flight.disply_passengers()
flight.remove_passenger("Eqbal")
flight.disply_passengers()
