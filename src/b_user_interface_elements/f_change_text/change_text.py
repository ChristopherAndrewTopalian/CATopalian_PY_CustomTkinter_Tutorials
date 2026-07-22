# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Multi-Button Word Selector")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# THE DISPLAY ELEMENT (Our Target Label)

# Create a title label to welcome the user and explain what to do.
instruction_label = ctk.CTkLabel(
    window, text="Pick an animal below:", font=("Segoe UI", 20, "bold")
)
instruction_label.pack(pady=(30, 10))

# Create our large word display. We start it with a friendly placeholder string.
# We also make the font nice and large (45px) in a vibrant soft green.
word_display = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 45, "bold"),
    text_color="#48FF91",
)
word_display.pack(pady=20)

# THE ACTION FUNCTIONS (One function for each word)

# Function 1: Changes the screen text to say "DOG"
def show_dog():
    word_display.configure(text="🐶 DOG")


# Function 2: Changes the screen text to say "CAT"
def show_cat():
    word_display.configure(text="🐱 CAT")


# Function 3: Changes the screen text to say "BIRD"
def show_bird():
    word_display.configure(text="🐦 BIRD")


# THE PUSH BUTTONS (Stacked from top to bottom)

# Button 1: The Dog Button (Uses a calm ocean blue color)
dog_btn = ctk.CTkButton(
    window,
    text="Dog",
    font=("Segoe UI", 18, "bold"),
    fg_color="#2C638B",
    hover_color="#1E4663",
    command=show_dog,
)
dog_btn.pack(pady=8)

# Button 2: The Cat Button (Uses a soft forest green color)
cat_btn = ctk.CTkButton(
    window,
    text="Cat",
    font=("Segoe UI", 18, "bold"),
    fg_color="#2E7D32",
    hover_color="#1B5E20",
    command=show_cat,
)
cat_btn.pack(pady=8)

# Button 3: The Bird Button (Uses a warm amber/orange color)
bird_btn = ctk.CTkButton(
    window,
    text="Bird",
    font=("Segoe UI", 18, "bold"),
    fg_color="#D84315",
    hover_color="#BF360C",
    command=show_bird,
)
bird_btn.pack(pady=8)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

