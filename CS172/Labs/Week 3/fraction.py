#CS 172 - Lab 3 Start Code
#NAMES:		Shanielle Hall	Alyn Tetteh
#USER-ID'S:	snh325			aet78

class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self, a, b):
        self.__num = a
        self.__den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.__den == 1 :
            return str(self.__num)
        else:
            return str(self.__num) + "/" + str(self.__den)
            
    #Get the Numerator
    def getNum(self):
        return self.__num
        
    #Get the Denominator
    def getDen(self):
        return self.__den
        
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.__num / self.__den
        
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.__num, self.__den)
        self.__num = self.__num // x
        self.__den = self.__den // x
        
    #Find the GCD of a and b
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    #Compare two fraction objects
    def __eq__(self,other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()
    
    
    
    #Complete these methods in lab
    def __add__(self, other):        
        num = self.getNum() * other.getDen() + other.getNum() * self.getDen() # a*y + x*b 
        den = self.getDen() * other.getDen() # b*y
        return Fraction(num, den) # (a*y + x*b) / b*y
        
    def __sub__(self, other):
        num = (self.getNum() * other.getDen()) - (other.getNum() * self.getDen()) #(a*y - x*b)
        den = self.getDen() * other.getDen() #b*y
        return Fraction(num, den) #(a*y - x*b)/ b*y
        
    def __mul__(self, other):
        num = (self.getNum() * other.getNum()) #a*x
        den = self.getDen() * other.getDen() #b*y
        return Fraction(num, den) # a*x / b*y
        
    def __truediv__(self, other):
        num = self.getNum() * other.getDen() #a*y
        den = self.getDen() * other.getNum() #x*b
        return Fraction(num, den) # a*y / x*b
        
    def __pow__(self, exp):
        """
        (a/b)^ k = (a^k) / (b^k)
        (a/b)^ 0 = 1
        (a/b)^ -k = (b^k) / (a^k)
        """
        if exp == 0:
            return Fraction(1,1) # any number raised to the exponent 0 is 1
        elif exp > 0: #if the exponent is greater than 0, multiply by the exponent 
            return Fraction(self.getNum() ** exp, self.getDen() ** exp)
        else:
            return Fraction(self.getDen() ** abs(exp), self.getNum() ** abs(exp))
    
    
