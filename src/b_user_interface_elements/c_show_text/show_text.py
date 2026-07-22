# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from glare.
ctk.set_appearance_mode("dark")

# Set the default accent color (used for borders and highlights) to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Showing Text")

# Set the starting width and height of our window in pixels (400 wide by 300 tall).
window.geometry("400x300")

# ADDING TEXT (Just like creating an <h1> tag in HTML)

# Create a text label attached to our 'window' displaying the words "Hi everyone!".
# We also set a clean font ('Segoe UI'), make it 24 pixels tall, and bold it so it reads clearly.
greeting_label = ctk.CTkLabel(window, text="Hi everyone!", font=("Segoe UI", 50, "bold"))

# Place the label onto the window layout using .pack() (like appending to document body).
# Notice we add 50 pixels of vertical padding (pady=50) so it sits nicely near the center!
greeting_label.pack(pady=50)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

