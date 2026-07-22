# Building a Dual-Button Interactive Counter

In our previous tutorial, we learned how to connect a push button to a running calculation, allowing us to build an application that counts upward every time the button is pressed. 

Today, we are going to complete our interface by giving the user **full bidirectional control**. We will add a second interactive button that allows our application to count *backwards*! 

Along the way, we will also learn a valuable User Interface (UI) design technique: how to use custom button colors to give our users immediate visual cues about what a button does before they even click it.

---

## Three Core Concepts for Today

To build our dual-button counter, we are expanding on the exact same HTML-like building blocks we used previously:

### 1. Mirroring Logic (The Down Function)
To make our application count down, we don't need to invent complex new mathematics! We simply write a second function named `count_down()` that acts as the exact mirror image of our `count_up()` function. Instead of writing `count = count + 1`, we simply change the plus sign to a minus sign: `count = count - 1`.

### 2. Stacking Elements Sequentially
In HTML, if you write two `<button>` tags one after the other in your document body, the browser stacks them neatly on the page. CustomTkinter works the exact same way! By calling `up_btn.pack()` first and `down_btn.pack()` second, the layout engine automatically stacks our Count Up button directly on top of our Count Down button.

### 3. Visual Cues with Color (`fg_color`)
When an application has multiple buttons, making them all the exact same color can confuse the user's eye. Just like styling primary and secondary buttons with CSS classes, we can pass **`fg_color`** (foreground color) and **`hover_color`** into our button setup! 

By giving our Count Down button a soft, dark-red tint (`fg_color="#A83232"`), we signal to the user's brain that this button performs a subtractive or "reverse" action!

---

## The Complete Script: `up_down_counter.py`

Create a new file named `up_down_counter.py` and type in the code below. Read through the comments starting with the `#` symbol to see how seamlessly our second function and button fit into our top-to-bottom layout!

```python
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

# --- 1. TRACKING THE NUMBER (Our State Variable) ---

# Create an integer variable starting at 0 to act as our application's memory.
count = 0

# --- 2. THE UI ELEMENTS (Labels) ---

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

# --- 3. THE ACTION FUNCTIONS (The Math Logic) ---


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


# --- 4. THE PUSH BUTTONS (Stacked from top to bottom) ---

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

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

