from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def  __init__ (self,length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Total Area of Rectangle is: {self.length * self.width}")

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        print(f"The Total Area of Circle is: {3.14*self.radius*self.radius}")

R1 = Rectangle(10,10)
R1.area()

C1= Circle(30)
C1.area()
