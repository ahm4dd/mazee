from core.gui import Window
from core.cell import Cell
import random
import time

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window = None):
        """
        Initializes a Maze object with the given parameters.

        The Maze class is the class that builds the actual maze and animates it.
        It uses the Cell class to create the cells and the Window class to draw them on the screen.

        Args:
            x1 (int): The x-coordinate of the top left corner of the maze.
            y1 (int): The y-coordinate of the top left corner of the maze.
            num_rows (int): The number of rows in the maze.
            num_cols (int): The number of columns in the maze.
            cell_size_x (float): The width of each cell in the maze.
            cell_size_y (float): The height of each cell in the maze.
            win (Window): The window to draw the maze on. Defaults to None
        """
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

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

        Args:
            i (int): The column index of the cell.
            j (int): The row index of the cell.
        """

        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x # Calculate the x-coordinate of the top left corner of the cell
        y1 = self._y1 + j * self._cell_size_y # Calculate the y-coordinate of the top left corner of the cell
        x2 = x1 + self._cell_size_x # Calculate the x-coordinate of the bottom right corner of the cell
        y2 = y1 + self._cell_size_y # Calculate the y-coordinate of the bottom right corner of the cell
        self._break_entrance_and_exit()
        self._cells[i][j].draw(x1, x2, y1, y2)
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
