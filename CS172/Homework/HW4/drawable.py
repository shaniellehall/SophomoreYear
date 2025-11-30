from abc import ABC, abstractmethod

# Abstract base class for drawable objects
class Drawable(ABC):
    #Constructor
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        self.visible = True
    
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    #get location
    def getLoc(self):
        return (self.__x, self.__y)
    
    #set location
    def setLoc(self, x, y):
        self.__x = x
        self.__y = y
    
    #visibility methods
    def isVisible(self):
        return self.visible
    
    def setVisible(self, visible):
        self.visible = visible

    #collision detection
    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()    
        return rect1.colliderect(rect2)