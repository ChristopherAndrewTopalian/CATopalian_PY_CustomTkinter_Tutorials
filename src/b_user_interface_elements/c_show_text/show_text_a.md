# Showing Text on Screen

In our last lesson, we built a clean, dark-themed window. It looked great, but it was completely empty!

Today, we are going to learn how to put text on the screen. If you have ever built a basic web page using HTML, you already know the workflow: first, you create a text tag (like an `<h1>` or `<p>`), and then the browser renders it on the page.

In CustomTkinter, we follow that exact same two-step pattern: we **create** the text element in Python's memory, and then we **pack** it onto our window layout.

---

## Two New Concepts for Today

Before we look at the full code, let's look at the two tools we are adding to our toolbelt:

### 1. The Text Tag (`CTkLabel`)

In standard GUI programming, any static text displayed on the screen is called a **Label**. Think of a label as the exact equivalent of an HTML `<h1>` heading or `<p>` paragraph tag. When we create a label, we tell Python three things:

* **Where it lives:** Inside our main `window`.
* **What it says:** Using `text="Hi everyone!"`.
* **How it looks:** Using `font=("Segoe UI", 24, "bold")` to set the font family, size in pixels, and font weight.

### 2. The Layout Engine (`.pack()`)

If you just create a label in your script, nothing will show up on the screen! Why? Because Python created the text inside its memory, but you haven't told the layout engine *where* to put it on the page yet.

Calling **`.pack()`** is how we place elements onto the screen. It works just like calling `document.body.append()` in JavaScript or using `display: block` in CSS—it drops your element onto the page and stacks things neatly from top to bottom.

---

## The Complete Script: `03_showing_text.py`

Create a new file named `03_showing_text.py` and type in the code below. Read through the comments starting with the `#` symbol to see exactly how our new text instructions fit into the dark-theme window we built in Lesson 2!

```python
# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from glare.
ctk.set_appearance_mode("dark")

# Set the default accent color (used for borders and highlights) to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Lesson 3: Showing Text")

# Set the starting width and height of our window in pixels (400 wide by 300 tall).
window.geometry("400x300")

# --- ADDING TEXT (Just like creating an <h1> tag in HTML!) ---

# Create a text label attached to our 'window' displaying the words "Hi everyone!".
# We also set a clean font ('Segoe UI'), make it 24 pixels tall, and bold it so it reads clearly.
greeting_label = ctk.CTkLabel(
    window, text="Hi everyone!", font=("Segoe UI", 24, "bold")
)

# Place the label onto the window layout using .pack() (like appending to document body).
# Notice we add 50 pixels of vertical padding (pady=50) so it sits nicely near the center!
greeting_label.pack(pady=50)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

```

---

## Step-by-Step Breakdown of the New Lines

Let's zoom in on the two lines of code that made the text appear:

```python
greeting_label = ctk.CTkLabel(
    window, text="Hi everyone!", font=("Segoe UI", 24, "bold")
)

```

* Here, we instantiate (create a new instance of) the `CTkLabel` widget. We save it into a variable named `greeting_label` so we can control it later.
* We pass in `window` as the first argument so the label knows which screen it belongs to.

```python
greeting_label.pack(pady=50)

```

* This is the layout command. When we call `.pack()`, CustomTkinter places the label at the top center of our window by default.
* **What is `pady=50`?** The word `pad` stands for **padding (empty breathing space around an element)**, and the `y` stands for the vertical Y-axis. By asking for `pady=50`, we are telling the window: *"Put 50 pixels of empty space above and below this text so it doesn't press up against the top roof of the window!"*

---

## How to Run Your Script

1. Save your script as `03_showing_text.py`.
2. Open your terminal in the same folder where you saved the file.
3. Run the script by typing:
```bash
python 03_showing_text.py

```


4. A dark, 400x300 window will appear on your screen with the words **"Hi everyone!"** displayed clearly in a bold, modern font near the top center!

---

## What's Next?

Right now, our text is static—it just sits there like a printed poster. In **Lesson 4**, we are going to make our window interactive by adding a **Push Button** (`CTkButton`) directly below our text, using the exact same `.pack()` layout system!

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

