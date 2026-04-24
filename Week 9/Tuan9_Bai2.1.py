import math
import copy

class Point:
    def __init__(self, x=0, y=1):
        self.__x, self.__y = x, y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        return(f"{self.__x},{self.__y}")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self):
        return math.sqrt(self.__x**2+self.__y**2)
    def distance(self, other):
        return math.sqrt((self.__x - other.__x)**2+(self.__y - other.__y)**2)
    
class LineSegment():
    def __init__(self, * args):
        if len(args)==0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        elif len(args)==2:
            if isinstance(args[0], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]
        elif len(args)==4:
            if isinstance(args[0], int):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])
        elif len(args)==1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)
        else:
            raise ValueError
    def read(self):
        user_input = input().split()
        if len(user_input) >= 4:
            x1, y1, x2, y2 = map(int, user_input[:4])
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)
    def print(self):
        print (f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]")
    
    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)
    
    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()

        radian = math.atan2(dy, dx)

        degree = round(math.degrees(radian))

        final_angle = int(degree % 360)
        if final_angle < 0:
            final_angle += 360
        return final_angle
