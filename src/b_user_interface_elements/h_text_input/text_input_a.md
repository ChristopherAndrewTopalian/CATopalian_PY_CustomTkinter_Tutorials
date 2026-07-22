# Interactive Text Input & Keyboard Entry

In our previous tutorials, we explored how buttons can trigger pre-programmed text strings and colors. But what if we want to give the user the power to type their very own custom words, names, or sentences into our application?

Today, we are going to build an interactive **Message Confirmer**. We will create a clean text input box where you can type anything you want using your keyboard. When you press the confirm button, our application will grab your custom text, wipe the input box clean, and proudly display your message on the main screen!

---

## Three Core Concepts for Today

To capture keyboard input, we are adding a crucial new UI component that works just like an HTML form field:

### 1. The Text Entry Box (`CTkEntry`)
In graphical programming, a single-line text input field is called an **Entry Box**. This is the direct equivalent of an HTML `<input type="text">` tag. When we create a `CTkEntry`, we can customize its width, height, and even provide **`placeholder_text="..."`** to display helpful gray hint text that vanishes the moment the user starts typing!

### 2. Reading the Data (`.get()`)
Once the user types a message into the box and clicks our button, how does Python read what they wrote? We use the **`.get()`** method! 

Calling `entry_box.get()` is the exact GUI equivalent of writing `element.value` in JavaScript. It reaches inside the input box, copies the text string sitting inside it, and saves it into a variable so we can use it!

### 3. Resetting the Field (`.delete()`)
From a User Experience (UX) standpoint, if a user types a message and clicks confirm, they expect the text box to clear itself out so they can immediately type a second message. 

We accomplish this using **`.delete(0, "end")`**! In Python GUIs, `0` represents the very first character position, and `"end"` represents the final character position. This command tells our application: *"Start at character 0, and wipe everything clean all the way to the end!"*

---

## The Complete Script: `user_text_input.py`

Create a new file named `user_text_input.py` and type in the code below. Read through the comments starting with the `#` symbol to see how we create our text input field and wire it directly to our display label!

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
window.title("Interactive Text Input")

# Set the starting width and height of our window in pixels (350 wide by 400 tall).
window.geometry("350x400")

# --- 1. THE INSTRUCTION & INPUT BOX (Like HTML <input type="text">) ---

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

# --- 2. THE DISPLAY ELEMENT (Where the typed text will appear!) ---

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

# --- 3. THE ACTION FUNCTION (Reading and displaying the data) ---


# Define our function that runs when the confirm button is clicked.
def display_message():
    # 1. READ: Use .get() to grab whatever text string the user typed into the box
    # (This is the exact equivalent of reading element.value in JavaScript!)
    typed_text = entry_box.get()

    # 2. UPDATE: Push that text onto our large green output label
    output_label.configure(text=typed_text)

    # 3. CLEAR: Wipe the entry box clean so it is ready for the user's next message!
    # "0" means start at the very first character, and "end" means delete all the way to the end.
    entry_box.delete(0, "end")


# --- 4. THE CONFIRM BUTTON ---

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

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

