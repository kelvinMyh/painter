import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.brush_size = 2
        self.color = 'black'
        
        # Set up canvas 
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)

        # Add menu
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)        
        self.file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)
        
        self.shape_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Shapes", menu=self.shape_menu)        
        self.shape_menu.add_command(label="Line", command=self.draw_line)
        self.shape_menu.add_command(label="Circle", command=self.draw_circle)
        self.shape_menu.add_command(label="Rectangle", command=self.draw_rectangle)
        self.shape_menu.add_command(label="Triangle", command=self.draw_triangle)

        # Add color menu
        self.color_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Colors", menu=self.color_menu)
        self.color_menu.add_command(label="Brush Color", command=self.pick_brush_color)
        self.color_menu.add_command(label="Fill Color", command=self.pick_fill_color)
        
        # Add bindings
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_start_pos)

        self.start_x = None
        self.start_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def pick_brush_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def pick_fill_color(self):
        fill_color = colorchooser.askcolor(color=self.color)[1]
        self.canvas.config(bg=fill_color)

    def draw_line(self):
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line_motion)

    def draw_rectangle(self):
        self.canvas.bind("<Button-1>", self.start_rectangle)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle_motion)

    def draw_circle(self):
        self.canvas.bind("<Button-1>", self.start_circle)
        self.canvas.bind("<B1-Motion>", self.draw_circle_motion)

    def draw_triangle(self):
        self.canvas.bind("<Button-1>", self.start_triangle)
        self.canvas.bind("<B1-Motion>", self.draw_triangle_motion)

    def start_line(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_line_motion(self, event):
        x = event.x
        y = event.y
        self.canvas.create_line(self.start_x, self.start_y, x, y, width=self.brush_size, fill=self.color)
        self.start_x = x
        self.start_y = y
        
    # Add other shape drawing functions
    def start_rectangle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def start_triangle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def start_circle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_rectangle_motion(self, event):
        self.canvas.delete("temp")  # 删除旧的临时形状
        x = event.x
        y = event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, x, y, width=self.brush_size, fill=self.color, tags="temp")  # 创建新的临时形状

    def draw_circle_motion(self, event):
        self.canvas.delete("temp")  # 删除旧的临时形状
        x = event.x
        y = event.y
        radius = int(((self.start_x - x)**2 + (self.start_y - y)**2) ** 0.5)  # 计算半径
        self.canvas.create_oval(self.start_x - radius, self.start_y - radius, self.start_x + radius, self.start_y + radius, width=self.brush_size, fill=self.color, tags="temp")  # 创建新的临时形状

    def draw_triangle_motion(self, event):
        self.canvas.delete("temp")  # 删除旧的临时形状
        x = event.x
        y = event.y
        self.canvas.create_polygon(self.start_x, self.start_y, self.start_x, y, x, y, width=self.brush_size, fill=self.color, tags="temp")  # 创建新的临时形状

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def reset_start_pos(self, event): 
        self.start_x, self.start_y

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    app = PaintApp(tk.Tk())
    app.run()
