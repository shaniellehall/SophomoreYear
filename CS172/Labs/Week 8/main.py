#Main file building the maze
#Shanielle Hall snh325


from room import Room
from maze import Maze
def play(my_maze):
    #Play a game
    while not my_maze.atExit():
        
        ## TODO: Get direction from user
        current_room = my_maze.getCurrent()
        str(current_room)
        
        option = input("Enter direction to move north west east south restart\n").strip().lower()
        if option.lower() == "north":
            my_maze.moveNorth()
        elif option.lower() == "west":
            my_maze.moveWest()
        elif option.lower() == "east":
            my_maze.moveEast()
        elif option.lower() == "south":
            my_maze.moveSouth()
        elif option.lower() == "reset":
            my_maze.reset()
        else:
            print("Direction invalid, try again.")
    if my_maze.atExit():
        print("")


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE

room1 = Room("This room is the entrance.")
room2 = Room("This room has a table. Maybe a dining room?")
room3 = Room("This room is the exit. Good Job.")

#room 2 is north of room 1. Make sure to connect them both ways
#(it's not a 1-way door!)
room1.setNorth(room2)
room2.setSouth(room1)
#room 3 is east of room 2. Make sure to connect them both ways
#(it's not a 1-way door!)
room2.setEast(room3)
room3.setWest(room2)
SIMPLE_MAZE = (room1, room3)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE
r1 = Room("Room1")
r2 = Room("Room2")
r3 = Room("Room3")
r4 = Room("Room4")
r5 = Room("Room5")
r6 = Room("Room6")

r1.setWest(r2)
r2.setEast(r1)

r2.setWest(r3)
r3.setEast(r2)

r3.setWest(r4)
r4.setEast(r3)

r4.setNorth(r5)
r5.setSouth(r4)

r5.setEast(r6)
r6.setWest(r5)


INTERMEDIATE_MAZE = Maze(r1, r6)


if __name__=="__main__":
    #Define this play function above and run on your INTERMEDIATE_MAZE
    print("testing implementation of maze")
    play(INTERMEDIATE_MAZE)
