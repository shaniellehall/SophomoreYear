from drawable import Drawable
import pygame, random

# Text class inheriting from Drawable
class Text(Drawable):
    #Constructor
    def __init__(self, message = "Score: 0", x=0, y=0, font_size=24, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__text = message
        self.__font_size = font_size
        self.__color = color
        self.__font = pygame.font.Font(None, self.__font_size)
        self.center_text = False  # New property for text alignment

    #draws text on surface
    def draw(self, surface):
        if self.isVisible():
            text_surface = self.__font.render(self.__text, True, self.__color)
            x, y = self.getLoc()
            if self.center_text:
                # Center the text at the given position
                rect = text_surface.get_rect(center=(x, y))
                surface.blit(text_surface, rect)
            else:
                # Default top-left alignment
                surface.blit(text_surface, (x, y))

    #gets rectangle for collision detection
    def get_rect(self):
        text_surface = self.__font.render(self.__text, True, self.__color)
        x, y = self.getLoc()
        return text_surface.get_rect(topleft=(x, y))
    
    #sets message text
    def set_Message(self, message):
        self.__text = message
