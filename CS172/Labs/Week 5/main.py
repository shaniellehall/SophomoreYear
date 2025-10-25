"""
ADD YOUR NAME AND USER ID HERE:
Shanielle Hall snh325
Alyn Tetteh    aet78

Purpose:    This program creates a 'Winter Wonderland' where there are two rectangles(sky and ground), and animated snowflakes.
            This program also gives the user the option to press the space bar to pause the snowflakes.
"""

# import necessary modules and classes

import pygame
from drawable import * 

# initialize Pygame and create window
pygame.init()
width = 500
height = 500
surface = pygame.display.set_mode((width, height))

ground = Rectangle(0, 300, 500, 300, (86, 180, 70)) # use to test Rectangle - may need to remove later
sky = Rectangle(0, 000, 500, 300, (173, 216, 230))    # use to test Rectangle - may need to remove later
snowflake = Snowflake(50, 50)                    # use to test Rectangle - may need to remove later


# The snowflake draw loop
drawables = [ground, sky] #list of drawables including the ground and the sky

clock = pygame.time.Clock()

# the game loop
while True:
    for event in pygame.event.get():  
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q): #if the user presses the key 'Q', the program ends
            pygame.quit()
            exit()

    x = random.randint(10, width)  
    snowflake = Snowflake(x, 0)
    drawables.append(snowflake)
    
    surface.fill((0, 0, 0))
    
    for item in drawables:
        if isinstance(item, Snowflake):
            x, y = item.getLoc()
            item.setLoc((x, y + 1))  #updates the y coordinate of each snowflake
            
        item.draw(surface)
    
    pygame.display.update()
    clock.tick(60)
    #ground.draw(surface)      # use to test Rectangle - may need to remove later
    #sky.draw(surface)         # use to test Rectangle - may need to remove later
    #snowflake.draw(surface)  # use to test Snowflake - may need to remove later
    
    pygame.display.update()