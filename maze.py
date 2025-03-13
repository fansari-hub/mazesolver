from cell import *

class maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows= num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._cells = []


        self._create_cells()


    def _create_cells(self):
        for r in range (0, self._num_rows):
            column_list = []
            for c in range (0, self._num_cols):
                column_list.append(Cell(self._win))
            self._cells.append(column_list)

        for i in range (0, len(self._cells)):
            for j in range (0, len(i)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass