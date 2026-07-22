# Synchronized Sliders & Two-Way Data Binding

In our previous tutorials, we explored two powerful ways to gather numbers from a user: typing exact digits into a Text Entry Box (`CTkEntry`), and dragging a visual handle across a Slider (`CTkSlider`). 

While each tool is great on its own, professional software applications frequently use **both tools together**! When tweaking audio volume, resizing a graphics canvas, or setting a 3D simulation parameter, users love having a draggable slider for quick adjustments alongside a text box for typing exact, pinpoint measurements.

Today, we are going to build a **Synchronized Two-Way Interface**. We will link a slider and a text input box together so that dragging the slider automatically updates the text box, and typing a number into the text box automatically moves the physical slider handle across the screen!

---

## Three Core Concepts for Today

To build a synchronized interface without creating infinite feedback loops, we use three straightforward techniques:

### 1. Programmatic Text Writing (`.insert()`)
We already know that `.get()` reads text out of an entry box, and `.delete(0, "end")` wipes it clean. But how do we *write* new text into an entry box from inside our Python script?

We use the **`.insert(index, string)`** method! In Python GUIs, the number `0` represents the very first character index. Calling `entry_box.insert(0, "75")` tells our application: *"Start at position 0, and type the string '75' directly into the input box!"* This is the exact GUI equivalent of writing `element.value = "75"` in JavaScript.

### 2. Moving Sliders via Code (`slider.set()`)
Just as sliders can pass their numerical position to a function when dragged by a mouse, we can command them to move programmatically from our code! 

When a user types a number like `85` into our text box and presses our confirm button, we call **`slider.set(85)`**. This instruction instantly slides the visual track handle across the window until it rests precisely at the 85 mark!

### 3. Two-Way Data Flow (Separating the Triggers)
To keep our code linear and easy to debug, we create two distinct action functions:
* **`on_slider_move(value)`**: This fires *only* when the mouse drags the slider. It updates our large green label, wipes the entry box clean, and `.insert()`s the new slider number.
* **`on_button_click()`**: This fires *only* when the confirm button is clicked. It reads `.get()` from the entry box, converts it to an integer, updates our large green label, and calls `slider.set()` to reposition the track handle.

By separating our two triggers, our interface stays rock-solid and responsive!

---

## The Complete Script: `synced_slider_input.py`

Create a new file named `synced_slider_input.py` and type in the code below. Notice how cleanly our layout reads from top to bottom—we build our display screen at the top, drop in our draggable slider in the middle, and anchor our keyboard entry box at the bottom!

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
window.title("Synchronized Slider & Text Input")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# --- 1. THE DISPLAY ELEMENT (Our large visual number readout) ---

title_label = ctk.CTkLabel(
    window, text="Adjust value via slider or text:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(25, 15))

# Create our large number display label! We start it at "50" in vibrant green!
number_display = ctk.CTkLabel(
    window,
    text="50",
    font=("Segoe UI", 65, "bold"),
    text_color="#48FF91",
)
number_display.pack(pady=15)

# --- 2. THE ACTION FUNCTIONS (Handling the two-way communication!) ---


# Function 1: Runs continuously whenever the user DRAGS the slider
def on_slider_move(value):
    # Convert the decimal float from the slider into a clean whole integer
    whole_num = int(value)

    # 1. Update our large green display screen
    number_display.configure(text=str(whole_num))

    # 2. Update our text entry box so it stays perfectly in sync!
    # First, erase whatever text was previously sitting inside the box...
    entry_box.delete(0, "end")
    # Next, use .insert() to type our new number into the box programmatically!
    # "0" means start inserting at the very beginning of the text box.
    entry_box.insert(0, str(whole_num))


# Function 2: Runs when the user TYPES a number and clicks the "Set Value" button
def on_button_click():
    # Read the custom text string from the entry box and convert it to a float number
    typed_val = float(entry_box.get())

    # Turn it into a whole integer so it looks clean
    whole_num = int(typed_val)

    # 1. Command the physical slider handle to jump to this exact number!
    slider.set(whole_num)

    # 2. Update our large green display screen to match!
    number_display.configure(text=str(whole_num))


# --- 3. THE SLIDER ELEMENT ---

# Create our slider track from 0 to 100, connected to our on_slider_move function!
slider = ctk.CTkSlider(
    window,
    from_=0,
    to=100,
    width=250,
    height=20,
    command=on_slider_move,
)
# Position the handle at the halfway mark (50) on startup
slider.set(50)
slider.pack(pady=20)

# --- 4. THE TEXT INPUT BOX & CONFIRM BUTTON ---

# Create our text entry box where users can type exact numbers
entry_box = ctk.CTkEntry(
    window,
    font=("Segoe UI", 16),
    width=140,
    height=35,
)
# Pre-fill the box with "50" so it matches our slider's starting position!
entry_box.insert(0, "50")
entry_box.pack(pady=10)

# Create the confirm button that pushes the typed number back to the slider!
set_btn = ctk.CTkButton(
    window,
    text="Set Exact Value ➔",
    font=("Segoe UI", 16, "bold"),
    command=on_button_click,
)
set_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

