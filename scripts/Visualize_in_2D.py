import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("example.db")

# Retrieve the numbers from the root table
cursor = conn.execute("SELECT int1, int2 FROM root")
data = cursor.fetchall()

# Extract the x and y coordinates from the data
x = [row[0] for row in data]
y = [row[1] for row in data]

# Create a scatter plot
plt.scatter(x, y)

# Set the axis labels
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
