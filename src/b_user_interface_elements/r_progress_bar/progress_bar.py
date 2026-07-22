# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Tactical Shield Energy Recharger")

# Set the starting width and height of our window in pixels (400 wide by 400 tall).
window.geometry("400x400")

# TRACKING THE PROGRESS (The State Variable)

# CustomTkinter progress bars operate on decimals from 0.0 (empty) to 1.0 (full).
# We create a tracking variable starting at 0.0 (shields completely offline).
shield_progress = 0.0

# THE DISPLAY ELEMENTS (Readout label and Progress Bar)

title_label = ctk.CTkLabel(
    window, text="Defense Grid Status:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(35, 15))

# Create our status readout label!
status_display = ctk.CTkLabel(
    window,
    text="SHIELDS: OFFLINE (0%)",
    font=("Segoe UI", 22, "bold"),
    text_color="#FF5733",  # Start with a warning red color!
)
status_display.pack(pady=10)

# Create our progress bar widget! (Like HTML <progress> element)
# We set width=280 and height=20 to make it nice and chunky on screen.
shield_bar = ctk.CTkProgressBar(
    window,
    width=280,
    height=20,
    progress_color="#3DAEE9",  # Icy cyan blue energy color!
)
# Set the bar to start completely empty at 0.0
shield_bar.set(0.0)
shield_bar.pack(pady=20)

# THE ACTION FUNCTION (Increments the progress meter)

# This function runs every time the operative presses the recharge button
def recharge_shield():
    # Use 'global' so we can modify our tracking variable outside this function
    global shield_progress

    # Check if shields are already fully charged (1.0)
    if shield_progress < 1.0:
        # Add 20% (0.2) to our current progress level
        shield_progress = shield_progress + 0.2

        # Send the decimal value straight to the progress bar!
        shield_bar.set(shield_progress)

        # Update our text readout and color based on the current charge level
        if shield_progress >= 1.0:
            status_display.configure(
                text="SHIELDS: FULLY CHARGED (100%)", text_color="#48FF91"
            )
        elif shield_progress >= 0.6:
            status_display.configure(
                text="SHIELDS: STABLE (60% - 80%)", text_color="#FFD166"
            )
        else:
            status_display.configure(
                text="SHIELDS: CHARGING...", text_color="#3DAEE9"
            )


# THE RECHARGE PUSH BUTTON

recharge_btn = ctk.CTkButton(
    window,
    text="⚡ Charge Energy Core (+20%)",
    font=("Segoe UI", 16, "bold"),
    fg_color="#2E7D32",  # Rugged tactical green
    hover_color="#1B5E20",
    command=recharge_shield,
)
recharge_btn.pack(pady=20)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

