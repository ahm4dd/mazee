from gui import *
def main():
    win = Window(800, 600)
    p1 = Point(400, 200)
    p2 = Point(300, 100)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()