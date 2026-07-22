# Multi-Select Checkboxes & Tactical Loadout Builder

In our previous tutorial, we explored **Radio Buttons**—an interface tool designed for mutually exclusive decisions where selecting one option automatically forces all other options to turn off. 

While that is perfect for choosing difficulty settings, many real-world scenarios require **multi-select capabilities**. When preparing for a tactical mission, an operative doesn't want to be forced to choose between body armor *or* night vision goggles—they need an interface that allows them to equip **both** at the same time!

Today, we are going to build an interactive **Tactical Mission Loadout Builder** using modern **Checkboxes (`CTkCheckBox`)**. 

If you have ever built a web form using HTML, you know this element as `<input type="checkbox">`. Checkboxes are designed specifically for independent toggling: checking one box has zero effect on the others. We will wire three tactical gear checkboxes to dynamically assemble a custom mission readout on our screen!

---

## Three Core Concepts for Today

To allow multiple options to be selected at the same time, we need to adapt how we manage our memory variables:

### 1. Independent Control Variables (`ctk.IntVar`)
With radio buttons, we created a *single* shared variable because we only ever wanted to remember one choice. But with checkboxes, every single item needs to remember its own personal state! 

To accomplish this, we instantiate three completely separate integer variables at the top of our script:
```python
nvg_var = ctk.IntVar(value=0)
armor_var = ctk.IntVar(value=0)
suppressor_var = ctk.IntVar(value=0)

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

