# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Tactical Deployment Sector Selector")

# Set the starting width and height of our window in pixels (400 wide by 400 tall).
window.geometry("400x400")

# THE DISPLAY ELEMENT (Our mission deployment HUD readout)

title_label = ctk.CTkLabel(
    window,
    text="Select Target Deployment Sector:",
    font=("Segoe UI", 18, "bold"),
)
title_label.pack(pady=(35, 15))

# Create our large HUD display label! We start with our default Sector 1.
# Notice we use wraplength=350 so long sector descriptions wrap neatly!
hud_display = ctk.CTkLabel(
    window,
    text="📍 DEPLOYING TO:\nSector 1: Arctic Tundra",
    font=("Segoe UI", 24, "bold"),
    text_color="#3DAEE9",  # Start with an icy cyan blue color!
    wraplength=350,
)
hud_display.pack(pady=30)

# THE ACTION FUNCTION (Updates the HUD when an option is selected)

# When an Option Menu item is clicked, CustomTkinter automatically passes the exact
# text string of the selected item into our function! We capture it as 'selected_zone'.
def update_deployment(selected_zone):
    # Use if/elif/else logic to dynamically change our HUD accent color based on the terrain
    if "Arctic" in selected_zone:
        # Icy cyan blue for cold weather
        hud_display.configure(
            text=f"📍 DEPLOYING TO:\n{selected_zone}", text_color="#3DAEE9"
        )
    elif "Desert" in selected_zone:
        # Arid amber/yellow for desert heat
        hud_display.configure(
            text=f"📍 DEPLOYING TO:\n{selected_zone}", text_color="#FFD166"
        )
    elif "Jungle" in selected_zone:
        # Forest green for deep jungle operations
        hud_display.configure(
            text=f"📍 DEPLOYING TO:\n{selected_zone}", text_color="#48FF91"
        )
    else:
        # High-alert orange for dense urban combat zones
        hud_display.configure(
            text=f"📍 DEPLOYING TO:\n{selected_zone}", text_color="#FF9F1C"
        )


# THE DROPDOWN OPTION MENU (Like HTML <select> and <option>)

# Create a list of tactical sector strings that will appear inside our menu
sectors_list = [
    "Sector 1: Arctic Tundra (Sub-Zero)",
    "Sector 2: Desert Outpost (Arid)",
    "Sector 3: Deep Jungle (Humid)",
    "Sector 4: Urban Metro (High Density)",
]

# Create our dropdown option menu!
# 1. We pass values=sectors_list to populate the menu items (like HTML <option> tags).
# 2. We pass command=update_deployment so it updates our HUD instantly when clicked!
# 3. We style it with a rugged tactical green foreground color.
deployment_menu = ctk.CTkOptionMenu(
    window,
    values=sectors_list,
    font=("Segoe UI", 16, "bold"),
    fg_color="#2E7D32",  # Rugged forest green button
    button_color="#1B5E20",  # Darker green dropdown arrow button
    button_hover_color="#144317",
    width=280,
    height=40,
    command=update_deployment,
)

# By default, Option Menus display the very first item in the list (index 0).
# We place the menu onto our layout!
deployment_menu.pack(pady=20)

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

