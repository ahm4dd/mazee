from tkinter import Tk, BOTH, Canvas
class Point():
    def __init__(self, x: int = 0, y: int = 0):
        """
        Initializes a Point object with the given x and y coordinates.

        Args:
            x (int): The x-coordinate of the point. Defaults to 0.
            y (int): The y-coordinate of the point. Defaults to 0.
        """
        self.x = x
        self.y = y
class Line():
    def __init__(self, p1: Point, p2: Point):
        """
        Initializes a Line object with two points.

        Args:
            p1 (Point): The starting point of the line.
            p2 (Point): The ending point of the line.
        """
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "white") -> None:
        """
        Draws this line on the given canvas.

        Args:
            canvas (Canvas): The canvas to draw on.
            fill_color (str): The color to draw the line with. Defaults to "white".
        """
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window():
    def __init__(self, width: int, height: int):
        """
        Initializes a Window object with the given width and height.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """
        self.width = width  # Set the width of the window
        self.height = height  # Set the height of the window
        self.__root = Tk()  # Initialize the main Tkinter window
        self.__root.title("Ahm4dd's Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Set the protocol for the window to close (Basically calling self.close when the window closes to make sure the program stops looping and closes safely)
        self.__canvas = Canvas(self.__root, {"bg": "black"})  # Create a canvas with a black background to draw on
        self.__canvas.pack(fill=BOTH, expand=1)  # Pack the canvas into the window 
        self.__running = False  # Initialize the running state to False (Basically if the program is running or not)

    def redraw(self) -> None:
        """
        Updates the window by redrawing the canvas and calling the mainloop once to handle any events.
        All it does is call update_idletasks() to update the window but not process any events caused by the user (e.g. close button) and update() to update the window for all pending events
        """
        self.__root.update_idletasks() # Update the window but do not process any events caused by user (e.g. close button is an event caused by the user)
        self.__root.update() # Update the window for all pending events
    
    def wait_for_close(self) -> None:
        """
        Runs the main loop for this window until the window is closed. (Basically keep redrawing the window until the window is closed)
        """
        self.__running = True # Set the running state to True to start the main loop (while self.__running is True)
        while self.__running: # Keep redrawing the window until the window is closed (When self.__running is False)
            self.redraw()
    
    def close(self) -> None: # Close the window (This method is called when you close the window)
        """
        Closes the window and stops the main loop.
        This method is called when the window is closed.
        """
        self.__running = False
    
    def draw_line(self, line: Line, fill_color: str = "white") -> None:
        """
        Draws a line on the canvas.

        Args:
            line (Line): The line to draw.
            fill_color (str): The color to draw the line with. Defaults to "white".
        """
        line.draw(self.__canvas, fill_color) # Draw the line on the canvas of this current window


