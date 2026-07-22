# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Passing Parameters with Lambda")

# Set the starting width and height of our window in pixels (350 wide by 450 tall).
window.geometry("350x450")

# THE DISPLAY ELEMENT (Our Target Label)

# Create an instructional label to welcome the user.
instruction_label = ctk.CTkLabel(
    window, text="Pick an animal below:", font=("Segoe UI", 20, "bold")
)
instruction_label.pack(pady=(30, 10))

# Create our large word display! We start it with a friendly placeholder string.
word_display = ctk.CTkLabel(
    window,
    text="---",
    font=("Segoe UI", 45, "bold"),
    text_color="#FFFFFF",
)
word_display.pack(pady=20)

# THE DYNAMIC HELPER FUNCTION (One function replaces three)

# Instead of writing separate functions for dog, cat, and bird, we write ONE function
# that accepts two parameters: the text string to show, and the color to change it to!
def update_display(animal_word, color_hex):
    # We update both the text AND the text_color property at the same time!
    word_display.configure(text=animal_word, text_color=color_hex)


# THE PUSH BUTTONS (Using Lambda to Pass Parameters)

# Button 1: The Dog Button
# WHY WE USE LAMBDA: If we just wrote command=update_display("🐶 DOG", "#3DAEE9"),
# Python would run the math instantly when the app opens!
# Adding 'lambda:' acts like a JavaScript arrow function (() => ...), pausing execution
# until the user physically clicks the button!
dog_btn = ctk.CTkButton(
    window,
    text="Dog (Blue)",
    font=("Segoe UI", 18, "bold"),
    fg_color="#2C638B",
    hover_color="#1E4663",
    command=lambda: update_display("🐶 DOG", "#3DAEE9"),
)
dog_btn.pack(pady=8)

# Button 2: The Cat Button (Passes "CAT" and a bright green hex color!)
cat_btn = ctk.CTkButton(
    window,
    text="Cat (Green)",
    font=("Segoe UI", 18, "bold"),
    fg_color="#2E7D32",
    hover_color="#1B5E20",
    command=lambda: update_display("🐱 CAT", "#48FF91"),
)
cat_btn.pack(pady=8)

# Button 3: The Bird Button (Passes "BIRD" and a vibrant orange hex color!)
bird_btn = ctk.CTkButton(
    window,
    text="Bird (Orange)",
    font=("Segoe UI", 18, "bold"),
    fg_color="#D84315",
    hover_color="#BF360C",
    command=lambda: update_display("🐦 BIRD", "#FF9F1C"),
)
bird_btn.pack(pady=8)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

