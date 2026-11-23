from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...                          # тела нет — только контракт

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

figures = [Rectangle(10, 5), Circle(5), Triangle(5, 5)]
for fig in figures:
    print(fig.area())