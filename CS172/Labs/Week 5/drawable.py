#File Name:   drawable.py
#Purpose:     Abstract class that allows us to create drawable objects
#             with different shapes, at a given location (x, y)
#Last update: 4/24/24 - A. Medlock
"""
ADD YOUR NAME AND USER ID HERE:
Shanielle Hall snh325
Alyn Tetteh    aet78
"""

import random
import pygame
from abc import ABC, abstractmethod

# Abstract Base Class: Drawable
class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface):
        pass
        
# Rectangle Class: ADD YOUR CODE HERE

class Rectangle(Drawable):
    def __init__(self, x = 0, y = 0, width = 0, height = 0, color = (0,0,0)):
        super().__init__(x, y)#inherits x and y from the Drawable class
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, [location[0], location[1],\
                                                 self.__width, self.__height] )
    
    def getRectangle(self):
        location = self.getLocation()
        return pygame.Rect([location[0], location[1], self.__width, self.__height] )
        
# Snowflake Class: ADD YOUR CODE HERE

class Snowflake(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)#inherits x and y from the Drawable class
        self.__maxSnowFall = random.randint(300,500)
    
    def getMaxFall(self):
        return self.__maxSnowFall
    
    def draw(self, surface):
        white= (255,255,255)
        x, y = self.getLoc()
        #line 1
        pygame.draw.line(surface, white, (x - 5, y),(x + 5, y))
        #line 2
        pygame.draw.line(surface, white, (x, y - 5),(x, y + 5))
        #line 3
        pygame.draw.line(surface, white, (x - 5, y - 5) , (x + 5, y + 5))
        #line 4
        pygame.draw.line(surface, white, (x - 5, y + 5),(x + 5, y -5 ))
