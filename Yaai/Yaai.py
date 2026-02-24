import tkinter as tk
from PIL import Image, ImageTk

# --- Setup ---
root = tk.Tk()
root.overrideredirect(True) # Borderless
width, height = 200, 200
root.geometry(f'{width}x{height}+100+100')

# --- Load Image ---
# Replace 'image.png' with your file
try:
    img = ImageTk.PhotoImage(Image.open("resources/YAAIicon.png").resize((200, 200)))
    label = tk.Label(root, image=img)
    label.pack()
except:
    label = tk.Label(root, text="Image Not Found", bg="red")
    label.pack(expand=True, fill='both')

# --- Animation Setup ---
x, y = 100, 100
dx, dy = 5, 5 # Velocity
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def bounce():
    global x, y, dx, dy
    x += dx
    y += dy

    # Boundary Check (Reverse velocity if hits edge)
    if x <= 0 or x + width >= screen_width:
        dx = -dx
    if y <= 0 or y + height >= screen_height:
        dy = -dy

    root.geometry(f'{width}x{height}+{x}+{y}')
    root.after(20, bounce) # Run every 20ms

# Start
bounce()
root.mainloop()
