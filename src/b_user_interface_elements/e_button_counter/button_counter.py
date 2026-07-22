# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Dual-Button Interactive Counter")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
# Notice we made it slightly taller (450px) to give our second button plenty of breathing room!
window.geometry("350x450")

# TRACKING THE NUMBER (Our State Variable)

# Create an integer variable starting at 0 to act as our application's memory.
count = 0

# THE UI ELEMENTS (Labels)

# Create a title label to let the user know what this app does.
title_label = ctk.CTkLabel(
    window, text="Interactive Counter", font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(30, 10))

# Create our large number display. We start it at "0" in a vibrant green font!
number_label = ctk.CTkLabel(
    window, text="0", font=("Segoe UI", 65, "bold"), text_color="#48FF91"
)
number_label.pack(pady=20)

# THE ACTION FUNCTIONS (The Math Logic)

# Function 1: Adds 1 to our number
def count_up():
    global count
    count = count + 1
    number_label.configure(text=str(count))


# Function 2: Subtracts 1 from our number (The exact mirror of count_up!)
def count_down():
    global count
    count = count - 1
    number_label.configure(text=str(count))


# THE PUSH BUTTONS (Stacked from top to bottom)

# Button 1: The Up Button (Uses the default blue theme color)
up_btn = ctk.CTkButton(
    window,
    text="Count Up ➔",
    font=("Segoe UI", 18, "bold"),
    command=count_up,
)
up_btn.pack(pady=(10, 15))  # 10px padding on top, 15px on bottom

# Button 2: The Down Button
# Notice we use 'fg_color' (foreground color) and 'hover_color' to give it a soft red
# tint! This gives the user an immediate visual cue that this button subtracts.
down_btn = ctk.CTkButton(
    window,
    text="⬅ Count Down",
    font=("Segoe UI", 18, "bold"),
    fg_color="#A83232",  # Soft dark red
    hover_color="#8F2A2A",  # Slightly darker red when the mouse hovers over it
    command=count_down,
)
down_btn.pack(pady=5)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

