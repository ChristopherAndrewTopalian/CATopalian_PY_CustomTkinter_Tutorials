# Import the CustomTkinter library and give it the short nickname 'ctk'.
import customtkinter as ctk

# Tell the library to use a low-light 'dark' theme to protect our eyes from screen glare.
ctk.set_appearance_mode("dark")

# Set the default accent color to blue.
ctk.set_default_color_theme("blue")

# Create our main application window and store it in the simple variable 'window'.
window = ctk.CTk()

# Set the title text that appears up in the top bar of our window.
window.title("Tactical Scrollable Frame")

# Set the starting width and height of our window in pixels (450 wide by 500 tall).
window.geometry("450x500")

# THE MAIN TITLE

title_label = ctk.CTkLabel(
    window,
    text="SECURE COMMUNICATIONS LOG",
    font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(25, 15))

# CREATING A SCROLLABLE FRAME (The Scrollable Div Equivalent)

# In CustomTkinter, a scrollable container is called a 'CTkScrollableFrame'.
# This is the exact equivalent of a <div> with CSS 'overflow-y: auto' in web development.
# We set an explicit width and height so that any content taller than 300px automatically scrolls.
scrollable_log = ctk.CTkScrollableFrame(
    window,
    width=360,
    height=300,
    fg_color="#1F2937",  # Sleek dark-slate background
    border_width=2,
    border_color="#3DAEE9",  # Icy cyan border
)
scrollable_log.pack(pady=10)

# POPULATING THE SCROLLABLE FRAME WITH CONTENT

# To make sure our text elements never overhang or clip through our frame's borders,
# we apply safe horizontal padding (padx=20) and left-alignment (anchor="w") to every item.

log_header = ctk.CTkLabel(
    scrollable_log,  # Nested inside our scrollable frame
    text="--- TRANSMISSION HISTORY ---",
    font=("Segoe UI", 14, "bold"),
    text_color="#FFD166",
)
log_header.pack(pady=(15, 10), padx=20, anchor="w")

# Add a series of classified transmission log entries
transmission_entries = [
    "[0400 HRS] Sector Alpha perimeter secured.",
    "[0415 HRS] Recon drone launched from FOB Delta.",
    "[0530 HRS] Weather anomaly detected in Northern Grid.",
    "[0600 HRS] Shift change completed for Ground Forces.",
    "[0715 HRS] Supply drop received at Outpost Echo.",
    "[0800 HRS] Satellite uplink re-established.",
    "[0930 HRS] Routine patrol reported zero hostile contacts.",
    "[1045 HRS] Fuel reserves at 85% capacity across all units.",
    "[1200 HRS] Midday command briefing concluded.",
]

# Use a clean for-loop to quickly generate and pack each log entry into our scrollable frame
for entry in transmission_entries:
    log_item = ctk.CTkLabel(
        scrollable_log,  # Nested inside our scrollable container!
        text=entry,
        font=("Segoe UI", 13),
        text_color="#A5B6C6",
    )
    # padx=20 guarantees our text stays safely inside the frame boundaries without clipping!
    log_item.pack(pady=6, padx=20, anchor="w")

# Turn on the window and keep it running in an endless loop until the user clicks X to close it.
window.mainloop()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

