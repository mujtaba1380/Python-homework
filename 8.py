class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,department,name,salary):
        super().__init__(name,salary)
        self.department = department
    def disply(self):
        print(self.department,"Department",self.name,"| salary :", self.salary)
ma = Manager("English","Ashraf Azad",10000)
ma.disply()