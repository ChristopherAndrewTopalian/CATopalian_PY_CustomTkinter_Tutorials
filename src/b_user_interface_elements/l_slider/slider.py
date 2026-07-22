# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Interactive Number Slider")

# Set the starting width and height of our window in pixels (350 wide by 350 tall).
window.geometry("350x350")

# THE DISPLAY ELEMENT (Where the live slider number will appear)

# Create an instructional title label.
title_label = ctk.CTkLabel(
    window, text="Drag the slider below:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(35, 15))

# Create our large number display label! We start it at "50" (our halfway point)
# in a vibrant green font!
number_display = ctk.CTkLabel(
    window,
    text="50",
    font=("Segoe UI", 65, "bold"),
    text_color="#48FF91",
)
number_display.pack(pady=20)

# THE ACTION FUNCTION (Handles live updates as the slider moves)

# When a CustomTkinter slider moves, it automatically passes its current numerical
# position into our function! We capture that number in the variable named 'value'.
def update_display(value):
    # Sliders move in tiny decimal fractions (like 50.4382).
    # To keep our screen display clean and easy to read, we wrap 'value' inside
    # int() to chop off the decimals and turn it into a whole integer number!
    whole_number = int(value)

    # Convert the integer into a text string and push it onto our large green label!
    number_display.configure(text=str(whole_number))


# THE SLIDER ELEMENT (Like HTML <input type="range">)

# Create our interactive slider track!
# Notice we use 'from_=0' with an underscore! In Python, the plain word 'from' is reserved
# for importing libraries (like 'from random import...'), so we add the underscore!
slider = ctk.CTkSlider(
    window,
    from_=0,
    to=100,
    width=250,
    height=20,
    command=update_display,
)

# Set the slider handle to start right in the middle at 50!
slider.set(50)

# Place the slider onto our window layout!
slider.pack(pady=25)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

