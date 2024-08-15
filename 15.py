class Student:
    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    def get_name(self):
        return self.__name
    def get_grade(self):
        return self.__grade
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def set_grade(self,grade):
        self.__grade = grade
    def set_age(self,age):
        self.__age = age
    def show_detail(self):
        print("Name:",self.__name,"| Grade:",self.__grade,"| Age:",self.__age)

stu = Student("Mujtaba","bacaloria",23)
stu.show_detail()