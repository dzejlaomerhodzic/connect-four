# Connect Four AI Implementation

## Overview
This project implements a Connect Four game with an AI opponent utilizing the Minimax algorithm with Alpha-Beta Pruning. The AI strategically competes against a human player in a two-person game on a 6-row by 7-column grid.

## Features
- **Human vs AI Gameplay**: Play against an AI opponent that makes optimal moves.
- **Minimax Algorithm with Alpha-Beta Pruning**: The AI evaluates possible game states efficiently.
- **Game Mechanics**: Piece dropping, move validation, and win condition checks.
- **Modular Codebase**: Easily readable and maintainable functions.

## How to Play
1. Players take turns dropping pieces into one of the seven columns.
2. Pieces fall to the lowest available row in the selected column.
3. The first player to align four pieces in a row (horizontally, vertically, or diagonally) wins.
4. If the board is full and no player has four in a row, the game ends in a draw.

## Key Components
- **Game Board Initialization**: Uses a NumPy array to create a 6x7 grid.
- **Move Validation**: Ensures moves are legal before execution.
- **Winning Condition Check**: Detects if a player has won after each move.
- **Minimax Algorithm**: AI decision-making using game-tree evaluation.
- **Alpha-Beta Pruning**: Optimizes AI performance by eliminating unnecessary calculations.

## Installation
```sh
# Clone the repository
git clone https://github.com/your-username/connect-four.git
cd connect-four

# Install dependencies
pip install numpy

# Run the game
python connect_four.py
```

## Future Improvements
- **Dynamic AI Difficulty**: Adjustable AI depth based on game complexity.
- **Enhanced Evaluation Function**: Smarter AI decision-making.
- **Graphical User Interface**: A more interactive and visually appealing game experience.
- **Error Handling & Input Validation**: More robust handling of edge cases.

## Contributing
Feel free to fork the repository and submit pull requests to improve the game!

## License
This project is open-source and available under the MIT License.
