# Frog and Flies Game

A time-based challenge game where you control a frog to catch multiple flies within a time limit.

## Prerequisites

Make sure you have Python and Pygame installed on your system:
- Python 3.x
- Pygame library

To install Pygame:
```bash
python -m pip install pygame
```

## How to Run

1. Open a terminal/command prompt
2. Navigate to the game directory:
   ```bash
   cd path/to/HW_04
   ```
3. Run the game:
   ```bash
   python hw04.py
   ```

## Game Rules

- **Goal**: Catch 20 flies before time runs out
- **Time Limit**: 30 seconds
- **Starting Flies**: 5 flies of varying sizes
- **Dynamic Spawning**: New flies appear when existing ones are caught

## How to Play

1. Click anywhere on the start screen to begin
2. Move your mouse to control the frog
3. Catch flies by touching them with your frog
4. Watch your score and remaining time
5. Get 20 flies before time runs out to win!

## Controls

- **Mouse Movement**: Controls the frog
- **Mouse Click**: Start game/Restart after win/loss
- **Q key**: Quit the game
- **Window Close (X)**: Alternative way to quit

## Game Features

- Multiple flies with varying sizes
- Real-time score counter (X/20)
- Countdown timer display
- Start screen with instructions
- Win/lose screens with restart option
- Dynamic difficulty (flies move randomly)

## Game States

1. **Start Screen**: "Click to Start!"
2. **Playing**: Active gameplay with score and timer
3. **Victory**: Displayed when reaching 20 flies
4. **Game Over**: Displayed when time runs out

## Files

- `hw04.py`: Main game file with game loop and states
- `drawable.py`: Base class for drawable objects
- `frog.py`: Frog player character implementation
- `fly.py`: Fly target implementation with varying sizes
- `text.py`: Text display system for UI elements