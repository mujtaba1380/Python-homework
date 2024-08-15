class School:
    def __init__(self,name):
        self.__name = name
        self.__students = []
    def add_student(self,stu_name):
        self.__students.append(stu_name)
        print("succesfully added!")
    def remove_student(self,stu_name):
        self.__students.remove(stu_name)
        print("succesfully removed in list!")
    def show_students(self):
        return self.__students
sch = School("Sayed Yusuf elmi HIGH SCHOOL")
sch.add_student("Mujtaba")
sch.add_student("Emal")
sch.add_student("Shahzad")
print(sch.show_students())
