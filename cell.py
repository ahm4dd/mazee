from gui import Window, Point, Line
class Cell():
    def __init__(self, win: Window,
                # Optional parameters:
                has_left_wall: bool = True, has_right_wall: bool = True, has_top_wall: bool = True, has_bottom_wall: bool = True,  x1:int = None, x2:int = None, y1:int = None, y2:int = None):
        """
        Initializes a Cell object with a window and optional parameters to specify whether the cell has a left, right, top, or bottom wall, and the coordinates of the cell.

        Args:
            win (Window): The window to draw the cell on.
            has_left_wall (bool): Whether the cell has a left wall. Defaults to True.
            has_right_wall (bool): Whether the cell has a right wall. Defaults to True.
            has_top_wall (bool): Whether the cell has a top wall. Defaults to True.
            has_bottom_wall (bool): Whether the cell has a bottom wall. Defaults to True.
            x1 (int): The x-coordinate of the top left corner of the cell. Defaults to None.
            x2 (int): The x-coordinate of the bottom right corner of the cell. Defaults to None.
            y1 (int): The y-coordinate of the top left corner of the cell. Defaults to None.
            y2 (int): The y-coordinate of the bottom right corner of the cell. Defaults to None.
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
    
    def draw(self, x1_top_left: int, x2_bottom_right: int, y1_top_left: int, y2_bottom_right: int) -> None:
        """
        Draws this cell on the given window.

        Args:
            x1_top_left (int): The x-coordinate of the top left corner of the cell.
            x2_bottom_right (int): The x-coordinate of the bottom right corner of the cell.
            y1_top_left (int): The y-coordinate of the top left corner of the cell.
            y2_bottom_right (int): The y-coordinate of the bottom right corner of the cell.
        """
        self._x1 = x1_top_left
        self._x2 = x2_bottom_right
        self._y1 = y1_top_left
        self._y2 = y2_bottom_right

        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2)) # Create a line from the top right corner to the bottom right corner
            self._win.draw_line(line) # Draw the line on the window
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2)) # Create a line from the top left corner to the bottom left corner
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1)) # Create a line from the top left corner to the top right corner
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2)) # Create a line from the bottom left corner to the bottom right corner
            self._win.draw_line(line)