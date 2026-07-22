# Interactive Sliders & Live Value Tracking

In our previous tutorials, our applications relied on discrete events: typing text into a box and pressing a button to trigger a calculation. While buttons are great for confirming actions, some data is much better explored dynamically!

Today, we are going to introduce a brand new interactive component: the **Slider** (`CTkSlider`). 

If you have ever built a web page, you know this tool as an HTML range input (`<input type="range">`). A slider allows the user to click and drag a visual handle across a track to select a value within a minimum and maximum range. We are going to wire our application so that dragging the slider updates a large number display on our screen in real-time—giving our users buttery-smooth, continuous visual feedback!

---

## Three Core Concepts for Today

### 1. The Slider Widget (`CTkSlider`)
To create a slider in CustomTkinter, we use **`CTkSlider`**. When we set up our track, we define the minimum value, the maximum value, and the physical width of the track on screen. We can also use `.set(50)` to tell the slider where to position its draggable handle when the window first opens!

### 2. The `from_` Keyword Trap
When setting the range of our slider from 0 to 100, you will notice something interesting in our syntax:
```python
# Notice the underscore after the word 'from'!
slider = ctk.CTkSlider(..., from_=0, to=100)

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

