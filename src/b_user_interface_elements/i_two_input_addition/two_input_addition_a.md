# Building a Two-Input Precision Calculator

In our previous tutorial, we learned how to read custom text from a single entry box and display it on the screen. But what happens when we want our application to read data from **multiple input fields** and perform calculations with them?

Today, we are going to build an interactive **Two-Input Precision Adder**. We will create two separate text entry boxes where you can type numeric values. When you press the calculate button, our application will grab both values, convert them into mathematical decimal numbers, add them together, and instantly project the total onto our screen!

---

## Three Core Concepts for Today

To build a calculator, we need to bridge the gap between human text strings and computer mathematics. We will use three straightforward concepts:

### 1. Managing Multiple Inputs
Just like creating two `<input>` tags in an HTML form, we can instantiate two completely separate `CTkEntry` boxes (`num1_box` and `num2_box`). Because we store them in distinct variables, we can independently read whatever the user typed into each box at any time!

### 2. The String-to-Float Bridge (`float()`)
In web development, whenever you read `element.value` from an input box, the browser gives you a **text string**—even if the user typed the number `5`. If you try to add the strings `"5"` and `"10"` together without converting them, you end up with `"510"` instead of `15`!

CustomTkinter works the exact same way. Calling `.get()` always returns a text string. To do real math, we wrap our `.get()` commands inside Python's built-in **`float()`** tool. A "float" is simply a number that allows decimals. Calling `float(num1_box.get())` is the exact GUI equivalent of writing `parseFloat(element.value)` in JavaScript!

### 3. Converting Back for Display (`str()`)
Graphical labels are designed to display text strings, not math variables! Once our function finishes adding `val1 + val2`, we wrap our final answer in **`str()`** to convert the numerical total back into text before pushing it onto our screen with `.configure(text=...)`.

---

## The Complete Script: `two_input_calculator.py`

Create a new file named `two_input_calculator.py` and type in the code below. Read through the line-by-line comments starting with the `#` symbol to see how cleanly we can wire two inputs into a single math function!

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
window.title("Two-Input Precision Adder")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# --- 1. THE INSTRUCTION & INPUT BOXES (Like two HTML <input> tags!) ---

# Create an instructional title label.
title_label = ctk.CTkLabel(
    window, text="Enter two numbers to add:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(25, 15))

# Input Box 1: The Top Number
num1_box = ctk.CTkEntry(
    window,
    placeholder_text="First number...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
num1_box.pack(pady=8)

# Input Box 2: The Bottom Number
num2_box = ctk.CTkEntry(
    window,
    placeholder_text="Second number...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
num2_box.pack(pady=8)

# --- 2. THE DISPLAY ELEMENT (Where the calculation answer will appear!) ---

# Create a large label to display the final math result.
# We start with a friendly placeholder ("---") in a vibrant green font!
result_label = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 50, "bold"),
    text_color="#48FF91",
)
result_label.pack(pady=25)

# --- 3. THE ACTION FUNCTION (Reading, Converting, and Adding) ---


# Define our function that runs when the button is clicked.
def calculate_sum():
    # 1. READ & CONVERT: Grab the text strings using .get(), and immediately
    # wrap them in float() to convert them into decimal math numbers!
    # (This is the exact equivalent of using parseFloat(element.value) in JavaScript!)
    val1 = float(num1_box.get())
    val2 = float(num2_box.get())

    # 2. CALCULATE: Add our two numbers together!
    total = val1 + val2

    # 3. DISPLAY: Convert our math total back into a string using str()
    # and push it onto our large green result label!
    result_label.configure(text=str(total))


# --- 4. THE CALCULATE BUTTON ---

# Create our push button and connect it directly to our calculate_sum function!
add_btn = ctk.CTkButton(
    window,
    text="Add Numbers ➔",
    font=("Segoe UI", 18, "bold"),
    command=calculate_sum,
)
add_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

