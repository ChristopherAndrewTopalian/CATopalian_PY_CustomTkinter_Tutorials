# Building a Dual-Output Geometry Calculator

In our previous tutorial, we built a calculator that took two input measurements and used them to solve a single geometric equation: the perimeter of a rectangle. 

Today, we are going to unlock the true efficiency of graphical software by updating **two independent display screens simultaneously**! 

When planning a room, building a garden bed, or designing a user interface, knowing the outside boundary (Perimeter) is only half the battle—you also need to know the total surface space inside (Area). We are going to wire our application so that a single click of our button instantly calculates both formulas and pushes the answers onto two color-coded display screens!

---

## Three Core Concepts for Today

To upgrade our single-answer tool into a dual-output calculator, we are introducing three powerful concepts:

### 1. Multiple Display Targets
In HTML, a single button click can easily run a script that updates two different `<div>` tags on different parts of your webpage. CustomTkinter works identically! By creating two separate labels (`perimeter_display` and `area_display`), we give our action function two distinct targets to update whenever the button is pressed.

### 2. The Area Formula
While Perimeter measures the outside boundary by adding all sides together, **Area** measures the total two-dimensional space inside the rectangle by multiplying the length by the width:

$$\text{Perimeter} = 2 \times (\text{length} + \text{width})$$

$$\text{Area} = \text{length} \times \text{width}$$

In Python, we simply write `area = length_val * width_val` using the asterisk (`*`) symbol for multiplication!

### 3. Clean Text Injection (Python f-strings)
Up until now, whenever we wanted to display a math number, we had to wrap it inside `str()` to convert it into text. But what if we want our label to display a nice sentence like `"Perimeter: 50.0"`?

We use a **Python f-string**! By placing the letter `f` right before our opening quote, we can inject math variables directly into our text using curly braces: **`f"Perimeter: {perimeter}"`**. 

If you have ever used JavaScript, **an f-string is the exact 1-to-1 equivalent of a JavaScript template literal (`Perimeter: ${perimeter}`)!** Python automatically converts whatever number is inside the curly braces into clean text for you.

---

## The Complete Script: `perimeter_and_area.py`

Create a new file named `perimeter_and_area.py` and type in the code below. Notice how linear and structured our layout is—we create our two inputs at the top, stack our green and blue display screens in the middle, and wire them together at the bottom!

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
window.title("Dual-Output Geometry Calculator")

# Set the starting width and height of our window in pixels (350 wide by 500 tall).
# Notice we made it taller (500px) so both of our large display labels fit comfortably!
window.geometry("350x500")

# --- 1. THE INSTRUCTION & INPUT BOXES (Length and Width) ---

title_label = ctk.CTkLabel(
    window,
    text="Enter rectangle dimensions:",
    font=("Segoe UI", 18, "bold"),
)
title_label.pack(pady=(25, 15))

# Input Box 1: The Length
length_box = ctk.CTkEntry(
    window,
    placeholder_text="Length (e.g., 15)...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
length_box.pack(pady=8)

# Input Box 2: The Width
width_box = ctk.CTkEntry(
    window,
    placeholder_text="Width (e.g., 10)...",
    font=("Segoe UI", 16),
    width=220,
    height=40,
)
width_box.pack(pady=8)

# --- 2. THE DUAL DISPLAY ELEMENTS (Two separate output targets!) ---

# Display Label 1: The Perimeter (Styled in vibrant green!)
perimeter_display = ctk.CTkLabel(
    window,
    text="Perimeter: ---",
    font=("Segoe UI", 26, "bold"),
    text_color="#48FF91",
)
perimeter_display.pack(pady=(30, 10))

# Display Label 2: The Area (Styled in cyan blue!)
area_display = ctk.CTkLabel(
    window,
    text="Area: ---",
    font=("Segoe UI", 26, "bold"),
    text_color="#3DAEE9",
)
area_display.pack(pady=(0, 25))

# --- 3. THE ACTION FUNCTION (Calculating Both Formulas at Once) ---


def calculate_geometry():
    # 1. READ & CONVERT: Grab text from both boxes and convert to decimal floats
    length_val = float(length_box.get())
    width_val = float(width_box.get())

    # 2. CALCULATE BOTH FORMULAS:
    # Perimeter = 2 * (length + width)
    perimeter = 2 * (length_val + width_val)

    # Area = length * width
    area = length_val * width_val

    # 3. UPDATE BOTH LABELS SIMULTANEOUSLY:
    # Why use f"..."? An f-string in Python works exactly like a JavaScript template
    # literal (`Perimeter: ${perimeter}`). It automatically converts the math number
    # into text and injects it right into our sentence!
    perimeter_display.configure(text=f"Perimeter: {perimeter}")
    area_display.configure(text=f"Area: {area}")


# --- 4. THE CALCULATE BUTTON ---

# Create our push button and connect it directly to our calculate_geometry function!
calc_btn = ctk.CTkButton(
    window,
    text="Calculate Both ➔",
    font=("Segoe UI", 18, "bold"),
    command=calculate_geometry,
)
calc_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

