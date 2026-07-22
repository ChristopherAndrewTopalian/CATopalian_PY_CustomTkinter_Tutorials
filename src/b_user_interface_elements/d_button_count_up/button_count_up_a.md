# Building an Interactive Click Counter

When designing user interfaces, one of the most fundamental skills you can learn is how to connect interactive buttons to data that changes over time. 

Today, we are going to build a clean, dark-themed **Click Counter**. Whenever you press the push button, our application will do some behind-the-scenes math, add 1 to our running total, and instantly update the large number displayed on your screen!

---

## Three Core Concepts for Today

To build our counter without complicated programming architecture, we are going to use three straightforward concepts that mirror how HTML and JavaScript work together:

### 1. Tracking State (Variables)
To count up, the computer needs to remember what number it is currently on! We create a simple variable named `count = 0` at the very top of our script. This acts as our application's memory.

### 2. Connecting Functions to Buttons (`command=`)
In web development, you attach an event listener (like `onclick`) to a button so it runs a script when pressed. In CustomTkinter, we do the exact same thing using **`command=`**. 

We will write a short function named `count_up()` that handles the math, and attach it directly to our button using `command=count_up`. Notice that **we do not use parentheses** when attaching the function! This tells Python: *"Hold onto this instruction, and only execute it when the user physically clicks the button."*

### 3. Converting Numbers to Text (`str()`)
Graphical labels are designed to display **text strings**, not math equations! Once our function adds 1 to our number, we use Python's built-in **`str()`** tool to turn that math integer back into text before pushing it onto the screen.

---

## The Complete Script: `up_counter.py`

Create a new file named `up_counter.py` and type in the code below. Notice that every single line has a helpful comment starting with the `#` symbol to walk you through exactly how the application is assembled from top to bottom!

```python
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

# --- 1. TRACKING THE NUMBER (The State Variable) ---

# Create a simple integer variable starting at 0 to keep track of our clicks.
count = 0

# --- 2. THE UI ELEMENTS (Labels and Buttons) ---

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

# --- 3. THE ACTION FUNCTION (The Logic) ---


# Define a simple procedural function that adds 1 to our number and updates the screen.
def count_up():
    # Use the 'global' keyword to tell Python we want to modify the 'count' variable created at the top of our script.
    global count

    # Add 1 to our current count!
    count = count + 1

    # Update our number label on screen.
    # We must wrap 'count' in str() to convert the math integer back into a text string!
    number_label.configure(text=str(count))


# --- 4. THE PUSH BUTTON ---

# Create our interactive push button. Notice we pass command=count_up without any parentheses!
# This tells the button: "Do not run this function right now! Only run it when clicked."
up_btn = ctk.CTkButton(
    window,
    text="Count Up ➔",
    font=("Segoe UI", 18, "bold"),
    command=count_up,
)

# Place the button onto our layout!
up_btn.pack(pady=30)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

