import sqlite3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Connect to the database
conn = sqlite3.connect("example.db")

# Retrieve the numbers from the root table
cursor = conn.execute("SELECT int1, int2, int3 FROM root")
data = cursor.fetchall()

# Extract the x, y, and z coordinates from the data
x = [row[0] for row in data]
y = [row[1] for row in data]
z = [row[2] for row in data]

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
