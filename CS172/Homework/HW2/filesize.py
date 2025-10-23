"""
Purpose: The purpose of this assignment is to practice creating a class given a set of specifications, as well as
         overloading some operators to use with our objects. 
Name:    Shanielle Hall
UserID:  snh325   
Date:    10/12/2025
"""

#class to represent a file size
class FileSize:
    #initializer with normalization
    def __init__(self, mb = 0, kb = 0, B = 0, b = 0):
        #Normalize the values
        total_bits = mb * 1024 * 1024 * 8 + kb * 1024 * 8 + B * 8 + b
        
        #converting back to normal
        self.__megabytes = total_bits // (1024 * 1024 * 8)
        remainder = total_bits % (1024 * 1024 * 8)
        
        self.__kilobytes = remainder // (1024 * 8)
        remainder = remainder % (1024 * 8)
        
        self.__bytes = remainder // 8
        self.__bits = remainder % 8
        
    #getters    
    def getMegabytes(self):
        return self.__megabytes
    
    def getKilobytes(self):
        return self.__kilobytes
    
    def getBytes(self):
        return self.__bytes
    
    def getBits(self):
        return self.__bits
    
    def addBits(self, n):
        total_bits = self.totalBits() + n #adds n bits to the file size
        
        #Normalize the values
        self.__megabytes = total_bits // (1024 * 1024 * 8)
        remainder = total_bits % (1024 * 1024 * 8)
        self.__kilobytes = remainder // (1024 * 8)
        remainder = remainder % (1024 * 8)
        self.__bytes = remainder // 8
        self.__bits = remainder % 8
        
    
    def totalBits(self):
        #returns the total size in bits
        return (self.__megabytes * 1024 * 1024 * 8 + self.__kilobytes * 1024 * 8 + self.__bytes * 8 + self.__bits)
    
    def __add__(self, other):
        #adds two FileSize objects
        total_bits = self.totalBits() + other.totalBits()
        
        #makes a new FileSize object from total_bits
        mb = total_bits // (1024 * 1024 * 8)
        remainder = total_bits % (1024 * 1024 * 8)
        kb = remainder // (1024 * 8)
        remainder = remainder % (1024 * 8)
        B = remainder // 8
        b = remainder % 8
        
        return FileSize(mb, kb, B, b)
    
    def __sub__(self, other):
        #subtracts two FileSize objects
        diff_bits = self.totalBits() - other.totalBits()
        
        if diff_bits < 0:
            diff_bits = abs(diff_bits)  # Ensure non-negative result
        
        #makes a new FileSize object from diff_bits
        mb = diff_bits // (1024 * 1024 * 8)
        remainder = diff_bits % (1024 * 1024 * 8)
        kb = remainder // (1024 * 8)
        remainder = remainder % (1024 * 8)
        B = remainder // 8
        b = remainder % 8
        
        return FileSize(mb, kb, B, b)
    
    def __mul__(self, n):
        #multiply FileSize by an integer n
        total_bits = self.totalBits() * n
        
        #makes a new FileSize object from total_bits
        mb = total_bits // (1024 * 1024 * 8)
        remainder = total_bits % (1024 * 1024 * 8)
        kb = remainder // (1024 * 8)
        remainder = remainder % (1024 * 8)
        B = remainder // 8
        b = remainder % 8
        
        return FileSize(mb, kb, B, b)
    
    #comparison operators
    def __eq__(self,other):
        return self.totalBits() == other.totalBits()
    
    def __ne__(self,other):
        return self.totalBits() != other.totalBits()
    
    def __lt__(self,other):
        return self.totalBits() < other.totalBits()
    
    def __le__(self,other):
        return self.totalBits() <= other.totalBits()
    
    def __gt__(self,other):
        return self.totalBits() > other.totalBits()
    
    def __ge__(self,other):
        return self.totalBits() >= other.totalBits()
    
    #subscript operator
    def __getitem__(self, index):
        #SUbscripts
        if index == 0:
            return self.__megabytes
        elif index == 1:
            return self.__kilobytes
        elif index == 2:
            return self.__bytes
        elif index == 3:
            return self.__bits
        else:
            raise IndexError("Index out of Bounds")
    
    #string representation
    def __str__(self):
        return f"{self.__megabytes} MB, {self.__kilobytes} KB, {self.__bytes} B, {self.__bits} b"