
# Public member


from abc import ABC,abstractmethod
from ast import Delete
from distutils.command.config import config 
from math import pi
from turtle import shape

class Animal(ABC):

    #Concrete method
    #Inherited
    def sleep(self):
        print("Im sleeping")

    # This have to be overritten
    @abstractmethod
    def sound(self):
        print("This function is for definnign the sound by any animal")


class Snake(Animal):
    def sound(self):
        print("Im can hiss")

class Cat(Animal):
    def sound(self):
        print("mjau")

class Dog(Animal):
    def sound(self):
        print("I an bark")

class Lion(Animal):
    def sound(self):
        return super().sound()

class Rabbit(Animal):
    def sound(self):
        return super().sound()
        print("I can squeak")

class Parent:
    def func1(self):
        print("Hello im a parent.")

class Child(Parent):
    def func2(self):
        print("Hello im a child.")

class parent1:
    def func1(self):
        print("Hello parent1")

class parent3:
    def func2(self):
        print("Hello parent3")

class parent2:
    def func2(self):
        print("Hello parent2")


class child2(parent1,parent3, parent2):
    def func1(self):
        print("Hellp child")

# Polymorfism
class Shape:
    def __init__(self,name) -> None:
        self.name = name
        
    def area(self):
        pass

    def fact(self):
        print("Im todimentional shape")

    def __str__(self) -> str:
        return self.name

class Circle(Shape):

    def __init__(self, radius) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def face(self):
        print("I cound be a thre dimensional shape, but then you have to call med a ball")
   
    def __repre__(self):
        return self.name

shape_circle = Circle(7)

print(shape_circle)
print(round(shape_circle.area(), 2))
print(shape_circle.fact())



#Test child 
confused_chiled = child2()
confused_chiled.func2()

#This is shows the python "search" hierkey
print(child2.__mro__)
print("Is child2 is subclass of parent2: ", issubclass(child2,parent2))



# Driver code:
test = Child()
test.func1()
test.func2()

rabbit = Rabbit()
rabbit.sound()

lion = Lion()
lion.sound()





