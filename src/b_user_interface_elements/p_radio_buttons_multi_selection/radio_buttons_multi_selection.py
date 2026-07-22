# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Tactical Mission Loadout Builder")

# Set the starting width and height of our window in pixels (400 wide by 500 tall).
window.geometry("400x500")

# INDEPENDENT CONTROL VARIABLES (One memory box per piece of gear)

# Unlike radio buttons that share ONE variable, checkboxes operate independently.
# We create a separate binary integer variable (IntVar) for each piece of equipment.
# 0 means unselected (OFF), and 1 means selected (ON).
nvg_var = ctk.IntVar(value=0)
armor_var = ctk.IntVar(value=0)
suppressor_var = ctk.IntVar(value=0)

# THE DISPLAY ELEMENT (Our mission HUD readout)

title_label = ctk.CTkLabel(
    window,
    text="Select Tactical Equipment:",
    font=("Segoe UI", 20, "bold"),
)
title_label.pack(pady=(35, 15))

# Create our large readout label! We start with a standard default loadout.
# We also include wraplength=350 so that if they select all three items,
# the text wraps neatly to a new line instead of running off the screen!
loadout_display = ctk.CTkLabel(
    window,
    text="Standard Issue Only",
    font=("Segoe UI", 24, "bold"),
    text_color="#48FF91",
    wraplength=350,
)
loadout_display.pack(pady=25)

# THE ACTION FUNCTION (Building the custom loadout)

# This function runs instantly whenever ANY of our checkboxes are clicked!
def update_loadout():
    # Create an empty list to hold whatever gear the operative selects
    equipped_items = []

    # Check each variable independently using simple binary logic (1 = ON):
    if nvg_var.get() == 1:
        equipped_items.append("🥽 Night Vision")

    if armor_var.get() == 1:
        equipped_items.append("🛡️ Heavy Armor")

    if suppressor_var.get() == 1:
        equipped_items.append("🤫 Suppressor")

    # Now, check if our list is empty!
    # If len() is 0, the operative unchecked everything.
    if len(equipped_items) == 0:
        loadout_display.configure(
            text="Standard Issue Only", text_color="#A5B6C6"
        )
    else:
        # If items were selected, use Python's .join() tool to combine our list into
        # a clean text string separated by bullets, and turn the display green!
        combined_string = " • ".join(equipped_items)
        loadout_display.configure(text=combined_string, text_color="#48FF91")


# THE CHECKBOX ELEMENTS (Like HTML <input type="checkbox">)

# Checkbox 1: Night Vision Goggles
# Notice we connect it to 'nvg_var' and give it a rugged tactical green color!
nvg_box = ctk.CTkCheckBox(
    window,
    text="Equip Night Vision Goggles",
    font=("Segoe UI", 16),
    variable=nvg_var,  # Links to our first independent variable
    fg_color="#2E7D32",  # Rugged forest green accent
    hover_color="#1B5E20",  # Darker green on hover
    command=update_loadout,  # Runs our loadout builder
)
nvg_box.pack(pady=12, padx=60, anchor="w")  # anchor="w" aligns the box to the West (left) side!

# Checkbox 2: Heavy Body Armor
armor_box = ctk.CTkCheckBox(
    window,
    text="Equip Heavy Body Armor",
    font=("Segoe UI", 16),
    variable=armor_var,  # Links to our second independent variable
    fg_color="#2E7D32",
    hover_color="#1B5E20",
    command=update_loadout,
)
armor_box.pack(pady=12, padx=60, anchor="w")

# Checkbox 3: Stealth Suppressor
suppressor_box = ctk.CTkCheckBox(
    window,
    text="Equip Acoustic Suppressor",
    font=("Segoe UI", 16),
    variable=suppressor_var,  # Links to our third independent variable
    fg_color="#2E7D32",
    hover_color="#1B5E20",
    command=update_loadout,
)
suppressor_box.pack(pady=12, padx=60, anchor="w")

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

