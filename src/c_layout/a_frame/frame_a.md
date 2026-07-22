# Creating Layout Containers (The Python Equivalent of a `<div>`)

Up until now, every element we have built—labels, buttons, text boxes, sliders, and progress bars—has been stacked directly onto the main application window. 

But as your applications grow larger, you need a way to group related elements together into distinct visual sections, cards, or panels. In web development, you accomplish this using the ubiquitous **`<div>` tag**.

Today, we are going to learn how to create layout containers in CustomTkinter using **Frames (`CTkFrame`)**. A `CTkFrame` is the exact 1-to-1 equivalent of an HTML `<div>`. We will build a styled tactical container box, customize its background color and borders, and learn the golden rule of nesting elements inside it!

---

## Three Core Concepts for Today

To build layout containers without CSS or stylesheets, we rely on three straightforward concepts:

### 1. The Frame Widget (`CTkFrame`)
To create a layout container in CustomTkinter, we instantiate a **`CTkFrame`**. This acts as our structural `<div>`. We can explicitly define its physical width and height, give it a custom background color (`fg_color`), and even add a clean structural border (`border_width` and `border_color`) so it stands out like a professional UI card.

### 2. The Golden Rule of Nesting
In HTML, if you want to put text or a button inside a `<div>`, you simply place it between the opening and closing tags:
```html
<div class="card">
    <h1>Hello World</h1>
</div>

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

