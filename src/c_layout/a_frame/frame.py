# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Tactical Div Container (CTkFrame)")

# Set the starting width and height of our window in pixels (400 wide by 400 tall).
window.geometry("400x400")

# THE INSTRUCTION LABEL

title_label = ctk.CTkLabel(
    window, text="Main Window Container", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(25, 15))

# CREATING A DIV CONTAINER (Like an HTML <div> tag)

# In CustomTkinter, a layout container is called a 'CTkFrame'.
# This is the exact 1-to-1 equivalent of creating a <div> element in HTML!
# We set a distinct background color (fg_color) and add a border so we can see its edges.
tactical_div = ctk.CTkFrame(
    window,
    width=320,
    height=200,
    fg_color="#1F2937",  # A sleek dark-slate background color (like a CSS background)
    border_width=2,  # A clean structural border width
    border_color="#3DAEE9",  # Icy cyan border color
)

# Place our <div> container onto the main window layout using .pack()
tactical_div.pack(pady=10)

# PUTTING ELEMENTS *INSIDE* OUR DIV

# In HTML, you nest text or buttons inside a <div> by placing them between the open/close tags.
# In CustomTkinter, we nest elements inside a frame by passing the frame's variable name
# as the very first argument when creating the element.

div_title = ctk.CTkLabel(
    tactical_div,  # Notice we pass 'tactical_div' here instead of 'window'!
    text="⚠️ CLASSIFIED SECTOR",
    font=("Segoe UI", 16, "bold"),
    text_color="#FFD166",
)
div_title.pack(pady=(15, 15))

div_text = ctk.CTkLabel(
    tactical_div,  # Nested inside our div container!
    text="This content is safely contained\ninside our custom frame (div).",
    font=("Segoe UI", 20),
    text_color="#A5B6C6",
)
div_text.pack(pady=5, padx=15)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

