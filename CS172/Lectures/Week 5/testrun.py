#File:      basicPyGame.py
#Purpose:   Demo of a basic program using pygame
#Author:    S. Hall
#Date:      October 21, 2025


#import pygame so we can use its features
import pygame

#intialize API
pygame.init()

# create a graphics window to put our object in
# Provide dimensions of the window as a tuple (w, h)
surface = pygame.display.set_mode( (400, 300) )

"""
Tuple creation
t = ('red', 'white', 'blue')
t = (10, 20)
"""
# give window a title
pygame.display.set_caption('Hello World!!')

# the game loop
while True:
    #get each event from the queue, one event at the time and process the
    #one that we are interested in
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or \
        (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q): #if user presses the key 'Q' the program ends
            pygame.quit()
            exit()
            
    #display and image. Pygame handles: jpg, bmp, png
    #process: 1) load image file into memory
    #         2) copy image into target surface at a given x,y position
    
    catImg = pygame.image.load('cat.png')
    catX = 303 #x coordinate
    catY = 203 #y coordinate
    
    surface.blit(catImg, (catX, catY))
    
    #display text - we treat text as another image
    #process: 1) choose a font and a size
    #         2) create the text with the chosen font
    #         3) copy the text onto the target surface
    
    fontObj = pygame.font.Font("freesansbold.ttf", 24) #1
    textSurface = fontObj.render("Kitty Cat!", True, (255,255,0) ) #2
    surface.blit(textSurface, (10, 10))
    
    
    #update the display
    pygame.display.update()
    