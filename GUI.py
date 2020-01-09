import Configuration
import tkinter as tk


class GUI:
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    rows = 8
    columns = 8
    dim_square = 64

    def __init__(self, parent):
        self.parent = parent
        # Adding Frame
        self.bottomframe = tk.Frame(parent, height=64)
        self.info_label = tk.Label(self.bottomframe,
                                text="   Les blancs commencent la partie  ",
                                fg=self.color2)
        self.info_label.pack(side=tk.RIGHT, padx=8, pady=5)
        self.bottomframe.pack(fill="x", side=tk.BOTTOM)

        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = tk.Canvas(parent, width=canvas_width,
                               height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()

    def draw_board(self):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square)
                y1 = ((7 - row) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="area")
                color = self.color1 if color == self.color2 else self.color2

def main():
    root = tk.Tk()
    root.title("Chess")
    gui = GUI(root)
    gui.draw_board()
    root.mainloop()


if __name__ == "__main__":
    main()

