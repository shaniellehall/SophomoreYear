import pygame, random
from drawable import Drawable

# Fly class inheriting from Drawable
class Fly(Drawable):
    #Constructor
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius

    def draw(self, surface):
        #retu8rn if not visible
        if not self.isVisible():
            return

        #retrieve location and radius
        x, y = self.getLoc()
        r = int(self.__radius)

        # Body: oval shape
        body_w = int(r * 2.4)
        body_h = int(r * 1.4)
        body_rect = pygame.Rect(int(x - body_w // 2), int(y - body_h // 2), body_w, body_h)
        pygame.draw.ellipse(surface, self.__color, body_rect)

        # Head: small circle in front of the body
        head_r = max(2, int(r * 0.6))
        head_x = int(x + body_w * 0.28)
        head_y = int(y - body_h * 0.15)
        pygame.draw.circle(surface, (30, 30, 30), (head_x, head_y), head_r)

        # Eyes: two small white dots on the head
        eye_r = max(1, head_r // 2)
        eye_offset_x = max(1, head_r // 2)
        eye_offset_y = max(1, head_r // 2)
        pygame.draw.circle(surface, (255, 255, 255), (head_x - eye_offset_x, head_y - eye_offset_y), eye_r)
        pygame.draw.circle(surface, (255, 255, 255), (head_x - eye_offset_x, head_y + eye_offset_y), eye_r)

        # Antennae: thin lines from head
        pygame.draw.line(surface, (40, 40, 40), (head_x, head_y - 1), (head_x + 6, head_y - 8), 1)
        pygame.draw.line(surface, (40, 40, 40), (head_x, head_y + 1), (head_x + 6, head_y + 8), 1)

    #gets rectangle for collision detection
    def get_rect(self):
        x, y = self.getLoc()
        return pygame.Rect(x - self.__radius, y - self.__radius, self.__radius * 2, self.__radius * 2)
    
    #sets random movement within window
    def move_randomly(self):
        x, y = self.getLoc()
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)
        
        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        # Keep the fly within window
        x = max(self.__radius, min(width - self.__radius, x))
        y = max(self.__radius, min(height - self.__radius, y))

        self.setLoc(x, y)