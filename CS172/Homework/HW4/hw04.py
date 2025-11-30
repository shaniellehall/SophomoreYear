# hw04.py
import pygame
import random
import time
from fly import Fly
from drawable import Drawable
from frog import Frog
from text import Text

# Initialize Pygame and set up the display
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Frog and Flies")

# Define colors
BLACK = (0, 0, 0)
BLUE = (62, 105, 133)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Game constants
INITIAL_FLIES = 5
WIN_SCORE = 20
GAME_DURATION = 30  # seconds
MIN_FLY_RADIUS = 5
MAX_FLY_RADIUS = 15

# Game state -Taken from CS164
class GameState:
    START = 0
    PLAYING = 1
    WON = 2
    LOST = 3

# Create game objects
frog = Frog(400, 300, 40, 40, GREEN)
flies = []
score = 0
start_time = 0
game_state = GameState.START

# Create text objects
score_text = Text(f"Score: {score}/{WIN_SCORE}", 10, 10, 24, BLACK)
timer_text = Text(f"Time: {GAME_DURATION}", 10, 40, 24, BLACK)
message_text = Text("Click to Start!", surface.get_width()//2, surface.get_height()//2, 36, WHITE)
message_text.center_text = True  # Assuming we added this property to Text class

def spawn_fly():
    """Spawn a new fly with random size and position"""
    radius = random.randint(MIN_FLY_RADIUS, MAX_FLY_RADIUS)
    x = random.randint(radius, surface.get_width() - radius)
    y = random.randint(radius, surface.get_height() - radius)
    return Fly(x, y, radius, BLACK)

def reset_game():
    """Reset the game state"""
    global score, start_time, flies
    score = 0
    start_time = time.time()
    flies = []
    for _ in range(INITIAL_FLIES):
        flies.append(spawn_fly())

# Main game loop
fpsClock = pygame.time.Clock()
running = True

while running:
    current_time = time.time()
    
    # Fill background
    surface.fill(BLUE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start game on click if in start screen
            if game_state == GameState.START:
                game_state = GameState.PLAYING
                reset_game()
    
    # Update game based on state
    if game_state == GameState.START:
        # Draw start screen
        message_text.set_Message("Click to Start!")
        message_text.draw(surface)
        
    elif game_state == GameState.PLAYING:
        # Update timer
        time_left = max(0, GAME_DURATION - (current_time - start_time))
        timer_text.set_Message(f"Time: {int(time_left)}")
        
        # Update game objects
        frog.follow_mouse()
        for fly in flies:
            fly.move_randomly()
            fly.draw(surface)
            
            # Check collision with frog
            if fly.isVisible() and frog.intersects(fly):
                score += 1
                fly.setVisible(False)
                # Spawn new fly
                flies.append(spawn_fly())
        
        # Draw frog and UI
        frog.draw(surface)
        score_text.set_Message(f"Score: {score}/{WIN_SCORE}")
        score_text.draw(surface)
        timer_text.draw(surface)
        
        # Check win/lose conditions
        if score >= WIN_SCORE:
            game_state = GameState.WON
        elif time_left <= 0:
            game_state = GameState.LOST
            
    elif game_state == GameState.WON:
        message_text.set_Message("You Won! Click to Play Again")
        message_text.draw(surface)
        if pygame.mouse.get_pressed()[0]:
            game_state = GameState.START
            
    elif game_state == GameState.LOST:
        message_text.set_Message("Time's Up! Click to Try Again")
        message_text.draw(surface)
        if pygame.mouse.get_pressed()[0]:
            game_state = GameState.START
    
    # Update display
    pygame.display.update()
    fpsClock.tick(60)

pygame.quit()