#File:     myObject.py
#Purpose:  Simple class MyObject to demostrate the hash method
#          MyObject has one data member which is a printable
#          character (ASCII codes 32 to 126 --> 95 characters)
#Author:   Adelaida A. Medlock
#Date:     March 4, 2025

class MyObject() :
    # constructor
    def __init__(self, value) :
        self.__value = value
    
    # getter 
    def getValue(self) :
        return self.__value
    
    # setter
    def setValue(self, newValue):
        self.__value = newValue
    
    # overloaded operators
    def __str__(self):
        return ('Value of my object: ' + str(self.__value))
    
    def __eq__(self, other) :
        return (self.__value == other.getValue())
    
    # the __hash__ method to implement hash() function
    # for a table that has 95 slots (so index 0 to 94)
    def __hash__(self) :
        return ord(self.__value) - 32
    
    
    
    """
    Testing myObject
    
    o = MyObject("q")
    o.getValue()
    'q'
    o.setValue("M")
    o == o
    True
    hash(o)
    45
    print(o)
    Value of my object: M
    """