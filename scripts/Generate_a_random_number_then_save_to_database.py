import random
import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")

# Create the root table with a column named ints
conn.execute("CREATE TABLE IF NOT EXISTS root (ints INTEGER)")

counter = 0
while True:
    # Generate a random number between -2147483647 and 2147483647
    random_number = random.randint(-2147483647, 2147483647)

    # Insert the random number into the root table
    conn.execute("INSERT INTO root (ints) VALUES (?)", (random_number,))
    
    counter += 1
    
    # Commit the changes after every 100000 inserts
    if counter % 100000 == 0:
        conn.commit()
