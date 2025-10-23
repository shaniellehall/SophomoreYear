'''
    Authors:Alyn Tetteh and Shanielle Hall
    ID: aet78 and snh325
    Date: 2nd October, 2025
    Description:
'''

from item import Item
from receipt import Receipt


if __name__=="__main__":
    print ("Welcome to the Receipt Creator\n")
    
    receipt = Receipt()
    #assigns the more boolean value as true (yes)
    more = "yes"

    while more == "yes": #while more is true
        name = input ("Enter Item name: ")
        price = float (input("Enter Item Price: "))
        taxable_input = input ("Is the item taxable (yes/no): ")
        taxable = (taxable_input == "yes")
        
        item = Item(name, price, taxable)
        receipt.addItem(item)
        
        #when the use inputs a string, strips all the empty spaces and formats the word to lower case
        more = input("Add another item (yes/no): ").strip().lower()
        print()
        
    #prints the full program    
    print("\n" + receipt.receiptToString())