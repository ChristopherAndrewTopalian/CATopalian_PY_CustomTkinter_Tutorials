# Building a Multi-Button Word Selector

In our previous tutorials, we explored how buttons can trigger mathematical calculations like counting upward and downward. But what if we want our application to display different descriptive text messages depending on which button the user clicks?

Today, we are going to build a **Multi-Button Word Selector**. We will create three separate interactive push buttons—one for **Dog**, one for **Cat**, and one for **Bird**. Whenever you click one of the buttons, our application will instantly update our main display screen with your chosen animal!

---

## Three Core Concepts for Today

By removing math from the equation, we can focus entirely on how multiple UI components talk to each other using simple HTML-style logic:

### 1. Multiple Triggers, One Target
In web development, you might have three different navigation links that all change the text inside a single main content box (`<div>`). CustomTkinter works exactly the same way! We can create three completely independent buttons, and point all of their `command=` instructions toward the exact same display label (`word_display`).

### 2. Dedicated Functions for Clarity
When beginners start building interfaces with multiple buttons, the cleanest way to avoid confusion is to write a short, dedicated function for each action! We will create three 2-line functions:
* `show_dog()`
* `show_cat()`
* `show_bird()`

Because we are only changing a text string, we don't even need the `global` keyword! We just call `word_display.configure(text=...)` directly inside each function.

### 3. Color-Coding for Visual Identity
To make our application feel polished and fun to use, we can give each button its own unique visual personality! Using **`fg_color`** (foreground color) and **`hover_color`**, we will give the Dog button a calming ocean blue, the Cat button a natural forest green, and the Bird button a vibrant sunset orange.

---

## The Complete Script: `word_selector.py`

Create a new file named `word_selector.py` and type in the code below. Notice how clean and linear the script reads from top to bottom—we define our display screen first, write our three action rules second, and pack our three styled buttons onto the layout last!

```python
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

# --- 1. THE DISPLAY ELEMENT (Our Target Label) ---

# Create a title label to welcome the user and explain what to do.
instruction_label = ctk.CTkLabel(
    window, text="Pick an animal below:", font=("Segoe UI", 20, "bold")
)
instruction_label.pack(pady=(30, 10))

# Create our large word display! We start it with a friendly placeholder string.
# We also make the font nice and large (45px) in a vibrant soft green.
word_display = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 45, "bold"),
    text_color="#48FF91",
)
word_display.pack(pady=20)

# --- 2. THE ACTION FUNCTIONS (One function for each word!) ---


# Function 1: Changes the screen text to say "DOG"
def show_dog():
    word_display.configure(text="🐶 DOG")


# Function 2: Changes the screen text to say "CAT"
def show_cat():
    word_display.configure(text="🐱 CAT")


# Function 3: Changes the screen text to say "BIRD"
def show_bird():
    word_display.configure(text="🐦 BIRD")


# --- 3. THE PUSH BUTTONS (Stacked from top to bottom) ---

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

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

