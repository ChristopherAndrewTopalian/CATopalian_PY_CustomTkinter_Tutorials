# Interactive Toggle Switches & Conditional Logic

In our previous tutorials, our interfaces were driven by continuous numerical data from sliders and text boxes. But in software design, many controls don't need a hundred different numbers—they only need two states: **ON** or **OFF**. 

Today, we are going to build an interactive **System Power Switch** using the modern **Toggle Switch (`CTkSwitch`)**. 

If you have ever built a web page using HTML, you know this element as the classic checkbox (`<input type="checkbox">`). CustomTkinter takes that familiar checkbox mechanism and styles it into a sleek, sliding iOS/Android-style pill toggle. Whenever you flip the switch, our application will instantly evaluate the switch's binary state and change our system readout between **💤 STANDBY** and **⚡ ONLINE**!

---

## Three Core Concepts for Today

To connect an ON/OFF toggle switch to a visual display, we get to introduce one of the most fundamental building blocks in all of computer science: conditional logic!

### 1. The Toggle Widget (`CTkSwitch`)
To create a modern toggle switch, we instantiate a **`CTkSwitch`**. Just like a push button or a slider, we can attach a function directly to the switch using `command=toggle_power`. Whenever the user clicks the switch or drags the toggle handle, our function executes immediately!

### 2. Binary States (`1` and `0`)
How does Python know whether your switch is currently flipped ON or flipped OFF? We call the **`.get()`** method! 

When you call `power_switch.get()`, CustomTkinter returns a simple binary integer:
* **`1`**: The switch is **ON** (Checked / True).
* **`0`**: The switch is **OFF** (Unchecked / False).

### 3. Conditional Logic (`if` / `else`)
Now that we have a binary number (`1` or `0`), how do we tell our application to display different text depending on that number? We use an **`if` / `else` block**! 

If you have used JavaScript, Python's conditional syntax will feel completely natural. We simply write:
```python
if current_state == 1:
    # Do this if the switch is ON!
else:
    # Do this if the switch is OFF!

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

