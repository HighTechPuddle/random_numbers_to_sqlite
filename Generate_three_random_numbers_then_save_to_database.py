import random
import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")

# Create the root table with three columns named int1, int2, and int3
conn.execute("CREATE TABLE IF NOT EXISTS root (int1 INTEGER, int2 INTEGER, int3 INTEGER)")

counter = 0
while True:
    # Generate three random numbers between -2147483647 and 2147483647
    random_number1 = random.randint(-2147483647, 2147483647)
    random_number2 = random.randint(-2147483647, 2147483647)
    random_number3 = random.randint(-2147483647, 2147483647)

    # Insert the triplet of random numbers into the root table
    conn.execute("INSERT INTO root (int1, int2, int3) VALUES (?, ?, ?)", (random_number1, random_number2, random_number3))
    
    counter += 1
    
    # Commit the changes after every 100000 inserts
    if counter % 100000 == 0:
        conn.commit()
