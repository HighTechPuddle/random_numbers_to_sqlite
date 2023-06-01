import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")

# Calculate the sum of all the numbers in the ints column
cursor = conn.execute("SELECT SUM(ints) FROM root")
result = cursor.fetchone()
total_sum = result[0]

print(f"The sum of all the numbers in the database is: {total_sum}")
