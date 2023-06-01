import sqlite3
import cairo
import math

# Connect to the database
conn = sqlite3.connect("example.db")

# Retrieve the numbers from the root table
cursor = conn.execute("SELECT int1, int2 FROM root")
data = cursor.fetchall()

# Extract the x and y coordinates from the data
x = [row[0] for row in data]
y = [row[1] for row in data]

# Set the width and height of the image
width, height = 1000, 1000

# Create a new PDF surface
surface = cairo.PDFSurface("scatter_plot.pdf", width, height)

# Create a new context
ctx = cairo.Context(surface)

# Set the background color to white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set the point color to blue
ctx.set_source_rgb(0, 0, 1)

# Set the point size
point_size = 5

# Draw the points
for i in range(len(x)):
    ctx.arc(x[i], y[i], point_size, 0, 2 * math.pi)
    ctx.fill()

# Finish the drawing
ctx.show_page()
surface.finish()
