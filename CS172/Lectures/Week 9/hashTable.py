#File:     hashTable.py
#Purpose:  A basic implemetation of an open hash table.
#Author:   Adelaida A. Medlock
#Date:     March 4, 2025

# This open hash table is a list of lists
# When instantiated it's initially empty
# Methods include: insert, search, remove, update, myHash, __str__
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
            htStr += f"data[{i}] = {self.__data[i]}\n"
        htStr += "End of Hash Table"
        return htStr
    
    # myHash() method is used to determine index within the table
    # note that key must be a hashable object
    def myHash(self, key):
        return hash(key) % self.__size 
    
    # insert item in hash table, as [key, value]
    def insert(self, key, value):
        index = self.myHash(key)
        row = self.__data[index]
        for pair in row:
            if pair[0] == key:
                raise KeyError('key already exists')             
        self.__data[index].append([key, value])
          
    # search by key
    def searchByKey(self, key):
        index = self.myHash(key)
        row = self.__data[index]
        for pair in row:
            if pair[0] == key:
                return pair[1]
        raise KeyError('key does not exist')
    
    # remove item from hash table when valid key is provided
    def remove(self, key):
        index = self.myHash(key)
        row = self.__data[index]
        for i in range(len(row)):
            if row[i][0] == key:
                row.pop(i) #removes an item
                return
        raise KeyError('key does not exist')
            
    # update an item when valid key is provided
    def update(self, key, newValue):
        index = self.myHash(key)
        row = self.__data[index]
        for i in range(len(row)):
            if row[i][0] == key:
                row[i][1] = newValue
                return
        raise KeyError('key does not exist')