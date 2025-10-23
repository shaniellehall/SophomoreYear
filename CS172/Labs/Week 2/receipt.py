'''
    Authors:Alyn Tetteh and Shanielle Hall
    ID: aet78 and snh325
    Date: 2nd October, 2025
    Description:
'''


import datetime
from item import Item

# Define the Receipt class
class Receipt:
    def __init__ (self, tax_rate = 0.07):
        self.__tax_rate = tax_rate
        self.__purchases = []
        
    def receiptToString(self):
        # Header with date
        result = f"----- Receipt {datetime.datetime.now()} -----\n\n"
        
        # Calculate totals
        subtotal = 0
        total_tax = 0

        for item in self.__purchases:
            price = item.getPrice()
            tax = item.getTax(self.__tax_rate)
            subtotal += price
            total_tax += tax

            # Format: name left, price right, 2 decimals
            result += "{:<20}{:>10.2f}\n".format(item.itemToString(), price)

        grand_total = subtotal + total_tax

        # Add totals section
        result += "\n"
        result += "{:<20}{:>10.2f}\n".format("Sub Total", subtotal)
        result += "{:<20}{:>10.2f}\n".format("Tax", total_tax)
        result += "{:<20}{:>10.2f}\n".format("Total", grand_total)

        return result
 
        
    def addItem(self, item):
        self.__purchases.append(item)
        
    
    
# Test your Receipt class here before you continue with the rest of the lab
if __name__ == "__main__":
    # Milestone 2: Create an instance of Receipt and test its methods
    print('*** Testing Receipt Class ***')
    item1 = Item ('Soda', 2.48, True)
    item2 = Item ('Milk', 4.79, False)
    myReceipt = Receipt(0.08)
    myReceipt.addItem(item1)
    myReceipt.addItem(item2)
    print(myReceipt.receiptToString())