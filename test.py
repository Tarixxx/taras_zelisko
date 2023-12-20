from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        print("Об'єкт створено")

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

square = Square(5)
rectangle = Rectangle(4, 6)
circle = Circle(3)

print(f"Площа квадрата: {square.area()}")
print(f"Площа прямокутника: {rectangle.area()}")
print(f"Площа круга: {circle.area()}")



print("jkfsdfsjkg;dfg")