import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x, self.__y = x, y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def distance_other(self, other):
        return math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)

    def symmetry(self):
        return Point(-self.__x, -self.__y)

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def __str__(self):
        return(f"{self.__x}, {self.__y}")
    
class PointTest():
    def testCase(self):
        p1 = Point()
        p1.print()
        p2 = Point()
        p2.read()
        p2.print()
        p2.move(1, 1)
        p2.print()
        print(p2.distance())
        


