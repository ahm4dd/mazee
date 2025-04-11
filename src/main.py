from core.gui import *
from core.cell import *
from core.maze import *
from constants import *
def main():
    # Calculate cell size based on window dimensions and maze grid
    cell_size_x = (WINDOW_WIDTH - 2 * MARGIN) / NUM_COLS
    cell_size_y = (WINDOW_HEIGHT - 2 * MARGIN) / NUM_ROWS
    
    # Create window
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    # Create and solve maze
    maze = Maze(MARGIN, MARGIN, NUM_ROWS, NUM_COLS, cell_size_x, cell_size_y, win)
    maze.solve()
    
    # Wait for user to close window
    win.wait_for_close()

if __name__ == "__main__":
    main()