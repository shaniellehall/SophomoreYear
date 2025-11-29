"""
Author: [Your Name]
Date: November 26, 2025
Description: Participant class hierarchy for graduation ceremony management
"""

from abc import ABC, abstractmethod


class Participant(ABC):
    """Abstract base class for all ceremony participants"""
    
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getFullName(self):
        """Returns full name as 'FirstName LastName'"""
        return f"{self.__firstName} {self.__lastName}"
    
    def getSortName(self):
        """Returns name for sorting as 'LastName, FirstName'"""
        return f"{self.__lastName}, {self.__firstName}"
    
    @abstractmethod
    def __str__(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Graduate(Participant):
    """Represents a graduate student"""
    
    def __init__(self, firstName, lastName, designation, degree, major, distinctions):
        super().__init__(firstName, lastName)
        self.__designation = designation  # "G" or "UG"
        self.__degree = degree
        self.__major = major
        self.__distinctions = distinctions
    
    def getDesignation(self):
        return self.__designation
    
    def getDegree(self):
        return self.__degree
    
    def getMajor(self):
        return self.__major
    
    def getDistinctions(self):
        return self.__distinctions
    
    def getAnnouncerCard(self):
        """Returns formatted announcer card with name, degree, and distinctions"""
        lines = [self.getFullName()]
        lines.append(f"- {self.__degree} in {self.__major}")
        for distinction in self.__distinctions:
            lines.append(f"- {distinction}")
        return "\n".join(lines)
    
    def __str__(self):
        """Returns formatted string: 'Name, Degree in Major, Distinction(s)'"""
        result = f"{self.getFullName()}, {self.__degree} in {self.__major}"
        if len(self.__distinctions) > 0:
            result += ", " + self.__distinctions[0]
            if len(self.__distinctions) > 1:
                result += "*"
        return result


class Faculty(Participant):
    """Represents a faculty member"""
    
    def __init__(self, title, firstName, lastName, department):
        super().__init__(firstName, lastName)
        self.__title = title
        self.__department = department
    
    def getTitle(self):
        return self.__title
    
    def getDepartment(self):
        return self.__department
    
    def getFullName(self):
        """Override to include title"""
        return f"{self.__title} {self.getFirstName()} {self.getLastName()}"
    
    def __str__(self):
        """Returns formatted string: 'Title FirstName LastName, Department'"""
        return f"{self.getFullName()}, {self.__department}"


class Guest(Participant):
    """Represents a guest speaker"""
    
    def __init__(self, title, firstName, lastName, affiliation):
        super().__init__(firstName, lastName)
        self.__title = title
        self.__affiliation = affiliation
    
    def getTitle(self):
        return self.__title
    
    def getAffiliation(self):
        return self.__affiliation
    
    def getFullName(self):
        """Override to include title"""
        return f"{self.__title} {self.getFirstName()} {self.getLastName()}"
    
    def __str__(self):
        """Returns formatted string: 'Title FirstName LastName, Affiliation'"""
        return f"{self.getFullName()}, {self.__affiliation}"