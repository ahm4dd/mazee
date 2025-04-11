from core.gui import Window, Point, Line
class Cell():
    def __init__(self, win: Window = None,
                # Optional parameters:
                has_left_wall: bool = True, has_right_wall: bool = True, has_top_wall: bool = True, has_bottom_wall: bool = True,  
                x1: int = None, x2: int = None, y1: int = None, y2: int = None,
                visited: bool = False):
        """
        Initializes a Cell object with a window and optional parameters for walls and coordinates.

        Args:
            win (Window, optional): The window to draw the cell on. Defaults to None.
            has_left_wall (bool, optional): Whether the cell has a left wall. Defaults to True.
            has_right_wall (bool, optional): Whether the cell has a right wall. Defaults to True.
            has_top_wall (bool, optional): Whether the cell has a top wall. Defaults to True.
            has_bottom_wall (bool, optional): Whether the cell has a bottom wall. Defaults to True.
            x1 (int, optional): The x-coordinate of the top left corner of the cell. Defaults to None.
            x2 (int, optional): The x-coordinate of the bottom right corner of the cell. Defaults to None.
            y1 (int, optional): The y-coordinate of the top left corner of the cell. Defaults to None.
            y2 (int, optional): The y-coordinate of the bottom right corner of the cell. Defaults to None.
            visited (bool, optional): Whether the cell has been visited. Defaults to False.
        """
        # Initialize the coordinates of the cell
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        # Set the window to draw the cell on
        self._win = win
        
        # Initialize the walls of the cell
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
        # Flag to indicate if the cell has been visited
        self.visited = visited
    
    def draw(self, x1_top_left: int, x2_bottom_right: int, y1_top_left: int, y2_bottom_right: int) -> None:
        """
        Draws the cell on the window with its walls based on the given coordinates.

        Args:
            x1_top_left (int): The x-coordinate of the top left corner of the cell.
            x2_bottom_right (int): The x-coordinate of the bottom right corner of the cell.
            y1_top_left (int): The y-coordinate of the top left corner of the cell.
            y2_bottom_right (int): The y-coordinate of the bottom right corner of the cell.
        """
        # Update cell coordinates
        self._x1 = x1_top_left
        self._x2 = x2_bottom_right
        self._y1 = y1_top_left
        self._y2 = y2_bottom_right

        # Draw or remove right wall
        if self.has_right_wall:
            # Draw right wall
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            # Remove right wall by drawing in black
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

        # Draw or remove left wall
        if self.has_left_wall:
            # Draw left wall
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        else:
            # Remove left wall by drawing in black
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")

        # Draw or remove top wall
        if self.has_top_wall:
            # Draw top wall
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        else:
            # Remove top wall by drawing in black
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")

        # Draw or remove bottom wall
        if self.has_bottom_wall:
            # Draw bottom wall
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            # Remove bottom wall by drawing in black
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
    
    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        """
        Draws a line from the center of this cell to the center of the given cell to indicate a move.
        Args:
            to_cell (Cell): The cell to move to.
            undo (bool): Whether this move is an undo move. If True, draw the line in gray. If False, draw the line in red. Defaults to False.
        """
        point_cell1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2) # Get the center point of the current cell
        point_cell2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2) # Get the center point of the target cell
        line = Line(point_cell1, point_cell2) # Create a line from the center point of the current cell to the center point of the target cell
        if undo:
            self._win.draw_line(line, "gray") # Draw the line in gray
        else:
            self._win.draw_line(line, "red") # Draw the line in red