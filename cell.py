from line import *
from point import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        #print(f"{self._x1}, {self._x2}, {self._y1}, {self._y2}")

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center(), to_cell.get_center())
        if undo == False:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")

    def get_center(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return (Point(center_x, center_y))