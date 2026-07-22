# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Mutually Exclusive Radio Buttons")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# THE SHARED CONTROL VARIABLE (The secret to grouping radio buttons)

# In HTML, radio buttons group together by sharing the same name="group" attribute.
# In CustomTkinter, they group together by sharing a single 'StringVar' variable!
# We create our shared variable and pre-select "Easy" as our starting default value.
difficulty_var = ctk.StringVar(value="Easy")

# THE DISPLAY ELEMENT (Our large status readout)

title_label = ctk.CTkLabel(
    window, text="Select Game Difficulty:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(35, 15))

# Create our large display label! We start it matching our "Easy" default value
# with a calming green font color.
status_display = ctk.CTkLabel(
    window,
    text="🟢 EASY",
    font=("Segoe UI", 45, "bold"),
    text_color="#48FF91",
)
status_display.pack(pady=25)

# THE ACTION FUNCTION (Checks which radio button was selected)

# This function runs instantly whenever ANY of our radio buttons are clicked!
def update_difficulty():
    # Calling .get() on our shared variable tells us the exact 'value' string
    # of whichever radio button is currently selected
    choice = difficulty_var.get()

    # Use if/elif/else to update the screen text and color based on the choice!
    if choice == "Easy":
        status_display.configure(text="🟢 EASY", text_color="#48FF91")
    elif choice == "Medium":
        status_display.configure(text="🟡 MEDIUM", text_color="#FFD166")
    else:
        status_display.configure(text="🔴 HARD", text_color="#FF5733")


# THE RADIO BUTTON ELEMENTS (Like HTML <input type="radio">)

# Button 1: Easy
# Notice we connect it to our shared 'difficulty_var' and give it value="Easy".
easy_radio = ctk.CTkRadioButton(
    window,
    text="Easy Mode",
    font=("Segoe UI", 16),
    variable=difficulty_var,  # Links to our shared group!
    value="Easy",  # The specific string saved when this button is clicked
    command=update_difficulty,  # Runs our update function
)
easy_radio.pack(pady=10)

# Button 2: Medium
# Connects to the exact same 'difficulty_var', but holds value="Medium"!
medium_radio = ctk.CTkRadioButton(
    window,
    text="Medium Mode",
    font=("Segoe UI", 16),
    variable=difficulty_var,
    value="Medium",
    command=update_difficulty,
)
medium_radio.pack(pady=10)

# Button 3: Hard
# Connects to the exact same 'difficulty_var', but holds value="Hard"!
hard_radio = ctk.CTkRadioButton(
    window,
    text="Hard Mode",
    font=("Segoe UI", 16),
    variable=difficulty_var,
    value="Hard",
    command=update_difficulty,
)
hard_radio.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

