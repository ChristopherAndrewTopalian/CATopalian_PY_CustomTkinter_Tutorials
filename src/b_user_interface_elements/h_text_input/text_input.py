# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Interactive Text Input")

# Set the starting width and height of our window in pixels (350 wide by 400 tall).
window.geometry("350x400")

# THE INSTRUCTION & INPUT BOX (Like HTML <input type="text">)

# Create an instructional label to tell the user what to do.
title_label = ctk.CTkLabel(
    window, text="Type a message below:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(30, 10))

# Create a single-line text entry box!
# We use 'placeholder_text' to show gray hint text that disappears when they start typing.
# We also set width=250 so the box is nice and wide on the screen.
entry_box = ctk.CTkEntry(
    window,
    placeholder_text="Type something here...",
    font=("Segoe UI", 16),
    width=250,
    height=40,
)
entry_box.pack(pady=10)

# THE DISPLAY ELEMENT (Where the typed text will appear)

# Create a large label to display the user's custom text.
# We start with a friendly placeholder line ("---") in a vibrant green font!
output_label = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 28, "bold"),
    text_color="#48FF91",
    wraplength=300,  # This ensures long sentences wrap to a new line instead of running off the screen!
)
output_label.pack(pady=30)

# THE ACTION FUNCTION (Reading and displaying the data)

# Define our function that runs when the confirm button is clicked.
def display_message():
    # READ: Use .get() to grab whatever text string the user typed into the box
    # (This is the exact equivalent of reading element.value in JavaScript!)
    typed_text = entry_box.get()

    # UPDATE: Push that text onto our large green output label
    output_label.configure(text=typed_text)

    # CLEAR: Wipe the entry box clean so it is ready for the user's next message!
    # "0" means start at the very first character, and "end" means delete all the way to the end.
    entry_box.delete(0, "end")


# THE CONFIRM BUTTON

# Create our push button and connect it to our display_message function!
confirm_btn = ctk.CTkButton(
    window,
    text="Confirm Message ➔",
    font=("Segoe UI", 16, "bold"),
    command=display_message,
)
confirm_btn.pack(pady=10)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

