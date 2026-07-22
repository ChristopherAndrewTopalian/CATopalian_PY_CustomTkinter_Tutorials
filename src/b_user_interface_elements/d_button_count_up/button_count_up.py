# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color (used for button highlights and borders) to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Interactive Click Counter")

# Set the starting width and height of our window in pixels (350 wide by 400 tall).
window.geometry("350x400")

# TRACKING THE NUMBER (The State Variable)

# Create a simple integer variable starting at 0 to keep track of our clicks.
count = 0

# THE UI ELEMENTS (Labels and Buttons)

# Create a title label to let the user know what this app does.
title_label = ctk.CTkLabel(
    window, text="Click Counter", font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(40, 10))

# Create a large, bold label to display our actual number on the screen.
# Notice we wrap our starting 0 in quotes ("0") because GUI labels only display text strings!
number_label = ctk.CTkLabel(
    window, text="0", font=("Segoe UI", 60, "bold"), text_color="#48FF91"
)
number_label.pack(pady=20)

# THE ACTION FUNCTION (The Logic)

# Define a simple procedural function that adds 1 to our number and updates the screen.
def count_up():
    # Use the 'global' keyword to tell Python we want to modify the 'count' variable created at the top of our script.
    global count

    # Add 1 to our current count!
    count = count + 1

    # Update our number label on screen.
    # We must wrap 'count' in str() to convert the math integer back into a text string!
    number_label.configure(text=str(count))

# THE PUSH BUTTON

# Create our interactive push button. Notice we pass command=count_up without any parentheses!
# This tells the button: "Do not run this function right now! Only run it when clicked."
up_btn = ctk.CTkButton(
    window,
    text="Count Up ➔",
    font=("Segoe UI", 18, "bold"),
    command=count_up,
)

# Place the button onto our layout
up_btn.pack(pady=30)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

