# Animated Progress Bars & Shield Energy Recharger

In our previous tutorials, we explored controls that update instantly with a single click or a dragged motion. But in many software applications, you need to display visual **progress over time**—like monitoring a file download, tracking an installation wizard, or powering up a ship's defense grid.

Today, we are going to build an interactive **Tactical Shield Energy Recharger** using the **Progress Bar (`CTkProgressBar`)**. 

If you have ever built a web page, you know this component as the HTML `<progress>` element. A progress bar displays a visual fill-meter that tracks completion. We will wire a push button so that every time the operative hits "Charge Energy Core," our progress bar pulses forward by 20% until our defense grid reaches maximum capacity!

---

## Three Core Concepts for Today

To build an animated progress meter without complex background threads, we rely on three straightforward tools:

### 1. The Progress Bar Widget (`CTkProgressBar`)
To create a progress meter in CustomTkinter, we instantiate a **`CTkProgressBar`**. We can customize its physical dimensions and even change its internal energy color using `progress_color="#3DAEE9"` so it glows with a high-tech cyan blue hue!

### 2. Decimal Progress Tracking (0.0 to 1.0)
Unlike percentage numbers (0 to 100) or pixel dimensions, CustomTkinter progress bars operate on **decimals ranging from 0.0 to 1.0**:
* **`0.0`**: The bar is completely empty (0%).
* **`0.5`**: The bar is halfway full (50%).
* **`1.0`**: The bar is completely full (100%).

When we want to update the bar, we simply call **`shield_bar.set(0.4)`** to jump the fill-line directly to 40%!

### 3. Incremental State Logic
To make our recharger interactive, we create a tracking variable (`shield_progress = 0.0`). Every time the button is clicked, our function adds `0.2` to that variable, updates the progress bar, and uses an `if/elif` check to update our warning text from red to yellow and finally to green when full!

---

## The Complete Script: `tactical_shield_charger.py`

Create a new file named `tactical_shield_charger.py` and type in the code below. Notice how clean the top-to-bottom layout is—we declare our tracker at the top, build our visual HUD in the middle, and anchor our incremental recharge button at the bottom!

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
window.title("Tactical Shield Energy Recharger")

# Set the starting width and height of our window in pixels (400 wide by 400 tall).
window.geometry("400x400")

# --- 1. TRACKING THE PROGRESS (The State Variable) ---

# CustomTkinter progress bars operate on decimals from 0.0 (empty) to 1.0 (full).
# We create a tracking variable starting at 0.0 (shields completely offline).
shield_progress = 0.0

# --- 2. THE DISPLAY ELEMENTS (Readout label and Progress Bar) ---

title_label = ctk.CTkLabel(
    window, text="Defense Grid Status:", font=("Segoe UI", 18, "bold")
)
title_label.pack(pady=(35, 15))

# Create our status readout label!
status_display = ctk.CTkLabel(
    window,
    text="SHIELDS: OFFLINE (0%)",
    font=("Segoe UI", 22, "bold"),
    text_color="#FF5733",  # Start with a warning red color!
)
status_display.pack(pady=10)

# Create our progress bar widget! (Like HTML <progress> element)
# We set width=280 and height=20 to make it nice and chunky on screen.
shield_bar = ctk.CTkProgressBar(
    window,
    width=280,
    height=20,
    progress_color="#3DAEE9",  # Icy cyan blue energy color!
)
# Set the bar to start completely empty at 0.0
shield_bar.set(0.0)
shield_bar.pack(pady=20)

# --- 3. THE ACTION FUNCTION (Increments the progress meter) ---


# This function runs every time the operative presses the recharge button
def recharge_shield():
    # Use 'global' so we can modify our tracking variable outside this function
    global shield_progress

    # Check if shields are already fully charged (1.0)
    if shield_progress < 1.0:
        # Add 20% (0.2) to our current progress level
        shield_progress = shield_progress + 0.2

        # Send the decimal value straight to the progress bar!
        shield_bar.set(shield_progress)

        # Update our text readout and color based on the current charge level
        if shield_progress >= 1.0:
            status_display.configure(
                text="SHIELDS: FULLY CHARGED (100%)", text_color="#48FF91"
            )
        elif shield_progress >= 0.6:
            status_display.configure(
                text="SHIELDS: STABLE (60% - 80%)", text_color="#FFD166"
            )
        else:
            status_display.configure(
                text="SHIELDS: CHARGING...", text_color="#3DAEE9"
            )


# --- 4. THE RECHARGE PUSH BUTTON ---

recharge_btn = ctk.CTkButton(
    window,
    text="⚡ Charge Energy Core (+20%)",
    font=("Segoe UI", 16, "bold"),
    fg_color="#2E7D32",  # Rugged tactical green
    hover_color="#1B5E20",
    command=recharge_shield,
)
recharge_btn.pack(pady=20)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

