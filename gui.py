from tkinter import Tk, BOTH, Canvas
class Point():
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "white") -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, {"bg":"black"})
        self.__canvas.pack()
        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False
    
    def draw_line(self, line: Line, fill_color: str = "white") -> None:
        line.draw(self.__canvas, fill_color)


