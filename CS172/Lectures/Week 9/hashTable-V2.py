#File:     hashTable-V2.py
#Purpose:  An implementation variation of an open hash table
#Author:   Adelaida A. Medlock
#Date:     March 4, 2024

# This open hash table is a list of lists
# When instantiated it's initially empty
# Methods include: insert, search, remove, myHash, __str__
class OpenHashTable:
    # constructor
    def __init__(self, size): 
        self.__size = size
        self.__data = []
        for i in range(0, self.__size):
            self.__data.append([])
    
   # __str__ to use print() to display hash table
    def __str__(self):
        htStr = "Open Hash Table\n"
        htStr += f"My size is {self.__size}\n"
        for i in range(0, self.__size):
            htStr += f"data[{i:}] = {self.__data[i]:}\n"
        htStr += "End of Hash Table"
        return htStr
    
    # myHash() method is used to determine index within the table
    # note that key must be a hashable object
    def myHash(self, key):
        return hash(key) % self.__size 
    
    # insert a single value, but value must be hashable
    def insert(self, value):
        index = self.myHash(value)
        row = self.__data[index]
        for item in row:
            if item == value:
                raise KeyError('key already exits')             
        self.__data[index].append(value)

    # search for an item
    def search(self, value):
        index = self.myHash(value)
        row = self.__data[index]
        for i in range (0, len(row)) :
            if row[i] == value:
                return True
        return False
          
    # remove item from hash table
    def remove(self, value):
        index = self.myHash(value)
        row = self.__data[index]
        for i in range(0, len(row)):
            if row[i] == value:
                #row.remove(value)
                row.pop(i)
                return
        raise KeyError('key does not exist')

# the main routine
if __name__ == "__main__" :
    
    table = OpenHashTable(5)
    
    table.insert(10) # key is 10
    table.insert(21) # key is 21
    table.insert(33) # key is 33
    table.insert(7)  # key is 7
    table.insert(16) # key is 16
    table.insert(42) # key is 42
    table.insert(54) # key is 54
    # table.insert(54) # raises an exception
    
    print(table)
    
    searchKey = int(input('\nEnter value to search for: '))
    if table.search(searchKey) :
        print('Found!')
    else :
        print('Not Found!')
        
    print('\nRemoving items\n')
    table.remove(searchKey)
    print(table)