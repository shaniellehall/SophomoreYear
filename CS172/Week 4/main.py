"""
Names: Shanielle Hall 	Alyn Tetteh
UserId:snh325			aet78
Purpose: This program simulates a turn based game between a monster and a hero.
The user inputs the characters for the game, and follows the instructions,
with each input affecting the results of the game
"""

######TODO######    
#import the Monster and Hero classes here
from characters import Monster, Hero

import random

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
    
    #Whose turn is it?
    attacker = None
    defender = None

    ######TODO######    
    #Select Randomly whether h1 or m1 is the initial attacker
    #the other is the initial defender
    if random.choice([True, False]):
        attacker = h1
        defender = m1
    else:
        attacker = m1
        defender = h1
        
    print(attacker.getName() + " goes first.")
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        beforeHealth = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
            
            
            ######TODO######    
            #Have the attacker react.
            #Have the attacker attack.
            #Call the print_results function with the necessary info.
            print(attacker.react())
            attacker.attack(defender)
            damageDone = beforeHealth - defender.getHealth()
            printResults(attacker, defender, attacker.getWeaponName(), damageDone)


        else:
            # Asks the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
        
            ######TODO######    
            #Based on the input, either attack, defend, or end loop
            #If they chose to attack, have the attacker react, attack and then
            #call the print_results function with the necessary info.
            if action == 'a':
                print(attacker.react())
                attacker.attack(defender)
                damageDone = beforeHealth - defender.getHealth()
                printResults(attacker, defender, attacker.getWeaponName(), damageDone)
            elif action == 'd':
                attacker.defend()
                print("Our hero is defending with", attacker.getDefenseName(), "!")
            elif action == 'p':
                stop = True
                print("Battle stopped!")
            else:
                print("Invalid choice. Please choose a, d, or p.")
                continue
        
        ######TODO######
        #Swap attacker and defender
        temp = attacker
        attacker = defender
        defender = temp 
        

    ######TODO######    
    #Print out who won.
    #Return who won.
    print("Battle is over. Let's see who has won...")
    if h1.getHealth() > 0 and m1.getHealth() <= 0:
        print(h1.getName() + " is victorious!")
        return h1
    elif m1.getHealth() > 0 and h1.getHealth() <= 0:
        print(m1.getName() + " is victorious!")
        return m1
    else:
        print("It's a tie!")
        return None
    
    
#This function prints the status updates
def printResults(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))


#----------------------------------------------------
if __name__=="__main__":
    
    ######TODO######    
    #Get Monster's name, description, maxHealth, weaponName, weaponDamage, and motivation from the user here.
    #Instantiate a Monster using that info. Note that weaponDamage should be a floating point number.
        
    #myMonster = None  #this should be an instance of your Monster class
    monsterName = input("Enter monster's name: ")
    monsterDescription = input("Enter monster's description: ")
    monsterHealth = float(input("Enter a number for monster's health: "))
    monsterWeapon = input("Enter monster's weapon name: ")
    monsterDamage = float(input("Enter monster's weapon damage (as a number): "))
    monsterMotivation = input("Enter monster's motivation: ")
    
    myMonster = Monster(monsterName, monsterDescription, monsterHealth, monsterWeapon, monsterDamage, monsterMotivation)
    
    ######TODO######    
    #Get the Hero's name,description, maxHealth, weaponName, weaponDamage, defenseName from the user here.
    #Instantiate a Hero using that info. Note that weaponDamage should be a floating point number.
    heroName = input("Enter hero's name: ")
    heroDescription = input("Enter the hero's description: ")
    heroHealth = float(input("Enter a number for the hero's health: "))
    heroWeapon = input("Enter hero's weapon name: ")
    heroDamage = float(input("Enter hero's weapon damage (as a number): "))
    heroDefense = input("Enter the hero's defense name: ")
    
    myHero = Hero(heroName, heroDescription, heroHealth, heroWeapon, heroDamage, heroDefense)
    
    winner = monster_battle(myHero, myMonster)
