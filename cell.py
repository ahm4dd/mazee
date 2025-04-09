from gui import Window, Point, Line
class Cell():
    def __init__(self, x1:int, x2:int, y1:int, y2:int, win: Window, has_left_wall: bool = True, 
                has_right_wall: bool = True, has_top_wall: bool = True, has_bottom_wall: bool = True):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
    