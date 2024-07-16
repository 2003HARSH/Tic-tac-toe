# Tic-Tac-Toe using Minimax Algorithm

## Introduction
This project implements a command-line version of the classic Tic-Tac-Toe game in Python. It offers two modes of gameplay: 
- Player vs Computer
- Player vs Player

The game provides different levels of difficulty when playing against the computer.

## Features
- **Player vs Computer**: Play against an AI that utilizes the minimax algorithm for decision-making.
- **Player vs Player**: Play against another human player on the same machine.
- **Dynamic Board Display**: The game board is dynamically displayed after each move using ASCII characters.
- **Game Outcome Display**: The game displays the winner or if it ends in a draw using ASCII art.

## Requirements
- Python 3.x
- Myfiget (a python packgae developed by me for displaying Figlet font)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   cd repository-directory
   ```
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the game:
   ```bash
   python main.py
   ```
   
3. Follow the on-screen instructions to play:
   - Enter numbers from 1 to 9 to place your mark on the board during your turn.
   - Choose whether to play against the computer or another player.

## Gameplay Instructions
- The game board is displayed with positions numbered from 1 to 9, similar to the numeric keypad on a keyboard.
- Players take turns to place their mark ('X' or 'O') on the board.
- The game ends when a player wins by getting three marks in a row horizontally, vertically, or diagonally, or when the board is full (resulting in a draw).

## Credits
- This project uses the `myfiglet` library for ASCII art text display. `Myfiglet` library is developed by me.

## Example
![](https://github.com/2003HARSH/Tic-tac-toe/blob/main/docs/static/1.png)
![](https://github.com/2003HARSH/Tic-tac-toe/blob/main/docs/static/2.png)
![](https://github.com/2003HARSH/Tic-tac-toe/blob/main/docs/static/3.png)
![](https://github.com/2003HARSH/Tic-tac-toe/blob/main/docs/static/4.png)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
