import pygame
from abc import ABC, abstractmethod
from random import randint


class Drawable(ABC):
    #constructor
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    #getters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getLocation(self):
        return (self.__x, self.__y)
    
    
    #setters
    def moveRight(self):
        self.__x += 5
        
    def moveLeft(self):
        self.__y -= 5
        
    def moveUp(self):
        self.__x -= 5
        
    def moveDown(self):
        self.__y += 5

    def setLocation(self, x, y):
        self.__x = x
        self.__y = y
        
    #abstract methods
    @abstractmethod
    def draw(self, surface):
        pass
    
    @abstractmethod
    def getRectangle(self):
        pass
    
    


#define global colors
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (165, 156, 148)
PINK = (255, 182, 193)
GREEN = (4, 106, 56)

#Derived class that represents a mouse
class Mouse(Drawable):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.__body = GRAY
        self.__eyes = BLACK
        self.__ears = GRAY
        self.__nose = PINK
        
    #implement draw
        
    def draw(self, surface):
        #get location to draw the mouse
        location - self.getLocation()
        
        #Draw the body (oval): target surface, color
        #                      [upper-left corner x and y coordinates]
        #                      width, height
        
        pygame.draw.ellipse(surface, self.__body, \
                            [ location[0], location[1], 100, 50])
        
        #draw ears (circle): targer surface, color, (center x, center y), radius
        pygame.draw.circle( surface, self.__ears, \
                            (location[0] + 25, location[1]), 20 )
        pygame.draw.circle( surface, self.__ears, \
                            (location[0] + 75, location[1]), 20 )
        
        #draw eyes (circle): targer surface, color, (center x, center y), radius
        pygame.draw.circle( surface, self.__eyes, \
                            (location[0] + 25, location[1] + 20), 5 )
        pygame.draw.circle( surface, self.__eyes, \
                            (location[0] + 65, location[1] + 20), 5 )
        
        
        
        #draw the nose (circle)
        pygame.draw.circle( surface, self.__nose, \
                            (location[0] + 50, location[1] + 35) , 5 )
        
    #implement getRectangle()
    def getRectangle(self):
        location = self.getLocation()
        return pygame.Rect(location[0], location[1] - 22, 100, 75)
        
        