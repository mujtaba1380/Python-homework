class Bird:
    def Fly(self):
        pass
class Eagle(Bird):
    def Fly(self):
        print("Eagle can fly.")
class Penguin(Bird):
    def Fly(self):
        print("penguin cannot fly.")
eagle = Eagle()
eagle.Fly()
penguin = Penguin()
penguin.Fly()
