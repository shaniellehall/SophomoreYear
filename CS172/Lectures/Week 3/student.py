

class Student :
    
    #Static member that will be used to keep track of available ID numbers
    __currentID = 1
    
    
    #constructor
    def __init__(self, name):
        self.__name = name
        self.__totalCredits = 0
        self.__qualityPoints = 0
        self.__ID = Student.__currentID # self.__ID is an instance data member
        
        Student.__currentID += 1
        
    #getters
        
    def getName(self):
        return self.__name
        
    def getTotalCredits(self):
        return self.___totalCredits
        
    def getGPA(self):
        if self.__totalCredits == 0:
            return 0.0
        else:
            return self.__qualityPoints / self.totalCredits
    
    #new getter to obtain the student's ID
    def getStudentID(self):
        pass
        
        
             
        #setters
    def earnCredits(self):
        grade = grade.upper()
        if grade == "A":
            qPoints = 4.0
        elif grade == "B":
            qPoints = 3.0
        elif grade == "C":
            qPoints = 2.0
        elif grade == "D":
            qPoints = 1.0
        else: #grade is an F
            qPoints == 0.0
            
        
        self.__totalCredits = self.__totalCredits + creditCount
        self._qualityPoints = self.__qualityPoints + (creditCount * qPoints)
        
    #helper to display student
    #this 
    def printStudent(self):
        print("Student's name:", self.__name)
        print("Credits EarnedL", self.__totalCredits)
        print("Student's GPA: ", round(self.getGPA(), 2))
        
        
    #a static method to obtain the value of the static member
    @staticmethod #decorator to indicate that the method under this line is static
    def getNextAvailableID():
        return Student.__currentID
        
    #operator overloading
    
    # __str__(): allows me to use print() directly with objects
    def __str__(self):
        myStr = "Student's name: " + self.__name + '\n'
        myStr += "Student's ID#: " + str(self.__ID) + '\n'
        myStr += "Credits Earned: " + str(self.__totalCredits) + '\n'
        myStr += "Student's GPA: " + str(self.getGPA()) + '\n'
        return myStr
    
    
    #the comparison operators
    #__eq__ is for ==
    def __eq__(self,other):
        name = self.__name == other.getName()
        idNumber = self.__ID == other.getStudentID()
        courseCredits = self.__totalCredits == other.getTotalCredits()
        gpa = self.getGPA() == other.getGPA()
        return name and idNumber and courseCredits and gpa #boolean
    
    #__ne__ is for !=
    
    def __ne__(self, other):
        name = self.__name != other.getName()
        idNumber = self.__ID != other.getStudentID()
        courseCredits = self.__totalCredits != other.getTotalCredits()
        gpa = self.getGPA() != other.getGPA()
        return name or idNumber or courseCredits or gpa #boolean
    
    #how about < <= > >= ?
    #these may be useful if we need to sort a bunch of Student objects
    #but we need to know what the sorting criteria would be
    
    #let's assume we want to sort students in alphabetical order
    
    
    def __gt__(other, self):
        return self.__name > other.getName()
        #alternative way: sort by credits earned
        #return self.__totalCredits > other.getTotalCredits()
    
    def __lt__(other, self):
        return self.__name < other.getName()
    
    def __ge__(other, self):
        return self.__name >= other.getName()
    
    def __ge__(other, self):
        return self.__name =< other.getName()
    
    
    
    
    
    """
    s = Student('Sam')
    print(s)
    """
    
    
    
    
    """
    s = Student("Sam")
    s.earnCredits(3, "A")
    """

