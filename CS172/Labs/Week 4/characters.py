"""
Names: Shanielle Hall 	Alyn Tetteh
UserId:snh325			aet78
Purpose: This file sets up the definition for the classes Character, Monster and Hero
"""
# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self): #returns the name of the object
        return self.__name
    
    def getDescription(self): # returns the description of the object
        return self.__description
    
    def getWeaponName(self): # returns the weapon name of the object
        return self.__weaponName
    
    def getWeaponDamage(self): # returns the weapon damage of the object
        return self.__weaponDamage
    
    def attack(self, enemy): #initializes the attack method
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount): #initializes the attack takeDamage method
        self.__health -= amount
    
    def getHealth(self): # returns the health of the object
        return self.__health
    
    
## TODO: Create a Monster class that inherits from the Character class.
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        #TODO
        #Initialize parent class with provided information
        #Also create an attribute for motivation (a string)
        super().__init__(name, description, maxHealth, weaponName, weaponDamage) # inherits these attributes from the parent class
        self.__motivation = motivation # intializes the motivation attribute

        
    def __str__(self):
        #TODO
        #Return a string in the form:
        #<name> is a <description>
        #Weapon: <weapon>
        #Current Health: <health>
        #Motivation: <motivation>
        
        #prints the string for the monster class
        myStr = self.getName() + " is a " + self.getDescription()
        myStr += "Weapon: " + self.getWeaponName()
        myStr += "\nCurrent Health: " + str(self.getHealth())
        myStr += "\nMotivation: " + self.__motivation
        
        return myStr
    
    def react(self): 
        #TODO
        #return a string in the form:
        #<name> laughs maniacally.
        return self.getName() + " laughs maniacally."
    
    def getMotivation(self):
        #TODO
        #Return the monster's motivation
        return self.__motivation
        


## TODO: Create a Hero class that inherits from the Character class.
class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName):
        #TODO
        #Initialize parent class with provided information
        #Also creates attributes for defense name (string), and defending status (boolean)
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__defenseName = defenseName
        self.__isDefending = False
        
    def __str__(self):
        #TODO
        #Return a string in the form:  
        #Our hero <name> is a <description>
        #Weapon: <weapon>
        #Defense: <defenseName>
        #Current Health: <health>
        #Defense Status: <isDefending>
        myStr = "Our hero " + self.getName() + " is a " + self.getDescription() 
        myStr += "Weapon: " + self.getWeaponName() 
        myStr += "Defense: " + self.__defenseName
        myStr += "Current Health: " + str(self.getHealth()) 
        myStr += "Defense Status: " + str(self.__isDefending)
        return myStr
        
    def react(self):
        #TODO
        #Return a string in the form:
        #<name> charges bravely.
        return self.getName() + " charges bravely."
        
    def getDefenseName(self):
        #TODO
        #Return the defense name   
        return self.__defenseName
    
    def isDefending(self):
        #TODO
        #Return the defense status
        return self.__isDefending
    
    def defend(self):
        #TODO
        #Changes defense status to True
        self.__isDefending = True
        
    def takeDamage(self, amount):
        #TODO
        #Check defense status
        #If it is enabled (True), reduce the amount by 50%, and change the defense status to false.
        #Regardless, apply the final amount to the hero by calling its parent class' takeDamage method.
        if self.__isDefending:
            amount = amount * 0.5
            self.__isDefending = False
        super().takeDamage(amount)



# Test your Monster and Hero classes here before you work on the main.py file
if __name__ == "__main__":
    # Milestone 1: Create an instance of Monster and test its methods
    print('*** Testing Monster Class ***')
    monsterTest = Monster ('The Brain', 'Highly intelligent and scheming mouse', 10 , 'Laser beam', 2, 'to take over the world!')
    print(monsterTest)
    print('\nMotivation:', monsterTest.getMotivation())
    print('React:', monsterTest.react())
    print()
    
    # Milestone 2: Create an instance of Hero and test its methods
    
    print('*** Testing Monster Hero ***')
    heroTest = Hero ('Puss in Boots', 'Proud and honorable fighter', 10 , 'sword', 2, 'Cute Eyes tactic ')
    print(heroTest)
    print('\nDefense:', heroTest.getDefenseName())
    heroTest.defend()
    print('Is Defending?', heroTest.isDefending())
    print('React:', heroTest.react())
    print()
    heroTest.takeDamage(3)
    print(heroTest)