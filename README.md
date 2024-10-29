# Tkinter-Notes-Two



# Scale Widget
The `Scale` widget provides a graphical slider to select values within a specified range. You can customize it to be vertical or horizontal, control its range, and link it to functions to trigger actions when the value changes.

### Basic Syntax
```python
scale = Scale(master, options)
```

- `master` is the parent widget, typically the main Tkinter window or a frame.

### Common Options
Here are some key options for customizing `Scale` widgets:

- **`from_`**: Sets the starting value of the scale (e.g., `from_=0`).
- **`to`**: Sets the ending value of the scale (e.g., `to=255` for RGB values).
- **`orient`**: Determines the orientation, either `"horizontal"` or `"vertical"`.
- **`variable`**: Links the slider’s current value to an `IntVar` or `DoubleVar` variable. This way, changes to the slider are directly reflected in the variable.
- **`command`**: Specifies a function to be called whenever the slider is moved. This function receives the current slider value as an argument.
- **`bg` and `fg`**: Set the background and foreground colors of the scale widget, useful for differentiating sliders (e.g., red, green, blue for RGB).
- **`tickinterval`**: Adds labeled intervals along the slider, helping users see value ranges (e.g., `tickinterval=50` shows ticks at intervals of 50).
- **`resolution`**: Specifies the smallest increment by which the scale's value changes, such as `resolution=0.5` for half-steps.
- **`length`**: Sets the physical length of the slider in pixels (horizontal width or vertical height).

### Example Code
Here’s an example of a horizontal `Scale` widget used to set a value between 0 and 100:

```python
import tkinter as tk

def show_value(value):
    print("Current value:", value)

root = tk.Tk()
root.title("Scale Example")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=show_value, length=300)
scale.pack()

root.mainloop()
```

### Practical Tips for Using Scale Widgets
1. **Triggering Actions with `command`**: If you need to change a variable each time the slider moves, use the `command` option to call a function dynamically.
2. **Linking a Variable with `variable`**: This keeps the slider’s value stored in an `IntVar` or `DoubleVar`, making it accessible throughout your program.
3. **Styling for Usability**: For applications with multiple sliders, use colors (`bg`) or different orientations to make the widget’s purpose clear to users.

<br></br>
---
# Canvas Widget
The Tkinter `Canvas` widget is a versatile space where you can draw shapes, display images, and place other widgets. It’s perfect for creating graphics in Python GUI applications.

### Basic Syntax for Canvas
```python
canvas = Canvas(master, options)
canvas.pack()
```

- `master` is the parent widget, like the main window or a frame.
- You can customize the canvas size, background color, and other properties with options.

### Key Canvas Options
- **`width`** and **`height`**: Specify the size of the canvas.
- **`bg`**: Sets the background color of the canvas.
- **`highlightthickness`**: Sets the thickness of the border around the canvas.

### Drawing Shapes on Canvas
After creating the canvas, you can use various methods to draw shapes. These methods return an ID you can use to reference and modify the shape later.

#### 1. Draw a Line
Draws a line between two points or across multiple points.

```python
canvas.create_line(x1, y1, x2, y2, options)
```

- **Example**:
  ```python
  canvas.create_line(10, 10, 200, 200, fill="blue", width=3)
  ```

  - `fill` sets the color.
  - `width` sets the thickness of the line.

#### 2. Draw an Oval or Circle
Creates an oval within the bounding box defined by two opposite corners.

```python
canvas.create_oval(x1, y1, x2, y2, options)
```

- **Example (Circle)**:
  ```python
  canvas.create_oval(50, 50, 150, 150, fill="red")
  ```

  - The bounding box `(x1, y1, x2, y2)` defines the shape’s height and width.
  - If you want a perfect circle, ensure the width and height are the same.

#### 3. Draw a Rectangle
Creates a rectangle within the bounding box defined by two opposite corners.

```python
canvas.create_rectangle(x1, y1, x2, y2, options)
```

- **Example**:
  ```python
  canvas.create_rectangle(200, 200, 300, 300, fill="green", outline="black", width=2)
  ```

  - `outline` sets the color of the border.
  - `width` sets the thickness of the border.

#### 4. Draw a Polygon
Draws a closed shape with three or more points.

```python
canvas.create_polygon(x1, y1, x2, y2, ..., options)
```

- **Example**:
  ```python
  canvas.create_polygon(150, 75, 225, 200, 75, 200, fill="purple", outline="black")
  ```

#### 5. Draw an Arc
Draws an arc (a section of an oval) within a bounding box.

```python
canvas.create_arc(x1, y1, x2, y2, start=0, extent=150, options)
```

- **Example**:
  ```python
  canvas.create_arc(10, 50, 210, 250, start=0, extent=180, fill="yellow")
  ```

  - `start` is the starting angle (degrees).
  - `extent` specifies the angular range of the arc.

#### 6. Add Text
Displays text on the canvas at a specified location.

