# Precision Sliders (`0.1` Increments) & Dynamic Element Resizing

In our previous slider tutorial, we used `int()` to chop off all decimal numbers, forcing our slider to output clean, whole integers from 0 to 100. 

But what if you are building an interface that requires high precision—like calibrating an audio frequency, setting a 3D simulation scale factor, or dynamically resizing a UI element on the screen? For tasks like these, you need a slider that moves smoothly in **`0.1` decimal increments**.

Today, we will learn how to configure a CustomTkinter slider to snap to exact decimal steps, how to format floating-point numbers cleanly without ugly trailing decimals, and how to use that slider to dynamically resize the physical width of a `<div>` container (`CTkFrame`) in real-time!

---

## Three Core Concepts for Today

### 1. Slicing the Track (`number_of_steps`)
In HTML web development, creating a decimal slider is done by setting the step increment directly: `<input type="range" step="0.1">`. 

CustomTkinter uses a different mathematical model: instead of defining the *size* of each step, you define the **total number of notches (`number_of_steps`)** sliced across the track.
* If your slider ranges from `1` to `10`, the total span is `9` units wide.
* To get `0.1` increments across a span of 9, you divide: $9 / 0.1 = 90$.
* By passing **`number_of_steps=90`** into our `CTkSlider`, Python automatically slices the track into 90 exact notches—forcing the handle to snap cleanly to `1.1`, `1.2`, `1.3`, and so on!

### 2. Clean Decimal Formatting (`:.1f`)
Computers natively calculate math in binary, which often causes floating-point numbers to develop trailing decimal errors (for example, displaying `4.300000000000001` instead of `4.3`).

In JavaScript, you fix this by calling `.toFixed(1)`. In Python f-strings, we use the formatting code **`:.1f`**:
```python
clean_text = f"{value:.1f}"
```
---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

