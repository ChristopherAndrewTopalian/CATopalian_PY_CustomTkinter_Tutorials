# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Interactive Toggle Switch")

# Set the starting width and height of our window in pixels (350 wide by 350 tall).
window.geometry("350x350")

# THE DISPLAY ELEMENT (Our large status readout)

title_label = ctk.CTkLabel(
    window, text="System Power Control:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(35, 15))

# Create our large status display! We start it in STANDBY mode (OFF)
# with a muted, calming gray font color.
status_display = ctk.CTkLabel(
    window,
    text="💤 STANDBY",
    font=("Segoe UI", 40, "bold"),
    text_color="#A5B6C6",
)
status_display.pack(pady=25)

# THE ACTION FUNCTION (Using If/Else Conditional Logic)

# When a CustomTkinter switch is flipped, this function checks its state.
def toggle_power():
    # Calling .get() on a switch returns a binary number:
    # 1 means ON (checked), and 0 means OFF (unchecked).
    current_state = power_switch.get()

    # THE IF/ELSE BLOCK (Just like an if/else statement in JavaScript!):
    # If the switch state is equal to 1 (ON)...
    if current_state == 1:
        # Change the text to ONLINE and turn the font vibrant green!
        status_display.configure(text="⚡ ONLINE", text_color="#48FF91")
    # Otherwise (if the switch state is 0 / OFF)...
    else:
        # Change the text back to STANDBY and turn the font muted gray!
        status_display.configure(text="💤 STANDBY", text_color="#A5B6C6")


# THE TOGGLE SWITCH ELEMENT (Like HTML <input type="checkbox">)

# Create our modern sliding toggle switch!
# We give it a label ("Toggle Power"), make the font bold, and connect it directly
# to our toggle_power function so it runs instantly whenever flipped.
power_switch = ctk.CTkSwitch(
    window,
    text="Toggle System Power",
    font=("Segoe UI", 16, "bold"),
    command=toggle_power,
)

# By default, switches start in the OFF (0) position.
# We place it onto our layout with some comfortable breathing room!
power_switch.pack(pady=25)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

