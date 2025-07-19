import tkinter as tk
from PIL import Image, ImageTk
import random

# --- Configuration ---
IMAGE_FILE = "0.png"  # The name of your image file
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BRICK_SPEED = 5
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
SIDE_MARGIN = 50

# --- Setup the main window ---
root = tk.Tk()
root.title("Brick Game")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
canvas.pack()

# --- Load and display the central image ---
try:
    img = Image.open(IMAGE_FILE)
    photo_img = ImageTk.PhotoImage(img)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, image=photo_img)
except FileNotFoundError:
    canvas.create_text(
        WINDOW_WIDTH / 2,
        WINDOW_HEIGHT / 2,
        text="Image '0.PHG' not found",
        fill="white",
    )

# --- Brick Animation ---
bricks = []


def create_brick():
    """Creates a new brick at a random position on the sides."""
    x_pos = random.choice([random.randint(0, SIDE_MARGIN), random.randint(WINDOW_WIDTH - SIDE_MARGIN - BRICK_WIDTH, WINDOW_WIDTH - BRICK_WIDTH)])
    brick = canvas.create_rectangle(
        x_pos, 0, x_pos + BRICK_WIDTH, BRICK_HEIGHT, fill="white"
    )
    bricks.append(brick)
    root.after(1000, create_brick)  # Create a new brick every second


def move_bricks():
    """Moves the existing bricks down the screen."""
    for brick in bricks:
        canvas.move(brick, 0, BRICK_SPEED)
        if canvas.coords(brick)[1] > WINDOW_HEIGHT:
            canvas.delete(brick)
            bricks.remove(brick)
    root.after(50, move_bricks)


# --- Start the animation ---
create_brick()
move_bricks()

root.mainloop()