class ComplexNum():
    def __init__(self, r = 0, i = 0):
        self.__real = r
        self.__imaginary = i
        
    def getReal(self):
        return self.__real
    
    def getImaginary(self):
        return self.__imaginary
    
    def setReal(self, value):
        self.__real = value
        
    def setImaginary(self, value):
        self.__imaginary = value
        
    #overloading the operators
    #overload __str__ to be able to use print() --> ( real, imaginaryi )
        
    def __str__(self):
        cStr = "( {:.2f}, {:.2f} )".format(self.__real, self.__imaginary)
        return cStr
    
    def __getitem__(self, index):
        if index == 0:
            return self.__real
        elif index == 1:
            return self.__imaginary
        else:
            raise IndexError ("Index" + str(index) + " is out of bounds")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.__real = value
        elif index == 1:
            self.imaginary = value
        else:
            raise IndexError ("Index" + str(index) + " is out of bounds")
        
    
    # arithmetic operators + - * /
    #
    # __add__ this is for +
    # (a + bi) + (x + yi)
    # result: (a + x) + (b + y)i
    
    def __add__(self, other):
        a = self[0]
        b = self[1]
        x = other[0]
        y = other[1]
        real = a + x
        imaginary = b + y
        return ComplexNum(real, imaginary)
    
    # __sub__ this is for -
    # (a + bi) - (x + yi)
    # result: (a - x) + (b - y)i
    def __sub__(self, other):
        a = self[0]
        b = self[1]
        x = other[0]
        y = other[1]
        real = a - x
        imaginary = b - y
        return ComplexNum(real, imaginary)
    
    # __mul__ this is for *
    # (a + bi) * (x + yi)
    # result: (ax - by) + (ay - bx)i
    def __mul__(self, other):
        a = self[0]
        b = self[1]
        x = other[0]
        y = other[1]
        real = a * x - b * y
        imaginary = a * y + b * x
        return ComplexNum(real, imaginary)
        
    # __truediv__ this is for /
    # (a + bi) / (x + yi)
    # result: ( (ax + by) / (x^2 + y^2) ) + ( (bx - ay) / (x^2 + y^2) ) i
    def __truediv__(self, other):
        a = self[0]
        b = self[1]
        x = other[0]
        y = other[1]
        real = 		( (a * x + b * y) / (x ** 2 + y ** 2) )  
        imaginary = ( (b * x - a * y) / (x ** 2 + y ** 2) )
        return ComplexNum(real, imaginary)
    
    #other useful operators
    # __abs__ for abs()
    # result sqrt(r^2 + i^2)
    def __abs__():
       return sqrt(self[0] ** 2 + self[1] ** 2)
    
    # comparison operators
    # __eq__ for ==
    def __eq__(self, other):
        return (self[0] == other[0]) and (self[1] == other[1])
    
    def __ne__(self, other):
        return not (self == other)




"""
c = ComplexNum(100, 200)
print(c)
( 100.00, 200.00 )
l = [10, 30, 44]
print(l[0])
10

"""

"""
c = ComplexNum()
c[0]
0
c[1]
0
c[0] = 100
c[0]
100
c[10]
raise IndexError ("Index" + str(index) + " is out of bounds")
IndexError: Index10 is out of bounds
"""
"""
c1 = ComplexNum(10, 30)
>>> c2 = ComplexNum()
>>> print(c1)
( 10.00, 30.00 )
>>> print(c2)
( 0.00, 0.00 )
>>> print(c1/c2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\iwant\Desktop\Fall25\CS172\Week 3 Lecture\complexNum.py", line 89, in __truediv__
    real = 		( (a * x + b * y) / (x ** 2 + y ** 2) )
ZeroDivisionError: division by zero
>>> 

"""
