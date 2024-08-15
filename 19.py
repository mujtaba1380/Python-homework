class Company:
    def __init__(self,name):
        self.__name = name
        self.__employees = []
    def add_emp(self,emp_name):
        self.__employees.append(emp_name)
        print("succesfully added!")
    def remove_emp(self,emp_name):
        self.__employees.append(emp_name)
        print("succesfully removed!")
    def show_employees(self):
        return self.__employees
Alokozay_company = Company("Alokozay")
Alokozay_company.add_emp("Haroon")
Alokozay_company.add_emp("Salim")
print(Alokozay_company.show_employees())