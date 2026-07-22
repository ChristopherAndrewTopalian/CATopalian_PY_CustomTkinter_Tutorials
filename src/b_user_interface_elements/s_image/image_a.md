# Adding Background Textures and Images

In our previous tutorials, our applications have relied on solid background colors. But if you want to build a truly immersive tactical dashboard, a video game interface, or a polished desktop tool, you need to know how to load external image files!

In web development, adding a background image is handled by CSS (`background-image: url(...)`). CustomTkinter handles images a bit differently. Today, we are going to learn how to load a tactical metal texture from our computer and pin it to the very back of our window using a brand new layout manager: **`.place()`**.

---

## Three Core Concepts for Today

To put an image on our screen, we must process the file, convert it, and pin it to the background. 

### 1. The Pillow Library (`PIL`)
CustomTkinter is fantastic at building buttons and sliders, but it needs help opening raw image files (like `.jpg` or `.png`). For this, we use Python's industry-standard image processing library: **Pillow** (imported as `PIL`). 
We use `Image.open("filename.jpg")` to locate the file on our hard drive and pull it into our application's memory.

*(Note: If you have not installed Pillow yet, simply run `pip install Pillow` in your terminal!)*

### 2. The `CTkImage` Wrapper
Once we have our raw image data, we cannot just shove it onto the screen. We have to wrap it in a **`CTkImage`**. This acts like a translator, converting the raw picture into graphical pixels that CustomTkinter understands. We also use this step to define the exact `size=(width, height)` we want the image to be drawn!

### 3. The `.place()` Background Trick
How do we make an image act like a background instead of a normal button or label? 
1. We create a `CTkLabel` and pass our image into it, leaving the text completely blank (`text=""`).
2. We skip `.pack()` entirely! Instead, we use **`.place(x=0, y=0)`**. 

While `.pack()` stacks elements sequentially, `.place()` pins an element to exact pixel coordinates. By pinning our image label to the absolute top-left corner (`0, 0`) immediately after creating our window, it becomes the bottom layer of our canvas. Anything we `.pack()` afterward will beautifully float on top of it!

---

## The Complete Script: `window_background.py`

Before running this script, **you must save a picture to your folder!** Find a cool metal texture, a tactical map, or a sci-fi background on the internet, save it inside the exact same folder as your Python script, and rename it to `tactical_metal.jpg`.

Once your image is ready, create a new file named `window_background.py` and type in the code below!

```python
# Import CustomTkinter, and import the 'Image' tool from the Pillow (PIL) library!
import customtkinter as ctk
from PIL import Image

# Set up our standard dark theme and blue accent color.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create our main application window.
window = ctk.CTk()
window.title("Tactical Background Texture")

# Set the window size to exactly 600px wide by 400px tall.
# We also use .resizable(False, False) to lock the window size, ensuring our 
# background image perfectly fits the screen without stretching or breaking!
window.geometry("600x400")
window.resizable(False, False)

# --- 1. LOADING THE IMAGE DATA ---

# IMPORTANT: You must have a real image file named "tactical_metal.jpg" saved in the 
# exact same folder as this Python script! 
# We use Image.open() to load the raw file data from our computer into memory.
raw_image_data = Image.open("tactical_metal.jpg")

# --- 2. CONVERTING TO A CUSTOMTKINTER IMAGE ---

# Graphical windows cannot read raw image data directly. We must wrap our raw data 
# inside a 'CTkImage'. We also tell it exactly how large to draw the image (600x400)
# so it matches our window dimensions perfectly!
bg_texture = ctk.CTkImage(
    light_image=raw_image_data, 
    dark_image=raw_image_data, 
    size=(600, 400)
)

# --- 3. THE BACKGROUND LAYER TRICK (.place) ---

# To create a background, we create a standard CTkLabel, but we leave the text blank!
# Instead, we pass our converted image into the 'image=' property.
background_label = ctk.CTkLabel(window, text="", image=bg_texture)

# THE LAYOUT MAGIC: Instead of using .pack(), we use .place(x=0, y=0)!
# .pack() stacks elements, but .place() pins elements to exact pixel coordinates.
# By pinning this image exactly at the top-left corner (0,0) before we add anything else, 
# it becomes the bottom layer of our application!
background_label.place(x=0, y=0)

# --- 4. ADDING UI ELEMENTS ON TOP ---

# Because our background was "placed" first, anything we ".pack()" now will 
# naturally float on top of the background texture!

title_label = ctk.CTkLabel(
    window, 
    text="SYSTEM OVERRIDE INITIATED", 
    font=("Segoe UI", 28, "bold"), 
    text_color="#FF5733",
    fg_color="#1F2937", # We give the text a dark slate background so it's easy to read
    corner_radius=8     # We round the corners of the text background for a sleek look
)
title_label.pack(pady=(150, 10)) # Push the text down to the center of the screen

subtitle = ctk.CTkLabel(
    window,
    text="Bypassing mainframe security protocols...",
    font=("Segoe UI", 16),
    text_color="#48FF91",
    fg_color="#1F2937",
    corner_radius=8
)
subtitle.pack(pady=5)

# Turn on the window and keep it running in an endless loop!
window.mainloop()