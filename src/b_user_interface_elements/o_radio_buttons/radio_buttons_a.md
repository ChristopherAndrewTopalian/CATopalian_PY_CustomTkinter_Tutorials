# Mutually Exclusive Choices with Radio Buttons

In our previous tutorials, we built controls that trigger independent actions or toggle a single binary setting on and off. But what happens when we want to give our user a list of options where **only one choice can be selected at a time**—like choosing a difficulty setting, a shipping method, or an audio sample rate?

Today, we are going to build a **Game Difficulty Selector** using modern **Radio Buttons (`CTkRadioButton`)**. 

If you have ever built a web form using HTML, you know this element as `<input type="radio">`. Radio buttons are designed specifically for mutually exclusive choices: the moment you click "Hard Mode," the application automatically deselects "Easy Mode" for you! We will wire three radio buttons to smoothly update a color-coded status display in real-time.

---

## Three Core Concepts for Today

To group separate radio buttons together so they communicate with each other, we introduce a powerful new concept from the CustomTkinter engine:

### 1. The Shared Control Variable (`ctk.StringVar`)
In HTML, how does the browser know that three different radio buttons belong to the exact same multiple-choice question? You give them all the exact same attribute: `name="difficulty"`. 

In CustomTkinter, we achieve this by creating a single **Shared Control Variable** before we build our buttons:
```python
difficulty_var = ctk.StringVar(value="Easy")

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

