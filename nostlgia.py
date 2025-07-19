import tkinter as tk
from PIL import Image, ImageTk
import random

IMAGE_FILE = "0.png" 
WIN_W, WIN_H = 400, 600
SHAPE_SPEED = 4
SQUARE_SIZE = 15 
SIDE_MARGIN = 50

SHAPES = [
    [[1, 1], [1, 1]], 
    [[1, 1, 1, 1]],  
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 0, 0], [1, 1, 1]], 
    [[0, 0, 1], [1, 1, 1]], 
    [[1, 1, 0], [0, 1, 1]], 
    [[0, 1, 1], [1, 1, 0]], 
]

root = tk.Tk()
root.title("Brick Game")
canvas = tk.Canvas(root, width=WIN_W, height=WIN_H, bg="black")
canvas.pack()

try:
    img = Image.open(IMAGE_FILE)
    photo_img = ImageTk.PhotoImage(img)
    canvas.create_image(WIN_W / 2, WIN_H / 2, image=photo_img)
except FileNotFoundError:
    canvas.create_text(WIN_W/2, WIN_H/2, text=f"'{IMAGE_FILE}' not found", fill="white")

falling_shapes = []

def create_shape():
    """Creates a new shape on one of the sides."""
    shape_pattern = random.choice(SHAPES)
    
    left_x = random.randint(0, SIDE_MARGIN)
    right_x = random.randint(WIN_W - SIDE_MARGIN - 50, WIN_W - 50)
    start_x = random.choice([left_x, right_x])
    
    new_shape = []
    for row_idx, row in enumerate(shape_pattern):
        for col_idx, cell in enumerate(row):
            if cell:
                x1 = start_x + col_idx * SQUARE_SIZE
                y1 = row_idx * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                square = canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="yellow")
                new_shape.append(square)
                
    if new_shape:
        falling_shapes.append(new_shape)
        
    root.after(1200, create_shape)

def move_shapes():
    """Moves the existing shapes down the screen."""
    for shape in list(falling_shapes):
        
        lowest_y = 0
        for square in shape:
            canvas.move(square, 0, SHAPE_SPEED)
            pos = canvas.coords(square)
            if pos and pos[3] > lowest_y:
                lowest_y = pos[3]

        if lowest_y > WIN_H:
            for square in shape:
                canvas.delete(square)
            falling_shapes.remove(shape)

    root.after(50, move_shapes)

create_shape()
move_shapes()
root.mainloop()