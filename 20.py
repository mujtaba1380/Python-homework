class Zoo:
    def __init__(self,name):
        self.__name = name
        self.__animals = []
    def add_animal(self,anim_name):
        self.__animals.append(anim_name)
        print("succesfully added!")
    def remove_animal(self,anim_name):
        self.__animals.append(anim_name)
        print("succesfully removed!")
    def show_animals(self):
        return self.__animals
zoo1 = Zoo("Kabul")
zoo1.add_animal("Lion")
zoo1.add_animal("Monkey")
zoo1.add_animal("Bear")
print(zoo1.show_animals())