'''
    Authors:Alyn Tetteh and Shanielle Hall
    ID: aet78 and snh325
    Date: 2nd October, 2025
    Description:
''' 
 
class Item:
    def __init__ (self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
        
    def itemToString(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getTax(self, taxRate):
        if self.__taxable:
            return self.__price * taxRate
        else:
            return 0.0
        
        
    
    
# Test your Item class here before you continue with the rest of the lab
if __name__ == "__main__":
    # Milestone 1: Create an instance of Item and test its methods
    print('*** Testing Item Class ***')
    myItem = Item ('Soda', 2.48, True)
    print(myItem.itemToString())
    print('Price:', myItem.getPrice())
    print('Tax:', myItem.getTax(0.08))
