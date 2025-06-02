# Pong Game

A classic Pong game clone built with Python's turtle graphics library. This project recreates the iconic arcade game, allowing two players to compete against each other using keyboard controls.

## Features

- Two-player mode (W/S for left paddle, Up/Down for right paddle)
- Scoreboard with win condition
- Ball speed increases after each paddle hit
- Visual divider in the center
- Game over message when a player reaches the final score

## Controls

- **Left Paddle:**
  - Move Up: `W`
  - Move Down: `S`
- **Right Paddle:**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```sh
   git clone https://github.com/roshanbist/pong-game.git
   cd pong-game
   ```
3. Run the game:

   ```sh
   python main.py
   ```

   A new window will appear with the Pong game interface.

## File Structure

- `main.py` - Main game loop and setup
- [`paddle.py`](paddle.py) - Paddle class
- [`divider.py`](divider.py) - Divider class for center line
- [`ball.py`](ball.py) - Ball class with movement and collision logic
- [`scoreboard.py`](scoreboard.py) - Scoreboard and game over logic

## Screenshot

![Screenshot](screenshot/screenshot.png)

## License

This project is for educational purposes.
