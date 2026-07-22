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

# THE DISPLAY ELEMENT (Our large visual number readout)

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

# THE ACTION FUNCTIONS (Handling the two-way communication)

# Function 1: Runs continuously whenever the user DRAGS the slider
def on_slider_move(value):
    # Convert the decimal float from the slider into a clean whole integer
    whole_num = int(value)

    # Update our large green display screen
    number_display.configure(text=str(whole_num))

    # Update our text entry box so it stays perfectly in sync!
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

    # Command the physical slider handle to jump to this exact number!
    slider.set(whole_num)

    # Update our large green display screen to match
    number_display.configure(text=str(whole_num))


# THE SLIDER ELEMENT

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

# THE TEXT INPUT BOX & CONFIRM BUTTON

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

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

