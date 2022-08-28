# What is object oriented programming?

<p>
OOP is a consept which we program. The idea is how to manipulate the data rather than duplicate the same code for manipulation different data. The OOP is way to look at the complex outside world in an abstract and conseptual way. OOP helps programmers to work more effective than one did with procedure-oriented programing. </p>

### The four fundementals of OOP:

    - Inheritance
    - Encapsulation
    - Polymorphysm
    - Abstraction

### Advanteges of OOP:

    - Code reusability
    - reduce code complexity
    - Scalable

### What are the basic concepts of OOP?

Answer here

### What are the main principles of OOP?

Answer here

### Encapsulation

<p> The idea with encapsulation is to protect data of an object from clients to directly manipulate the private data. With another words, the objects data can only by manipulated by its own methods. The client can only send masseges to perform an method with different objects.</p>

> Wrapping up of data and funcitons into a single unit is called as data encapsulation

**Code example to illustrate encapsulation:**

```py
# Making a simple class structure

class Company:
    def __init__(self) -> None:
        # Protected
        self._project = "NLP"


class Employee(Company):
    """
    Employee class inherit from "Company" class
    """
    def __init__(self, name, project, salary) -> None :
        self.name = name
        self._project = project
        self.__salary = salary
        Company.__init__(self)

    # public instance methods
    def show(self):
        #Private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

emp = Employee("Shahin","Hydro.Plant", 900)
emp.show()
print(emp._Employee__salary) # one way to get the private members of the Empolyee

```

**Type of encapsulation**:

- public
- private
  -protected

### Why use encapsulation?

- Security
- Data Hiding
- Simplicity
- aesthetics

### Abstraction

Abstraction is...

### Inheritance

Inheritance is...

### Polymorphism

Polymorphism is...
