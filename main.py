from window import *
from cell import *
from line import *
from point import *

def main():
    win = Window(800, 600)
    #l = Line(Point(50, 100), Point(50, 200))
    #win.draw_line(l)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(125, 125, 200, 200)

    c3 = Cell(win)
    c3.has_bottom_wall = False
    c3.draw(225, 225, 250, 250)

    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(300, 300, 500, 500)
    c4.draw_move(c3, False)

    win.wait_for_close()

main()