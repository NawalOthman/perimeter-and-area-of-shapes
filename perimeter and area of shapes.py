
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

#Abstract Method
    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self,side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

#instant method
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length * self.__width) * 2


class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius
#static method 
    @staticmethod
    def PI():
        return 3.14

    def area(self):
        return Circle.PI() *self.__radius * self.__radius

    def perimeter(self):
        return 2 * Circle.PI() * self.__radius



square = Square(10)
print(f"Square area is {square.area()} and perimeter is {square.perimeter()}")

rectangle = Rectangle(5, 3)
print(f"Rectangle area is {rectangle.area()} and perimeter is {rectangle.perimeter()}")

circle1 = Circle(4)
print(f"Circle area is {circle1.area()} and perimeter is {circle1.perimeter()}")