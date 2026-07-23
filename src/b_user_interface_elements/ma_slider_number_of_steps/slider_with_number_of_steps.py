# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Precision Decimal Slider & Resizer")

# Set the starting width and height of our window in pixels (450 wide by 400 tall).
window.geometry("450x400")

# THE DISPLAY LABELS

title_label = ctk.CTkLabel(
    window,
    text="FORCEFIELD WIDTH CALIBRATION",
    font=("Segoe UI", 18, "bold"),
)
title_label.pack(pady=(25, 10))

# Create our readout label! We start it at "1.0x" in vibrant cyan blue!
readout_label = ctk.CTkLabel(
    window,
    text="Scale Factor: 1.0x",
    font=("Segoe UI", 28, "bold"),
    text_color="#3DAEE9",
)
readout_label.pack(pady=10)

# THE RESIZABLE DIV CONTAINER (Our visual target)

# We create a CTkFrame (div) that represents our tactical shield.
# We give it a starting width of 50px and an icy blue background!
shield_div = ctk.CTkFrame(
    window,
    width=50,
    height=40,
    fg_color="#3DAEE9",
    corner_radius=6,
)
# We place it onto our window layout!
shield_div.pack(pady=20)

# THE ACTION FUNCTION (Handles decimal formatting and resizing)

def on_slider_change(value):
    # FORMAT THE DECIMAL:
    # This is Python's exact equivalent of JavaScript's value.toFixed(1)!
    # It takes a messy number like 4.3000000001 and turns it into clean text: "4.3"
    clean_decimal = f"{value:.1f}"

    # UPDATE THE SCREEN TEXT:
    readout_label.configure(text=f"Scale Factor: {clean_decimal}x")

    # RESIZE OUR DIV CONTAINER IN REAL-TIME:
    # We multiply our slider value by 35 pixels so it grows visibly across the screen.
    # Because pixel measurements must be whole numbers, we wrap the math in int().
    new_pixel_width = int(value * 35)

    # We use .configure() to dynamically change the width of our div container!
    shield_div.configure(width=new_pixel_width)


# THE 0.1 INCREMENT SLIDER

# To get 0.1 steps between from_=1 and to=10, we calculate:
# (10 - 1) / 0.1 = 90 total notches!
# Setting number_of_steps=90 forces the handle to snap cleanly to 0.1 decimals!
precision_slider = ctk.CTkSlider(
    window,
    from_=1,
    to=10,
    number_of_steps=90,  # 90 notches = 0.1 increments!
    width=280,
    height=20,
    command=on_slider_change,
)

# Start the slider handle at position 1.0
precision_slider.set(1)
precision_slider.pack(pady=20)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

