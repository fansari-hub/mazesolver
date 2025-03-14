from cell import *
import time
import random
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows= num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)
        
        self._cells = []


        self._create_cells()


    def _create_cells(self):
        for r in range (0, self._num_rows):
            column_list = []
            for c in range (0, self._num_cols):
                column_list.append(Cell(self._win))
            self._cells.append(column_list)

        for i in range (0, self._num_rows):
            for j in range (0, self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1_pos = self._x1 + (self._cell_size_x * j)
        y1_pos =  self._y1 + (self._cell_size_y * i)
        x2_pos = self._x1 + (self._cell_size_x * j + self._cell_size_x )
        y2_pos =  self._y1 + (self._cell_size_y * i + self._cell_size_y)
        if self._win is not None:
            self._cells[i][j].draw(x1_pos, y1_pos, x2_pos, y2_pos)
            #self._animate()

    def _animate(self, speed=0.05):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(speed)

    def _break_entrance_and_exit(self):
        if len (self._cells) < 1:
            return
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        #print(self._cells)
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        while True:
            to_visit = []
            dead_end = True
            #print("inside loop")
            #print(f"current cell: {i}, {j}")
            if current_cell.has_left_wall == True and j>0:
                if self._cells[i][j-1].visited == False:
                    dead_end = False
                    to_visit.append((i, j-1))
            if current_cell.has_top_wall == True and i>0:
                if self._cells[i-1][j].visited == False:
                    dead_end = False
                    to_visit.append((i-1, j))
            if current_cell.has_right_wall == True and j<self._num_cols-1:
                if self._cells[i][j+1].visited == False:
                    dead_end = False
                    to_visit.append((i, j+1))
            if current_cell.has_bottom_wall == True and i<self._num_rows-1:
                if self._cells[i+1][j].visited == False:
                    dead_end = False
                    to_visit.append((i+1, j))
            #print(f"dead end? {dead_end}")
            #print(f"to visit: {to_visit}")

            if dead_end:
                self._animate(0.001)
                self._draw_cell(i, j)
                return
            else:
                random_direction = random.randint(0, len(to_visit)-1)
                #print(f"random index: {random_direction}")
                
                if to_visit[random_direction][0] == i and to_visit[random_direction][1] < j:
                    current_cell.has_left_wall = False
                elif to_visit[random_direction][0] < i and to_visit[random_direction][1] == j:
                    current_cell.has_top_wall = False
                elif to_visit[random_direction][0] == i and to_visit[random_direction][1] > j:
                    current_cell.has_right_wall = False
                elif to_visit[random_direction][0] > i and to_visit[random_direction][1] == j:
                    current_cell.has_bottom_wall = False
                
                self._break_walls_r(to_visit[random_direction][0], to_visit[random_direction][1])
            
    def _reset_cells_visited(self):
        for i in range (0, self._num_rows):
            for j in range (0, self._num_cols):
                self._cells[i][j].visited = False
        
    def solve(self):
        self._reset_cells_visited()
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        end_cell = self._cells[self._num_rows-1][self._num_cols-1]
        self._animate(0.01)
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        if current_cell == end_cell:
             return True

        if current_cell.has_left_wall == False and j>0:
            if self._cells[i][j-1].visited == False:
                next_cell = self._cells[i][j-1]
                current_cell.draw_move(next_cell)
                move_result = self.solve_r(i,j-1)
                if move_result:
                    return True
                else:
                    current_cell.draw_move(next_cell, True)
        if current_cell.has_top_wall == False and i>0:
            if self._cells[i-1][j].visited == False:
                next_cell = self._cells[i-1][j]
                current_cell.draw_move(next_cell)
                move_result = self.solve_r(i-1,j)
                if move_result:
                    return True
                else:
                    current_cell.draw_move(next_cell, True)                

        if current_cell.has_right_wall == False and j<self._num_cols-1:
            if self._cells[i][j+1].visited == False:
                next_cell = self._cells[i][j+1]
                current_cell.draw_move(next_cell)
                move_result = self.solve_r(i,j+1)
                if move_result:
                    return True
                else:
                    current_cell.draw_move(next_cell, True)                
    
        if current_cell.has_bottom_wall == False and i<self._num_rows-1:
            if self._cells[i+1][j].visited == False:
                next_cell = self._cells[i+1][j]
                current_cell.draw_move(next_cell)
                move_result = self.solve_r(i+1,j)
                if move_result:
                    return True
                else:
                    current_cell.draw_move(next_cell, True)                
        self._animate(0.01)
        return False