# File:		beverage.py
# Author:	Adelaida Medlock
# Date:		August 29, 2025
# Description:	Class to represent a beverage item and calculate
#				total sugar and caffeine consumption.

class BeverageItem:
    def __init__(self, name, size, sugar, caffeine):
        self.__name = name
        self.__size = size
        self.__sugar = sugar
        self.__caffeine = caffeine
        
    def getName(self):
        return self.__name

    def getServingSize(self):
        return self.__size

    def getSugar(self):
        return self.__sugar

    def getCaffeine(self):
        return self.__caffeine

    def calculateTotalSugar(self, servings):
        return self.__sugar * servings

    def calculateTotalCaffeine(self, servings):
        return self.__caffeine * servings
