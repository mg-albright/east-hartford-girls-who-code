import turtle

# Define colors
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

# Create the turtle object
t = turtle.Turtle()
t.speed(0)  # Set turtle speed to maximum
turtle.bgcolor('black')  # Set background color

# Loop to draw the spiral
for x in range(360):
    t.pencolor(colors[x % 6])  # Cycle through the list of colors
    t.width(x // 100 + 1)  # Set the pen width
    t.forward(x)  # Move forward by x units
    t.left(59)  # Turn left by 59 degrees

turtle.done()  # Keeps the turtle window open
