# File:    main.py
# Purpose: Demo of using a hash table.
#          Items will in the form [MyObject, int]
# Author:  Adelaida A. Medlock
# Date:    November 18, 2024

# import any needed modules
from myObject import MyObject
from hashTable import OpenHashTable

if __name__ == "__main__" :
    # We need to create a hash table of size 95 because
    # there are 95 printable characters
    table = OpenHashTable(95)
    
    # Show hash table before populating it
    #print(table)
    
    # Add items to the hash table. 
    howMany = int(input('How many items do you want to store? '))
    count = 1
    while count <= howMany :
        char = input('Enter a single character: ')
        number = int(input('How many tiles with this character do you have? '))
        key = MyObject(char)
        try:
            table.insert(key, number)
            count += 1
        except KeyError as e:
            print(e)
            print()
        
    # Let's see what the hash table looks like after populating it
    print('\nHere is our hash table:')
    print(table)
    print()
    
    # Search by key and removing item if key exits
    char = input('Enter key to search for: ')
    searchKey = MyObject(char)
    try : 
        print('There are', table.searchByKey(searchKey), 'tiles.')
        print('Removing item now')
        table.remove(searchKey)
    except KeyError as e:
        print(e)
        
    # Update item
    char = input('Enter key to update its value: ')
    value = int(input('Enter new value for this key: '))
    key = MyObject(char)
    try : 
        table.update(key, value)
    except KeyError as e:
        print(e)
        
    # print hash table to verify we removed item
    print(table)
