"""
NAMES AND USERID
Shanielle Hall snh325
Alyn Tetteh    aet78
"""

from birthday import Birthday #imports the birthday file
import os

class OpenHashTable:
    #constructor
    def __init__(self, birthday): 
        self.__birthday = int(birthday)
        self.__data = []
        for i in range(0, self.__birthday):
            self.__data.append([])
    
    
    def __str__(self):
        hashtabletStr = "Open Hash Table\n" 
        hashtabletStr += f"My birthday is {self.__birthday}\n"
        for i in range(0, self.__birthday):
            hashtabletStr += f"data[{i}] = {self.__data[i]}\n"
        hashtabletStr += "End of Hash Table"
        return hashtabletStr
    
    
    def myHash(self, key):
        return hash(key) % self.__birthday 
    
   
    def insert(self, key, value):
        index = self.myHash(key)
        row = self.__data[index]
        for pair in row:
            if pair[0] == key:
                raise KeyError('key already exists')             
        self.__data[index].append([key, value])
          
    def searchByKey(self, key):
        index = self.myHash(key)
        row = self.__data[index]
        for pair in row:
            if pair[0] == key:
                return pair[1]
        raise KeyError('key does not exist')
    
    def remove(self, key):
        index = self.myHash(key)
        row = self.__data[index]
        for i in range(len(row)):
            if row[i][0] == key:
                row.pop(i)
                return
        raise KeyError('key does not exist')
            
    
    def update(self, key, newValue):
        index = self.myHash(key)
        row = self.__data[index]
        for i in range(len(row)):
            if row[i][0] == key:
                row[i][1] = newValue
                return
        raise KeyError('key does not exist')
    

#Read in a list of birthdays from the supplied bdaylist.txt file
valid = True
while valid:
    filename = input("Enter name of the data file: ") #Ask the user to enter the name of the data file
    if os.path.isfile(filename):
        break
    else: print("Error: that file does not exist. Try again.")
    
#, open and read the data in the file in the following format: day/month/year
    
file = open(filename,"r")
lines = file.readlines()
file.close() #close the file after reading

#Create and populate a Hash Table
hashtable = OpenHashTable(12)

lineNum = 1

"""
For each birthday, create a Birthday object, and add the tuple (Birthday, i)
to the appropriate list in the hash table, where i is the line number from the input
file
"""
for line in lines:
    line= line.strip()
    
    if line != "":
        parts = line.split("/")
    if len(parts) == 3:
        day = parts[0]
        month = parts[1]
        year= parts[2]
        
        birthday = Birthday(month,day,year)
        
        index = hash(birthday) %12
        
        hashtable.insert(birthday,lineNum)
    lineNum = lineNum + 1
print() 

for index in range(12):
    bday_size = len(hashtable._OpenHashTable__data[index])
    print(f"Hash location {index} has {bday_size} elements in it.") #Output the total length of the list at each of the hash locations
