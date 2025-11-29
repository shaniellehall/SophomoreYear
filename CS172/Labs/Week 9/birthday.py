"""
NAMES AND USERID
Shanielle Hall snh325
Alyn Tetteh    aet78

Birthday class containing the day, month and year, getters for each attribute and a
__str__ method (converts the day, month and year into a string (dd/mm/yyyy)
__hash__ method (that returns an integer as the sum of the day, month, and year, mod 12)
and an __eq__ method (test if two Birthday objects have the same attribute values).
"""

class Birthday():
    #constructor
    def __init__(self, month, day, year):
        self.__month = int(month)
        self.__day = int(day)
        self.__year = int(year)
    
    def getMonth(self):
        return self.__month
    
    def getDay(self):
        return self.__day
    
    def getYear(self):
        return self.__year
    
    def __str__(self):
        return f"{self.__month}/{self.__day}/{self.__year}"
    
    def __hash__(self):
        return (self.__day + self.__month + self.__year) % 12
    
    def __eq__(self, other):
        return(self.__day == other.__day and self.__month == other.__month and self.__year == other.__year)      