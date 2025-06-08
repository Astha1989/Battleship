# Battleship

## 1. Project Overview

This is a simple command-line version of the classic **Battleship** game implemented in Python. The player is asked to guess the locations of five hidden ships on a customizable grid. The objective is to hit all ships within 10 turns. The game provides real-time feedback after each guess and displays the current state of the ocean grid.

## 2. Features

1. Allows the user to choose the number of rows and columns (maximum 9x9 grid).
2. Random placement of five ships on the board.
3. Interactive command-line input for making guesses.
4. Visual representation of the ocean grid using letters and numbers.
5. Marks:
   * 'O' for a successful hit.
   * 'X' for a missed attempt.
6. Prevents the user from guessing the same location twice.
7. Validates that guesses are within the grid limits.
8. Game ends when all ships are hit or the player runs out of 10 turns.

## 3. How the Game Works

1. When the program starts, the user is welcomed and prompted to enter the desired number of rows and columns (both between 1 and 9).
2. A blank 2D grid is created and displayed with labeled rows and columns.
3. The program randomly places five ships on the grid (locations are hidden from the player).
4. The user is then prompted to enter row and column guesses.
5. If the guessed coordinates match a ship’s location, it's marked as a hit.
6. If the guess is incorrect, it's marked as a miss.
7. The player has a total of 10 turns to hit all 5 ships.
8. If the player succeeds in hitting all ships before using all turns, a victory message is displayed.
9. If the player uses all 10 turns without hitting all ships, the game ends with a loss message.

## 4. Usage Instructions

1. Ensure you have Python 3 installed on your system.
2. Save the code in a `.py` file (for example, `battleship.py`).
3. Run the file using any Python IDE or terminal with the command:
   `python battleship.py`
4. Follow the prompts to enter grid dimensions and begin guessing ship positions.
5. After each turn, observe the updated grid and adjust your guesses accordingly.

## 5. Potential Improvements

1. Add support for different ship sizes and orientations.
2. Add a scoring system based on accuracy.
2. Introduce sound or visual elements using GUI libraries.

### Sample of game
![Image](https://github.com/user-attachments/assets/15af5561-3b0e-4a1e-956e-4f08384db0b7)
