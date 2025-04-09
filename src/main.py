from core.gui import *
from core.cell import *
def main():
    win = Window(800, 600)
    # p1 = Point(400, 200)
    # p2 = Point(300, 100)
    # line = Line(p1, p2)
    # win.draw_line(line, "red")
    cell = Cell(win)
    cell.draw(50, 100, 50, 100) 
    cell2 = Cell(win)
    cell2.draw(200, 300, 200, 300)
    cell.draw_move(cell2)
    win.wait_for_close()

main()