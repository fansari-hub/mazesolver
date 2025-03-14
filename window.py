from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def clear(self):
        self.__canvas.delete("all")

    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running:
            self.redraw()
        print("Close window!")

    def close(self):
        self.__is_window_running = False

    def draw_line(self, line, fill_color="black", line_width=2):
        line.draw(self.__canvas, fill_color,line_width)
        #print("window is drawing line")
