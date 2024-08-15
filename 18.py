class Team:
    def __init__(self,name):
        self.__name = name
        self.__members = []
    def add_member(self,mem_name):
        self.__members.append(mem_name)
        print("succesfully added!")
    def remove_member(self,mem_name):
        self.__members.remove(mem_name)
        print("succesfully removed from list")
    def show_members(self):
        return self.__members
team1 = Team("Ahmadi")
team1.add_member("Ali")
team1.add_member("mujtaba")
team1.add_member("mohammad")
print(team1.show_members())