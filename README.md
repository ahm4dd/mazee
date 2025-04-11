# mazee

A Python application that generates and solves random mazes using a recursive backtracking algorithm. The application creates a visual representation of the maze and animates both the generation and solving processes.

![Maze Solver Demo](nothing.git)

## Features

- Random maze generation using depth-first search algorithm
- Animated maze construction and solution finding
- Customizable maze dimensions and appearance through constants
- Visual tracking of the solution path and dead ends

## Installation

### Prerequisites

- Python 3.10 or higher
> To install visit: https://www.python.org/downloads/
  
- Tkinter (usually comes pre-installed with Python)
> To install on Linux (Ubuntu)
```bash
sudo apt-get install python3-tk
```
> To install on MacOS:
```zsh
brew install python-tk
```

> Check if it was installed:
```bash
python3 -m tkinter
# If python3 -m tkinter still isn't working, you may need to uninstall and reinstall Python so that it links to the now-available Tcl/Tk library.
```
### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ahm4dd/mazee.git
   cd mazee
   ```

2. No additional dependencies required! The project uses only Python's standard library.

## Usage

Run the application:

```bash
python src/main.py
```

This will:
1. Generate a random maze
2. Animate the maze generation process
3. Automatically solve the maze
4. Display the solution path in red (successful paths) and gray (dead ends)

### Customizing the Maze

You can easily modify the maze appearance and behavior by editing the parameters in `constants.py`:

```python
# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_BG_COLOR = "black"

# Maze dimensions
NUM_ROWS = 12
NUM_COLS = 16
MARGIN = 50

# Animation settings
ANIMATION_SPEED = 0.05  # seconds between frames (lower = faster)

# Colors
WALL_COLOR = "white"
PATH_COLOR = "red"
BACKTRACK_COLOR = "gray"
ERASER_COLOR = "black"

# Cell line settings
LINE_WIDTH = 2
```

### Running Tests

The project includes unit tests to verify the functionality of the maze generation and solving algorithms:

```bash
python src/tests.py
```

## Project Structure

- `src/constants.py` - Central configuration file for customizable parameters
- `src/core/gui.py` - Handles window creation and drawing functionality
- `src/core/cell.py` - Defines the Cell class for individual maze cells
- `src/core/maze.py` - Implements maze generation and solving algorithms
- `src/main.py` - Main entry point for the application
- `src/tests.py` - Unit tests for the maze functionality

## How It Works

1. **Maze Generation**: Uses a recursive backtracking algorithm to create a random maze.
2. **Maze Solving**: Uses depth-first search to find a path from entrance to exit.
3. **Visualization**: Animates the maze solving process with color-coded paths.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
