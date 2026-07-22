# Multi-Div Layouts: Row and Column Architectures

In our previous tutorial, we learned how to build a single layout container (`CTkFrame`)—the Python equivalent of an HTML `<div>`. 

While building one card is great, a real tactical dashboard or control panel requires multiple cards organized neatly across the screen. In web development, you accomplish side-by-side or stacked layouts using **CSS Flexbox** (`display: flex` with `flex-direction: row` or `column`). 

Today, we are going to build a **Multi-Sector Status Dashboard**. We will learn how to arrange multiple `<div>` cards side-by-side in a **Row**, while keeping the text elements inside each card neatly stacked in a **Column**!

---

## Three Core Concepts for Today

To build multi-column layouts without stylesheets or CSS, we use three straightforward techniques:

### 1. The Row Wrapper (`side="left"`)
By default, CustomTkinter's `.pack()` layout manager stacks elements vertically from top to bottom (acting like a column layout). 

To place two `<div>` cards side-by-side in a **Row**, we use a brilliant layout trick:
1. We create an invisible parent frame named `row_wrapper` and set its background to `fg_color="transparent"`.
2. When packing our individual divs inside that wrapper, we pass **`side="left"`** into their `.pack()` instructions! 

This tells Python: *"Stop stacking downward. Line these cards up horizontally from left to right, exactly like `display: flex; flex-direction: row;` in CSS!"*

### 2. Column Stacking Inside Cards
Once our cards are sitting side-by-side in a horizontal row, how do we arrange the text labels *inside* each card? 

We use standard, default `.pack()`! Because we did not pass `side="left"` to the labels inside `alpha_div`, Python automatically stacks the title and status text vertically from top to bottom. This gives us a **Column layout inside a Row layout**—the exact structural equivalent of nested flex containers on a web page!

### 3. Spacing with Padding (`padx`)
When placing elements side-by-side, cards can easily end up squished directly against one another. We use **`padx=15`** (horizontal padding) on our side-by-side `.pack()` calls to inject clean breathing room between our Sector Alpha and Sector Bravo containers.

---

## The Complete Script: `tactical_multi_div_layout.py`

Create a new file named `tactical_multi_div_layout.py` and type in the code below. Read through the line-by-line comments starting with the `#` symbol to see how effortlessly we can build a two-column command dashboard!

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
window.title("Tactical Multi-Div Layout (Row & Column)")

# Set the starting width and height of our window in pixels (650 wide by 450 tall).
# Notice we made it wider (650px) to comfortably fit two cards side-by-side!
window.geometry("650x450")

# --- 1. THE MAIN TITLE ---

title_label = ctk.CTkLabel(
    window, text="COMMAND CONTROL: REGIONAL SECTORS", font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(25, 20))

# --- 2. THE PARENT CONTAINER FOR ROW LAYOUT (Like a flex container with flex-direction: row) ---

# To place multiple divs side-by-side (in a row), we first create an invisible parent frame
# that acts as our row wrapper container.
row_wrapper = ctk.CTkFrame(window, fg_color="transparent")
row_wrapper.pack(pady=10)

# --- 3. DIV CARD 1: SECTOR ALPHA (Left Column) ---

# Create our first tactical <div> card
alpha_div = ctk.CTkFrame(
    row_wrapper,  # Nested inside our row wrapper!
    width=280,
    height=250,
    fg_color="#1F2937",  # Sleek dark-slate background
    border_width=2,
    border_color="#3DAEE9",  # Icy cyan border
)
# THE ROW LAYOUT TRICK: By passing side="left" into .pack(), we tell Python:
# "Do not stack this div downward! Place it to the left side of our row wrapper."
alpha_div.pack(side="left", padx=15)

# Nest elements inside Sector Alpha (Stacked in a column using default .pack())
alpha_title = ctk.CTkLabel(
    alpha_div,
    text="🛡️ SECTOR ALPHA",
    font=("Segoe UI", 16, "bold"),
    text_color="#48FF91",
)
alpha_title.pack(pady=(25, 10))

alpha_status = ctk.CTkLabel(
    alpha_div,
    text="Status: SECURE\nGround Forces: Active\nThreat Level: Low",
    font=("Segoe UI", 14),
    text_color="#A5B6C6",
)
alpha_status.pack(pady=5)

# --- 4. DIV CARD 2: SECTOR BRAVO (Right Column) ---

# Create our second tactical <div> card
bravo_div = ctk.CTkFrame(
    row_wrapper,  # Also nested inside our row wrapper!
    width=280,
    height=250,
    fg_color="#1F2937",  # Sleek dark-slate background
    border_width=2,
    border_color="#FF5733",  # High-alert warning red border
)
# Place it right next to Alpha using side="left" and add horizontal padding (padx) to separate them!
bravo_div.pack(side="left", padx=15)

# Nest elements inside Sector Bravo (Stacked in a column)
bravo_title = ctk.CTkLabel(
    bravo_div,
    text="✈️ SECTOR BRAVO",
    font=("Segoe UI", 16, "bold"),
    text_color="#FF5733",
)
bravo_title.pack(pady=(25, 10))

bravo_status = ctk.CTkLabel(
    bravo_div,
    text="Status: COMPROMISED\nAir Support: Grounded\nThreat Level: HIGH",
    font=("Segoe UI", 14),
    text_color="#A5B6C6",
)
bravo_status.pack(pady=5)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

