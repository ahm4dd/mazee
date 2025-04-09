from gui import Window, Point, Line
class Cell():
    def __init__(self, win: Window,
                # Optional parameters:
                has_left_wall: bool = True, has_right_wall: bool = True, has_top_wall: bool = True, has_bottom_wall: bool = True,  x1:int = None, x2:int = None, y1:int = None, y2:int = None):
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
        self._x1 = x1_top_left
        self._x2 = x2_bottom_right
        self._y1 = y1_top_left
        self._y2 = y2_bottom_right

        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)