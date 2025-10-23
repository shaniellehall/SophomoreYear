
class Student :
    #constructor
    def __init__(self, name):
        self.__name = name
        self.__totalCredits = 0
        self.__qualityPoints = 0
        
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
    def printStudent(self):
        print("Student's name:", self.__name)
        print("Credits EarnedL", self.__totalCredits)
        print("Student's GPA: ", round(self.getGPA(), 2))
        
        
    """
    s = Student("Sam")
    s.earnCredits(3, "A")
    """
