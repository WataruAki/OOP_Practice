from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self)-> float:
        pass

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    
    def area(self)->float:
        return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h
    
    def area(self) -> float:
        return self.w * self.h
