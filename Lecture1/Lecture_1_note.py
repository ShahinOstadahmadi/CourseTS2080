

# Making a simple

class Company:
    def __init__(self) -> None:
        # Protected
        self._project = "NLP"
        self._ting = "ting"


# Making a simple Employee class

class Employee(Company):
    def __init__(self, name, project, salary) -> None :
        self.name = name
        self._project = project
        self.__salary = salary
        Company.__init__(self)

    # public instance methods
    def show(self):
        #Private members are accessible from a class
        print("Name:", self.name, self._project ,'Salary:', self.__salary)


emp = Employee("Shahin","Hydro.Plant", 900)
emp._project = "nyProsjekt"
emp.show()

print(emp._project)
print(emp._Employee__salary) # one way to get the private members of the Empolyee
print(emp._ting) # one way to get the private members of the Empolyee






