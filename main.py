from window import *
from maze import *

NUM_ROWS = 30
NUM_COLS = 30
MARGIN = 50
SCREEN_X = 1024
SCREEN_Y = 1024
CELL_SIZE_X = (SCREEN_X - 2 * MARGIN) / NUM_COLS
CELL_SIZE_Y = (SCREEN_Y - 2 * MARGIN) / NUM_ROWS


def main():
    win = Window(SCREEN_X, SCREEN_Y)
    maze = Maze(MARGIN, MARGIN, NUM_ROWS, NUM_COLS, CELL_SIZE_X, CELL_SIZE_Y, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze.solve()
    win.wait_for_close()

main()