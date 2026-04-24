import math

class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def read(self):
        self.__x = int (input())
        self.__y = int (input())
    
    def print(self):
        print(f"({self.__x}, {self.__y})")

    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def distance_to_other(self, other):
        return math.sqrt((self.__x - other.__x)**2 + (self.__x - other.__y)**2)
    
    def symmetry(self):
        return Point(-self.__x, -self.__y)
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def __str__(self):
        return(f"{self.__x}, {self.__y}")
    
class ColorPoint(Point):
    def __init__(self, x, y, color = 'xanh'):
        super().__init__(x, y)
        self.__color = color

    def read(self):
        super().read()
        self.__color = str(input())
    
    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.__color}")
        super().print(),print(":"f"{self.__color}")