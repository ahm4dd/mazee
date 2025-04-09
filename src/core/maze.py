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
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()
        
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)