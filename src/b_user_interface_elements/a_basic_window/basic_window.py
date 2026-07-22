# Import the CustomTkinter library and give it the short nickname 'ctk' so we don't have to type the full name every time.
import customtkinter as ctk

# Create the main application window and assign it to a simple variable named 'window'.
window = ctk.CTk()

# Set the text that appears up in the top title bar of our window.
window.title("My First App")

# Set the starting width and height of the window in pixels (400 pixels wide by 500 pixels tall).
window.geometry("400x500")

# Tell Python to start running the window in an endless loop so it stays open on the screen until the user clicks the X button to close it.
window.mainloop()

'''
The basic window will be light or dark depending on the user's system settings for light and dark mode.

If the user has light theme on their system, then the window will be light.

If the user has dark theme on their system, then the window will be dark.
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

