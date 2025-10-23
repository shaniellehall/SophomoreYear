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

#Author:    Shanielle Hall
#Date:      September 30, 2025

from math import sqrt

class Point:
    #static member or attribute
    __count = 0
    
    
    #constructor
    def __init__(self, x = 0 , y = 0):
        self.__x = x
        self.__y = y
        Point.__count += 1 #increase __count by 1 each time a new Point object is created
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getCoordinates(self):
        return [self.__x, self.__y]
    
    #setters / mutators
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
        
    def reset(self):
        self.__x = 0
        self.__y = 0
        self.setPoint(0, 0)
    
    #helper methods
    def pointToString(self):
        ptStr = '(' + str(self.__x) + ', ' + str(self.__y) + ')'
        return ptStr
    
    """
    #sample test
    p = Point(0,0)
    print(p.pointToString())
    (0, 0)
    """
    
    def calculateDistance(self, other):
        xDiff = (self.__x - other.getX() ) ** 2
        yDiff = (self.getY() - other.getY() ) ** 2
        distance = sqrt(xDiff + yDiff)
        return distance
    
    #static method
    @staticmethod #decorator that indicates that the method below is a static method
    
    def getPointCount() : #do not use self in a static method
        return Point.__count
