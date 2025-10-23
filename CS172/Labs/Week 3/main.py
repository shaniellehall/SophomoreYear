# Purpose: Create an object with overloaded operators to create fractions
#NAMES:		Shanielle Hall	Alyn Tetteh
#USER-ID'S:	snh325			aet78

from fraction import Fraction

def H(n):
    sum = Fraction(0, 1)
    for k in range(n):
        sum += Fraction(1, (k+1))
    return sum                    
    
    
def T(n):
    sum = Fraction(1, 1)
    for k in range(n):
        sum += Fraction(1, 2) ** (k + 1)
    return sum
    
def Z(n):
    sum = Fraction(2, 1) - T(n)
    return sum
    
def R(n,b):
    sum = Fraction(0, 1)
    for k in range(1, n + 1):
        sum += Fraction(1,k) ** b
    return sum

if __name__ == "__main__":
    print ("Welcome to Fun with Fractions!")
    loop = False
     
    while not loop:
        try:
            n = int(input("Enter Number of iterations (integer>0): "))
            if n > 0:
                loop = True
        except ValueError:
            print("Bad input")
            
    print(f"H({n})={H(n)}")
    print(f"H({n})~={H(n).approximate():.8f}")
    print(f"T({n})={T(n)}")
    print(f"T({n})~={T(n).approximate():.8f}")
    print(f"Z({n})={Z(n)}")
    print(f"Z({n})~={Z(n).approximate():.8f}")
    print(f"R({n},10)={R(n,10)}")
    print(f"R({n},10)~={R(n,10).approximate():.8f}")
        
    
    #f1 = Fraction(3, 5)
    #f2 = Fraction(2, 3)
    #print(f1 + f2) # this should display 19/15
    #print(f2 - f1) # this should display 1/15
    #print(f1 * f2) # this should display 2/5
    #print(f1 / f2) # this should display 9/10
    #print(f1 ** 0) # this should display 1
    #print(f1 ** - 2) # this should display 25/9
    #print(f1 ** 3) # this should display 27/125
    #print(H(n))
    #print(T(n))
    #print(Z(n))
    #print(R(n, n))