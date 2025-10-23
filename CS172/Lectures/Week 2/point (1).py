#File Name: point.py
#Purpose:   Class to represent a point located at coordinates x, y
#           A point has an X and a Y coordinate. These values are integers
#           If no information is povided about the x, y coordinates at
#           instantiation time, assume both are zero.
#           At any given time, we may want to find out the x coordinate,
#           or just the y coordinate, or both of them.
#           A Point can be moved along the horizontal axis, or the
#           vertical axis. A Point can also be relocated to a x, y location;
#           and we can also reset the point to location 0, 0.
#           We may want to display the Point object and also be able to
#           calculate the distance between two Points
#           The Point class needs to keep track of all the points created.

#Author:    Adelaida Medlock
#Date:      April 8, 2024

from math import sqrt

class Point:
    # static (or class) attribute
    __count = 0  # to count how many points we have created so far
    
    # initialization method (constructor)
    def __init__ (self, x = 0, y = 0): # default arguments technique
        self.__x = x
        self.__y = y
        Point.__count += 1 # increase count by 1 each time we create a new point
    
    # public interface: made out of methods such as getters, setters,
    # and other useful methods
    # getters, accessors, inspectors
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getCoordinates(self):
        return (self.__x, self.__y)
    
    # setters, mutators
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
        
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y

    def reset(self):
        self.setPoint(0, 0)
        
    # this method calculates the distance between 2 Point objects
    def calculateDistance(self, p2):
        xDiff = ( self.getX() - p2.getX() ) ** 2
        yDiff = ( self.getY() - p2.getY() ) ** 2
        distance = sqrt(xDiff + yDiff)
        return distance
    
    # this method helps us print a Point object
    def pointToString(self):
        pStr = '(' + str(self.__x) + ',' + str(self.__y) + ')'
        return pStr
    
    # static methods
    @staticmethod
    def getPointCount(): # do not use the self implicit parameter with static methods
        return Point.__count  
    
    @staticmethod
    def printPointCount():
        print("Points created:", Point.__count)
        

# the code below only runs if this file is not being used as a module
if __name__ == "__main__" :
    # create some point objects
    p1 = Point()
    p2 = Point(10, 10)
    
    # print the points
    print('We have created', Point.getPointCount(), 'points:')
    print('p1 =', p1.pointToString())
    print('p2 =', p2.pointToString())
    
    # calculate the distance between p1 and p2
    dist = p1.calculateDistance(p2)
    print('The distance between p1 and p2 is', round(dist, 2))

        
