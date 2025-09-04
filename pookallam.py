"""
Digital Pookkalam 🌸✨ (Round version)
Author: <Mahin aboobakkar>
"""

import turtle
import colorsys

# ---- Setup Screen ----
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Round Digital Pookkalam - Onam 2025")

# ---- Create Turtle ----
pen = turtle.Turtle()
pen.speed(0)   # fast but still visible
turtle.colormode(255)

# ---- Colors (Rainbow Gradient) ----
num_colors = 90  # more colors for smoothness
colors = [colorsys.hsv_to_rgb(i/num_colors, 1, 1) for i in range(num_colors)]
colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]

# ---- Function: Draw one rounded flower layer ----
def draw_flower(radius, petals, layer):
    for i in range(petals):
        pen.color(colors[(i * layer * 4) % num_colors])
        pen.begin_fill()
        pen.circle(radius, 80)   # smoother round arc
        pen.left(100)            # less sharp than 120
        pen.circle(radius, 80)
        pen.end_fill()
        pen.left(360 / petals)

# ---- Function: Draw dotted decorative ring ----
def draw_decorative_ring(radius, count, color, size=8):
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    for i in range(count):
        pen.forward(2 * 3.14 * radius / count)
        pen.dot(size, color)

# ---- Function: Draw the full Pookkalam ----
def draw_pookkalam():
    pen.penup()
    pen.home()
    pen.pendown()

    # Multiple flower layers
    layers = 6
    for layer in range(1, layers + 1):
        draw_flower(30 + layer * 20, 18 + layer * 4, layer)  # more petals, round look
        pen.right(5)

    # Decorative dotted rings
    draw_decorative_ring(220, 60, "white")
    draw_decorative_ring(260, 72, "gold")

    # Central glowing core
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    for r in range(50, 70, 5):
        pen.color(255, 215, 0)
        pen.begin_fill()
        pen.circle(r)
        pen.end_fill()

# ---- Run ----
draw_pookkalam()
screen.mainloop()
