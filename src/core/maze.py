from core.gui import Window
from core.cell import Cell
import random
import time

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window = None, seed: int = None):
        """
        Initializes a Maze object with the given parameters.

        The Maze class is responsible for constructing the maze layout and handling its animation.
        It utilizes the Cell class to generate individual cells and the Window class for graphical rendering.

        Args:
            x1 (int): The x-coordinate of the top left corner of the maze.
            y1 (int): The y-coordinate of the top left corner of the maze.
            num_rows (int): The number of rows in the maze.
            num_cols (int): The number of columns in the maze.
            cell_size_x (float): The width of each cell in the maze.
            cell_size_y (float): The height of each cell in the maze.
            win (Window, optional): The window to draw the maze on. Defaults to None.
            seed (int, optional): The seed for the random number generator. Defaults to None.
        """
        # Set the random seed if provided to ensure reproducibility
        if seed is not None:
            random.seed(seed)

        # Initialize the maze grid and its properties
        self._cells = []  # A 2D list to store the cells of the maze
        self._x1 = x1  # X-coordinate of the top left corner of the maze
        self._y1 = y1  # Y-coordinate of the top left corner of the maze
        self._num_rows = num_rows  # Total number of rows in the maze
        self._num_cols = num_cols  # Total number of columns in the maze
        self._cell_size_x = cell_size_x  # Width of each cell
        self._cell_size_y = cell_size_y  # Height of each cell
        self._win = win  # The window object where the maze will be drawn

        # Create the cells for the maze
        self._create_cells()

        # Start breaking walls to form the maze path using recursive backtracking
        self._break_walls_r(0, 0)
        
        # Reset the visited status of all cells
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        """
        Creates a 2D list of Cell objects and draws them on the window.

        The outer list is a list of columns, and the inner list is a list of cells in each column.
        The cells are drawn on the window in the order they are created, which is from left to right and top to bottom.

        Args:
            None
        """
        for i in range(self._num_cols): # A loop to create a 2D list of cells
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win)) # Create a cell and add it to the column
            self._cells.append(col_cells) # Add the column to the 2D list of our current maze

        for i in range(self._num_cols): # A loop to draw each cell
            for j in range(self._num_rows):
                self._draw_cell(i, j) # Draw each cell

    def _draw_cell(self, i: int, j: int) -> None:
        """
        Draws a cell at the specified column and row indices.

        Calculates the coordinates of the cell based on its position in the grid and the size of each cell.
        Calls the draw method of the Cell object to render it on the window and animates the drawing process.

        It also breaks the entrance and exit walls of the maze.

        Args:
            i (int): The column index of the cell.
            j (int): The row index of the cell.
        """

        if self._win is None:
            return

        # Calculate the coordinates of the cell based on its position in the grid and the size of each cell
        x1 = self._x1 + i * self._cell_size_x  # Calculate the x-coordinate of the top left corner of the cell
        y1 = self._y1 + j * self._cell_size_y  # Calculate the y-coordinate of the top left corner of the cell
        x2 = x1 + self._cell_size_x  # Calculate the x-coordinate of the bottom right corner of the cell
        y2 = y1 + self._cell_size_y  # Calculate the y-coordinate of the bottom right corner of the cell

        # Remove the entrance and exit walls
        self._break_entrance_and_exit()

        # Draw the cell
        self._cells[i][j].draw(x1, x2, y1, y2)

        # Animate the drawing process
        self._animate()
        
    def _animate(self) -> None:
        """
        Animates the drawing process of the maze by redrawing the window and pausing for a short period of time.
        
        This method is called after each cell is drawn to give the appearance of the maze being drawn in real-time.
        """
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        """
        Removes the entrance and exit walls of the maze.

        This method breaks the left wall of the top-left cell to create an entrance
        and breaks the bottom wall of the bottom-right cell to create an exit.
        It then redraws the affected cells to visually update the maze.
        """
        self._cells[0][0].has_left_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False

    def _break_walls_r(self, i, j):
        """
        Recursively breaks walls between cells to create a random maze path using Depth-First Search (DFS).

        This method uses a recursive backtracking algorithm to visit each cell in the maze,
        breaking walls between the current cell and a randomly chosen unvisited neighboring cell.
        It continues this process until all cells have been visited, creating a solvable maze.

        Args:
            i (int): The column index of the current cell.
            j (int): The row index of the current cell.
        """
        # Check if the current cell exists
        if i < 0 or i >= self._num_cols or j < 0 or j >= self._num_rows:
            return
        
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        while True:
            # List to store unvisited neighboring cells
            to_visit = []
            
            # Check neighbors (left, top, right, bottom) and add unvisited ones to the list
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            
            # If no unvisited neighbors, exit the loop
            if len(to_visit) == 0:
                # Redraw the current cell to visualize the path
                self._draw_cell(i, j)
                return
            else:
                # Randomly select one of the unvisited neighbors
                next = random.choice(to_visit)
                
                # Break the wall between the current cell and the chosen neighbor
                if next[0] == i - 1:  # Move left
                    self._cells[i][j].has_left_wall = False
                    self._cells[next[0]][next[1]].has_right_wall = False
                elif next[0] == i + 1:  # Move right
                    self._cells[i][j].has_right_wall = False
                    self._cells[next[0]][next[1]].has_left_wall = False
                elif next[1] == j - 1:  # Move up
                    self._cells[i][j].has_top_wall = False
                    self._cells[next[0]][next[1]].has_bottom_wall = False
                elif next[1] == j + 1:  # Move down
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next[0]][next[1]].has_top_wall = False
                
                # Recursively visit the chosen neighbor
                self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        """
        Resets the visited status of all cells in the maze.

        This method is used to reset the maze after it has been solved.
        It sets the visited status of all cells to False, allowing the maze to be solved again.
        """
        # Loop through all cells in the maze
        for i in range(self._num_cols): # A loop to create a 2D list of cells
            for j in range(self._num_rows):
                # Reset the visited status of each cell
                self._cells[i][j].visited = False
    
    def solve(self):
        """
        Solves the maze using a recursive depth-first search algorithm.

        This method is the entry point for solving the maze. It calls the recursive
        helper method _solve_r() to start the search from the top-left cell of the maze.
        If the search is successful, it returns True. If the search is unsuccessful, it returns False.
        """
        # Start the search from the top-left cell
        if self._solve_r(0, 0):
            # If the search is successful, return True
            return True
        # If the search is unsuccessful, return False
        return False
    
    def _solve_r(self, i: int, j: int):
        """
        Solves the maze using a recursive depth-first search algorithm.

        This method is the recursive helper method for the solve() method. It is
        called to start the search from the top-left cell of the maze. If the search
        is successful, it returns True. If the search is unsuccessful, it returns False.

        Args:
            i (int): The column index of the current cell.
            j (int): The row index of the current cell.
        """
        if (i > 0 or i < self._num_cols) and (j > 0 or j < self._num_rows):
            # Animate the drawing process
            self._animate()
            # Mark the current cell as visited
            self._cells[i][j].visited = True
            
            # If the current cell is the exit, return True
            if i == self._num_cols - 1 and j == self._num_rows - 1:
                return True
            
            # Check the four possible directions to move
            # If the direction is valid (i.e., the cell is not visited and there is no wall in the way)
            # draw the move, recursively call _solve_r() to continue the search,
            # and if the search is successful, return True
            # If the search is unsuccessful, draw the move again (with a different color to indicate failure)
            # and return False
            
            # Left direction
            if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)
            # Top direction
            if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)
            # Right direction
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)
            # Bottom direction
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False
