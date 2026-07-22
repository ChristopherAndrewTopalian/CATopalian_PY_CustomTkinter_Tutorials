# Passing Parameters with Lambda Functions

In our previous tutorial, we learned how to connect multiple buttons to a single display screen by writing a dedicated action function for each button (`show_dog()`, `show_cat()`, `show_bird()`). 

While that approach works, writing repetitive functions can quickly clutter up our code. What if we had 50 different animals? We wouldn't want to write 50 different functions!

Today, we are going to level up our programming architecture. We will replace those separate functions with **ONE dynamic helper function** that accepts **parameters**. Along the way, we will unlock one of Python's most essential GUI tools: the **`lambda`** function!

---

## Three Core Concepts for Today

### 1. DRY Programming (Don't Repeat Yourself)
In web development and software engineering, a golden rule is **DRY: Don't Repeat Yourself**. Instead of writing three almost-identical functions, we can write a single function named `update_display(animal_word, color_hex)` that accepts variables. Whenever a button is pressed, it hands its custom word and color over to this single helper!

### 2. The Immediate Execution Trap
When attaching a function to a button, your first instinct might be to write this:
```python
# ❌ THIS WILL CAUSE A BUG!
command = update_display("🐶 DOG", "#3DAEE9")

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

