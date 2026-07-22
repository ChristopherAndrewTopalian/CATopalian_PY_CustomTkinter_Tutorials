# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Two-Input Precision Adder")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# THE INSTRUCTION & INPUT BOXES (Like two HTML <input> tags)

# Create an instructional title label.
title_label = ctk.CTkLabel(
    window, text="Enter two numbers to add:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(25, 15))

# Input Box 1: The Top Number
num1_box = ctk.CTkEntry(
    window,
    placeholder_text="First number...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
num1_box.pack(pady=8)

# Input Box 2: The Bottom Number
num2_box = ctk.CTkEntry(
    window,
    placeholder_text="Second number...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
num2_box.pack(pady=8)

# THE DISPLAY ELEMENT (Where the calculation answer will appear)

# Create a large label to display the final math result.
# We start with a friendly placeholder ("---") in a vibrant green font!
result_label = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 50, "bold"),
    text_color="#48FF91",
)
result_label.pack(pady=25)

# THE ACTION FUNCTION (Reading, Converting, and Adding)

# Define our function that runs when the button is clicked.
def calculate_sum():
    # READ & CONVERT: Grab the text strings using .get(), and immediately
    # wrap them in float() to convert them into decimal math numbers!
    # (This is the exact equivalent of using parseFloat(element.value) in JavaScript!)
    val1 = float(num1_box.get())
    val2 = float(num2_box.get())

    # CALCULATE: Add our two numbers together!
    total = val1 + val2

    # DISPLAY: Convert our math total back into a string using str()
    # and push it onto our large green result label!
    result_label.configure(text=str(total))


# THE CALCULATE BUTTON

# Create our push button and connect it directly to our calculate_sum function!
add_btn = ctk.CTkButton(
    window,
    text="Add Numbers ➔",
    font=("Segoe UI", 18, "bold"),
    command=calculate_sum,
)
add_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

