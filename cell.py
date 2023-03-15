from graphics import Point, Line
import time


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            linel = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(linel, "black")
        if self.has_right_wall:
            liner = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(liner, "black")
        if self.has_top_wall:
            linet = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(linet, "black")
        if self.has_bottom_wall:
            lineb = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(lineb, "black")

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            color = "red"
        else:
            color = "gray"
        line = Line(
            Point((self._x1 + self._x2)/2,(self._y1+self._y2)/2), 
            Point((to_cell._x1 + to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2))
        self._win.draw_line(line, color)