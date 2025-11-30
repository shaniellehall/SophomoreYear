from drawable import Drawable
import pygame, random

# Frog class inheriting from Drawable
class Frog(Drawable):
    #Constructor
    def __init__(self, x=0, y=0, width=40, height=40, color=(0, 255, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        self.__height = height

    #draws the frog on the surface
    def draw(self, surface):
        if not self.isVisible():
            return
            
        x, y = self.getLoc()
        w, h = self.__width, self.__height

        # Draw body (oval)
        body_rect = pygame.Rect(x - w//2, y - h//2, w, h)
        pygame.draw.ellipse(surface, self.__color, body_rect)

        # Draw eyes (white with black pupils)
        eye_spacing = w // 4
        eye_y = y - h//8  # Slightly above center
        eye_radius = max(3, w // 10)
        
        # Left eye
        pygame.draw.circle(surface, (255, 255, 255), (x - eye_spacing, eye_y), eye_radius)
        pygame.draw.circle(surface, (0, 0, 0), (x - eye_spacing, eye_y), eye_radius // 2)
        
        # Right eye
        pygame.draw.circle(surface, (255, 255, 255), (x + eye_spacing, eye_y), eye_radius)
        pygame.draw.circle(surface, (0, 0, 0), (x + eye_spacing, eye_y), eye_radius // 2)

    #gets rectangle for collision detection
    def get_rect(self):
        x, y = self.getLoc()
        return pygame.Rect(x - self.__width // 2, y - self.__height // 2, self.__width, self.__height)
    
    #follow mouse position
    def follow_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.setLoc(mouse_x, mouse_y)