# Our First Dark-Theme Window

Now that CustomTkinter is installed on your computer, it is time to build our very first window!

When learning a new tool, the most important step is simply getting a blank canvas on the screen. Today, we are going to create a 400x500 pixel window. Because we want this interface to be comfortable for all-day use, we will apply a **dark appearance mode** right on line 2 so our screen never flashes bright white.

## The Script: `dark_window.py`

Create a new file named `dark_window.py` and type in the code below. Notice that **every single line has a comment** starting with the `#` symbol. Python ignores anything after a `#`, so we use it to explain exactly what each line is doing in plain English!

---

### Code Walkthrough

```python
# Import the CustomTkinter library and give it the short nickname 'ctk' so we don't have to type the full name every time.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme for all windows and elements to protect our eyes from bright screens.
ctk.set_appearance_mode("dark")

# Set the default color accent (used for buttons and borders later) to a nice, clean shade of blue.
ctk.set_default_color_theme("blue")

# Create the main application window and assign it to a simple variable named 'window'.
window = ctk.CTk()

# Set the text that appears up in the top title bar of our window.
window.title("My First Dark Theme App")

# Set the starting width and height of the window in pixels (400 pixels wide by 500 pixels tall).
window.geometry("400x500")

# Tell Python to start running the window in an endless loop so it stays open on the screen until the user clicks the X button to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

