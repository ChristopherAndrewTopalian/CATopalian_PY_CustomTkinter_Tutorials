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

# LOADING THE IMAGE DATA

# IMPORTANT: You must have a real image file named "true_ai.webp" saved in the 
# exact same folder as this Python script! 
# We use Image.open() to load the raw file data from our computer into memory.
raw_image_data = Image.open("true_ai.webp")

# CONVERTING TO A CUSTOMTKINTER IMAGE

# Graphical windows cannot read raw image data directly. We must wrap our raw data 
# inside a 'CTkImage'. We also tell it exactly how large to draw the image (600x400)
# so it matches our window dimensions perfectly!
bg_texture = ctk.CTkImage(
    light_image=raw_image_data, 
    dark_image=raw_image_data, 
    size=(600, 400)
)

# THE BACKGROUND LAYER TRICK (.place)

# To create a background, we create a standard CTkLabel, but we leave the text blank!
# Instead, we pass our converted image into the 'image=' property.
background_label = ctk.CTkLabel(window, text="", image=bg_texture)

# THE LAYOUT MAGIC: Instead of using .pack(), we use .place(x=0, y=0)!
# .pack() stacks elements, but .place() pins elements to exact pixel coordinates.
# By pinning this image exactly at the top-left corner (0,0) before we add anything else, 
# it becomes the bottom layer of our application!
background_label.place(x=0, y=0)

# ADDING UI ELEMENTS ON TOP

# Because our background was "placed" first, anything we ".pack()" now will 
# naturally float on top of the background texture!

title_label = ctk.CTkLabel(
    window, 
    text="TRUE AI", 
    font=("Segoe UI", 28, "bold"), 
    text_color="#00F7FB",
    fg_color="#1F2937", # We give the text a dark slate background so it's easy to read
    corner_radius=8     # We round the corners of the text background for a sleek look
)
title_label.pack(pady=(150, 10)) # Push the text down to the center of the screen

subtitle = ctk.CTkLabel(
    window,
    text="Christopher Andrew Topalian",
    font=("Segoe UI", 16),
    text_color="#48FF91",
    fg_color="#1F2937",
    corner_radius=8
)
subtitle.pack(pady=5)

# Turn on the window and keep it running in an endless loop!
window.mainloop()