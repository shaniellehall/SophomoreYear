#Mark Boady
#CS 172 - Maze Game
#Drexel University 2018
#Shanielle Hall snh325

class Maze:
    #Inputs: Pointers to start room and exit room
    #Sets current to be start room
    def __init__(self, st = None, ex = None): 
        #Room the player starts in
        self.__st = st
        #If the player finds this room they win
        self.__ex = ex
        #What room is the player currently in
        self.__current = st
        
    #Return the room the player is in (current)
    def getCurrent(self):
        return self.__current

    #The next four methods all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new room (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
        if self.__current is None or self.__current.getNorth() is None:
            print("Direction invalid, try again.")
            return False # Return False on invalid move
        else:
            self.__current = self.__current.getNorth()
            print("You went north")
            print(self.__current) # Print room description
            if self.atExit():
                print("You found the exit!")
            return True
    
    def moveSouth(self):
        if self.__current is None or self.__current.getSouth() is None:
            print("Direction invalid, try again.")
            return False # Return False on invalid move
        else:
            self.__current = self.__current.getSouth()
            print("You went south")
            print(self.__current) # Print room description
            if self.atExit():
                print("You found the exit!")
            return True
        
    def moveEast(self):
        if self.__current is None or self.__current.getEast() is None:
            print("Direction invalid, try again.")
            return False # Return False on invalid move
        else:
            self.__current = self.__current.getEast()
            print("You went east")
            print(self.__current) # Print room description
            if self.atExit():
                print("You found the exit!")
            return True
    
    def moveWest(self):
        if self.__current is None or self.__current.getWest() is None:
            print("Direction invalid, try again.")
            return False # Return False on invalid move
        else:
            self.__current = self.__current.getWest()
            print("You went west")
            print(self.__current) # Print room description
            if self.atExit():
                print("You found the exit!")
            return True

    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        return self.__current is not None and self.__ex is not None and self.__current == self.__ex

    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start room
    def reset(self):
        # TODO
        self.__current = self.__st
        print("You went back to the start!")
        if self.__current is not None:
            print(self.__current) # Use print(self.__current) instead of print(self.__current.getDescription())