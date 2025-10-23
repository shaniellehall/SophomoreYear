#File:      basicPyGame.py
#Purpose:   Demo of a basic program using pygame
#Author:    A. Medlock
#Date:      October 21, 2024

#imports needed
import pygame

# initialize pygame
pygame.init()

# create a graphics window to put our object in
# Provide dimensions of the window as a tuple (w, h)
surface = pygame.display.set_mode((400, 300))

# give window a title
pygame.display.set_caption('Hello Kitty!')

# the game loop
while True: 
    #get each event from queue and process it
    for event in pygame.event.get():  
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
            
    # display an image: jpg, gif, png, bmp
    # process: load image file, copy image into target surface        
    catImg = pygame.image.load('cat.png')
    catX = 304   #coodinate x where the image will be placed
    catY = 204   #coodinate y where the image will be placed
    surface.blit(catImg, (catX, catY))
    
    # display some text
    # process: 1) choose a font and size, 
    #          2) create text using font, 
    #          3) copy text into target surface
    fontObj = pygame.font.Font("freesansbold.ttf", 24)
    textSurface = fontObj.render("Kitty Cat!", True, (255, 255, 0))
    surface.blit(textSurface, (10, 10))
    
    #update the display
    pygame.display.update()