```python
canvas.create_text(x, y, text="Your Text", options)
```

- **Example**:
  ```python
  canvas.create_text(100, 50, text="Hello Canvas", fill="black", font=("Arial", 20))
  ```

### Example of a Canvas with Multiple Shapes
```python
import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw shapes
canvas.create_line(10, 10, 200, 200, fill="blue", width=3)
canvas.create_oval(50, 50, 150, 150, fill="red")
canvas.create_rectangle(200, 200, 300, 300, fill="green", outline="black", width=2)
canvas.create_polygon(150, 75, 225, 200, 75, 200, fill="purple", outline="black")
canvas.create_text(100, 50, text="Hello Canvas", fill="black", font=("Arial", 20))

root.mainloop()
```

### Modifying or Removing Shapes
Each shape on the canvas has a unique ID, which is returned by the `create_*` methods. Use this ID to modify or delete shapes:

- **Modify Shape**:
  ```python
  canvas.itemconfig(shape_id, fill="new_color")
  ```

- **Delete Shape**:
  ```python
  canvas.delete(shape_id)

  ```

# Moving Canvas Objects
To move objects on a Tkinter `Canvas`, you can use the `move` method, which shifts an object by a specified amount in the x and y directions. You can also set up animations by repeatedly moving objects within a loop or event sequence.

### Moving Objects with `move` Method

The `move` method has the following syntax:
```python
canvas.move(item_id, dx, dy)
```

- **`item_id`**: The ID of the item (e.g., line, rectangle) you want to move. This ID is returned when you create the object.
- **`dx`**: The amount to move the object horizontally.
- **`dy`**: The amount to move the object vertically.

### Example: Basic Moving Object

Here’s a basic example where a circle moves downwards every second:

```python
import tkinter as tk

def move_circle():
    canvas.move(circle, 0, 5)  # Move the circle 5 pixels down
    root.after(100, move_circle)  # Schedule the function to run again in 100ms

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a circle (oval) and store its ID
circle = canvas.create_oval(180, 180, 220, 220, fill="blue")

move_circle()  # Start moving the circle

root.mainloop()
```

### Moving with Arrow Keys

You can move objects interactively with keyboard input by binding the arrow keys to functions.

```python
import tkinter as tk

def move_left(event):
    canvas.move(circle, -10, 0)

def move_right(event):
    canvas.move(circle, 10, 0)

def move_up(event):
    canvas.move(circle, 0, -10)

def move_down(event):
    canvas.move(circle, 0, 10)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

circle = canvas.create_oval(180, 180, 220, 220, fill="blue")

# Bind arrow keys to move functions
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

root.mainloop()
```

In this example:
- **`root.bind("<Key>", function)`** associates each arrow key with a function that moves the circle in the corresponding direction.
- Each function moves the circle by 10 pixels in the specified direction.

### Example: Smooth Animation Loop

For smooth, continuous movement, you can use a loop with the `after` method.

```python
import tkinter as tk

def animate():
    canvas.move(circle, 2, 0)  # Move the circle 2 pixels to the right
    root.after(20, animate)    # Repeat every 20 milliseconds for smooth animation

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

circle = canvas.create_oval(50, 50, 100, 100, fill="red")

animate()  # Start the animation loop

root.mainloop()
```

### Using `coords` to Reposition Objects Directly

The `coords` method can set the absolute position of an object, rather than moving it by a relative amount.

```python
canvas.coords(item_id, x1, y1, x2, y2)
```

- **`x1, y1, x2, y2`**: Define the bounding box coordinates for the new position.

For example:
```python
canvas.coords(circle, 100, 100, 150, 150)  # Move circle to new location
```

### Putting It All Together: Moving and Animating with Arrow Keys and `after`

Here’s a combined example where pressing arrow keys changes the direction of the movement, and the object keeps moving in that direction:

```python
import tkinter as tk

def animate():
    canvas.move(circle, dx[0], dy[0])  # Move in the current direction
    root.after(20, animate)             # Repeat every 20 milliseconds

def set_direction_left(event):
    dx[0], dy[0] = -5, 0

def set_direction_right(event):
    dx[0], dy[0] = 5, 0

def set_direction_up(event):
    dx[0], dy[0] = 0, -5

def set_direction_down(event):
    dx[0], dy[0] = 0, 5

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

circle = canvas.create_oval(180, 180, 220, 220, fill="blue")

dx = [0]
dy = [0]

root.bind("<Left>", set_direction_left)
root.bind("<Right>", set_direction_right)
root.bind("<Up>", set_direction_up)
root.bind("<Down>", set_direction_down)

animate()  # Start the animation loop

root.mainloop()
```

In this example:
- The `dx` and `dy` lists store the current movement direction.
- Pressing an arrow key updates `dx` and `dy`, causing the object to change direction.
- The `animate` function continuously moves the object based on `dx` and `dy`, creating a smooth animation that responds to keyboard input.

