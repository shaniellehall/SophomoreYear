
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name, color, x = 0, y = 0):
        self.__name = name
        self.__color = color
        self.__x = x
        self.__y = y
        
        
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
    
    def getLocation(self):
        return [self.__x, self.__y]
    
    def changeLocation(self, x, y):
        self.__x = x
        self.__y = y
        
    def changeColor(self, color):
        self.__color = color
        
    def __str__(self):
        myStr = "A " + self.__color + " " + self.__name + ", "
        myStr += "located at coordinates " + str(self.getLocation())
        return myStr
    
    #abstract methods\
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    
    
class Circle(Shape):
    def __init__(self, color, radius, x = 0, y = 0):
        super().__init__("Circle", color, x, y)
        self.__radius = radius
        
    def getRadius(self):
        return self._radius
    
    
    
    def area(self):
        return (math.pi ** math.pow(self.__radius, 2.0))
    
    def perimeter(self):
        return (2 * math.pi * self.__radius)
