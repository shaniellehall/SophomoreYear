"""
Purpose: The purpose of this assignment is to practice creating a class given a set of specifications, as well as
         overloading some operators to use with our objects. 
Name:    Shanielle Hall
UserID:  snh325   
Date:    10/12/2025
"""
#importing the FileSize class from filesize.py
from filesize import FileSize

if __name__ == "__main__":
    #Testing  normalization: FileSize(0, 0, 1300, 16) -> 0 MB, 1 KB, 277 B, 0 b
    print("Testing  normalization")
    fs1 = FileSize(0, 0, 1300, 16)
    fs2 = FileSize(2, 15, 200, 3)
    print(f"{fs1}")
    print(f"{fs2}")
    
    
    #Testing totalBits
    print("\nTesting totalBits")
    print(f"Total bits: {fs1.totalBits()}")
    print(f"Total bits: {fs2.totalBits()}")
    
    #Testing addBits
    print("\nTesting addBits")
    fs1.addBits(8)
    print(f"Add 8 bits: {fs1}")
    
    #Testing addition
    print("\nTesting addition")
    print(f"\nfs2: {fs2}")
    fs3 = fs1 + fs2
    print(f"fs1 + fs2 = {fs3}")
    
    #Testing subtraction
    print("\nTesting subtraction")
    fs4 = fs2 - fs1
    print(f"fs2 - fs1 = {fs4}")
    
    #Testing multiplication
    print("\nTesting multiplication")
    fs5 = fs1 * 3
    print(f"fs1 * 3 = {fs5}")
    
    print("\nTesting comparison operators")
    
    #Testing comparison operators
    print(f"fs1 == fs2: {fs1 == fs2}")
    print(f"fs1 < fs2: {fs1 < fs2}")
    print(f"fs2 > fs1: {fs2 > fs1}")
    
    print("\nTesting subscript operator")
    
    #Testing subscript operator
    print(f"fs2[0] (MB): {fs2[0]}")
    print(f"fs2[1] (KB): {fs2[1]}")
    print(f"fs2[2] (B): {fs2[2]}")
    print(f"fs2[3] (b): {fs2[3]}")
    
    print("\nTesting __str__")
    
    #Testing __str__
    print(f"{fs2}")
      
