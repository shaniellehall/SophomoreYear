# File:    DrawableObjects.py
# Purpose: Demo of a basic program using pygame
#          Case study for inheritance and Abstract Base classes 
# Author:  A. Medlock
# Date:    October 22, 2024

# import modules needed for this application
import pygame
from abc import ABC, abstractmethod

# Abstrat class to represent a drawable object
# Drawable objects have a (x, y) location and
# can be moved along the x-axis and the y-axis
# We want to be able to draw a Drawable object
# We also need to be able to get the object's
# bounding box
class Drawable(ABC):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    # getter
    def getLocation(self):
        return (self.__x, self.__y)
    
    # setters
    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def moveRight(self):
        self.__x += 1
        
    def moveLeft(self): 
        self.__x -= 1
        
    def moveDown(self):
        self.__y += 1
        
    def moveUp(self):
        self.__y -= 1
    
    # abstract methods
    @abstractmethod
    def draw(self, surface): # draw object on screen
        pass

    @abstractmethod
    def getRectangle(self): # return bounding box
        pass

      
# derived class that represents a House
class House(Drawable):
    # constructor
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color
    
    # draw() method implementation
    def draw(self, surface):
        location = self.getLocation()
        
        # the base of the house is a rectagle
        pygame.draw.rect( surface, self.__color, \
                         [location[0] - 15, location[1] - 10, 30, 20] )
        
        # the roof of the house is triangle
        pygame.draw.polygon(surface, self.__color, [ \
                   ( location[0] - 15, location[1] - 10 ), \
                   ( location[0] + 15, location[1] - 10 ), \
                   ( location[0], location[1] - 20 ) \
                   ] )
    
    # getRectangle() method implementation
    def getRectangle(self): # return bounding box for house
        location = self.getLocation()
        return pygame.Rect( [location[0] - 15, location[1] - 20, 30, 30] )
        
# derived class for Ground
class Ground(Drawable):
    # constructor
    def __init__(self, x = 0, y = 0, w = 0, h = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color
        self.__width = w
        self.__height = h
        
    # draw() method implementation
    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.rect(surface, self.__color, \
             [location[0], location[1], self.__width, self.__height] )
    
    # getRectangle() method implementation
    def getRectangle(self):
        location = self.getLocation()
        return pygame.Rect([location[0], location[1], self.__width, self.__height])
      
# derived class that represents a Snowman
class Snowman(Drawable):
    # constructor
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color    
    
    # draw() method implementation
    def draw(self,surface):
        location = self.getLocation()
        
        # base / bottom
        pygame.draw.circle(surface, self.__color, \
                          [location[0], location[1]], 20)
        
        # middle circle of the body
        pygame.draw.circle(surface, self.__color, \
                          [location[0], location[1] - 20], 15)
        
        # top circle is the head
        pygame.draw.circle(surface, self.__color, \
                          [location[0], location[1] - 40], 10)

    # getRectangle() method implementation
    def getRectangle(self):
        location = self.getLocation()
        return pygame.Rect( [location[0] - 20, location[1] - 45, 40, 90] )
    
# derived class for Text
class Text(Drawable):
    # constructor
    def __init__(self, message = "Pygame", x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 26)
        self.__surface = fontObj.render(message, True, color)

    # draw() method implementation
    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    # getRectangle() method implementation
    def getRectangle(self):
        return self.__surface.get_rect()


# a collision detection funcion - from the lecture notes
# this function receives 2 bounding boxes and checks if
# they intersect.
def collisionDetection(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and \
        (rect1.x + rect1.width > rect2.x) and \
        (rect1.y < rect2.y + rect2.height) and \
        (rect1.height + rect1.y > rect2.y) :
        return True
    return False

# main scrip starts here
if __name__ == "__main__":
    #initialization                           
    pygame.init()
    surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('My Drawable Objects')
    
    # add clock for refreshing screen
    fpsclock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []   
    
    newHouse = House(150, 200, (255, 0, 0))
    newSnow = Snowman(70, 200, (255, 255, 255))
    newText = Text('Python and Pygame!', 75, 50, (0, 0, 255))
    ground = Ground(0, 210, 400, 300, (255, 255, 255))
    
    drawables.append(newHouse)
    drawables.append(newSnow)
    drawables.append(newText)
    drawables.append(ground)

    # game loop
    while True: 
        for event in pygame.event.get(): # get and process events
            if (event.type == pygame.QUIT) or \
               (event.type == pygame.KEYDOWN and \
                event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
        
        # clear surface with color
        surface.fill((204, 229, 255))
        
        # get each drawable obj and draw it
        for drawable in drawables:
            drawable.draw(surface)

        # animation
        surface.fill((204, 229, 255))
        for drawable in drawables:
            if isinstance(drawable, Snowman):
                drawable.moveRight()
            drawable.draw(surface)
            
        # collision detection
        for i in range(len(drawables)):
            for j in range(i + 1, len(drawables)):
                if isinstance(drawables[i], House):
                    if(collisionDetection(drawables[i].getRectangle(),drawables[j].getRectangle())):
                        print('Collision detected!')

        #update display and set frames per second
        pygame.display.update()
        fpsclock.tick(20)


