# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Rectangle Perimeter Calculator")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# THE INSTRUCTION & INPUT BOXES (Length and Width)

# Create an instructional title label to set the context.
title_label = ctk.CTkLabel(
    window,
    text="Enter rectangle dimensions:",
    font=("Segoe UI", 18, "bold"),
)
title_label.pack(pady=(25, 15))

# Input Box 1: The Length
length_box = ctk.CTkEntry(
    window,
    placeholder_text="Length (e.g., 15)...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
length_box.pack(pady=8)

# Input Box 2: The Width
width_box = ctk.CTkEntry(
    window,
    placeholder_text="Width (e.g., 10)...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
width_box.pack(pady=8)

# THE DISPLAY ELEMENT (Where our calculated perimeter will appear)

# Create a large label to display the final measurement.
# We start with a friendly placeholder ("---") in a vibrant green font!
result_label = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 50, "bold"),
    text_color="#48FF91",
)
result_label.pack(pady=25)

# THE ACTION FUNCTION (Reading, Converting, and Calculating)

# Define our function that runs when the calculate button is clicked.
def calculate_perimeter():
    # READ & CONVERT: Grab the text strings from both boxes using .get(),
    # and immediately wrap them in float() to turn them into decimal math numbers!
    length_val = float(length_box.get())
    width_val = float(width_box.get())

    # CALCULATE: Apply the real-world perimeter formula!
    # We add the length and width together inside parentheses first, then multiply by 2.
    # Notice that Python uses the asterisk (*) symbol for multiplication!
    perimeter = 2 * (length_val + width_val)

    # DISPLAY: Convert our math total back into a string using str()
    # and project it onto our large green result label!
    result_label.configure(text=str(perimeter))


# THE CALCULATE BUTTON

# Create our push button and connect it directly to our calculate_perimeter function!
calc_btn = ctk.CTkButton(
    window,
    text="Calculate Perimeter ➔",
    font=("Segoe UI", 18, "bold"),
    command=calculate_perimeter,
)
calc_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

