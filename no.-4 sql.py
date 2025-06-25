import csv

data = [["name","address","mobile","email"],["John Doe","123 Main St, Anytown, USA","5551234567","john.doe@example.com"],
["Jane Smith","456 Oak Ave, Somewhere, USA","5559876543","jane.smith@example.com"],
["Peter Jones","789 Pine Rd, Nowhere, USA","5551112222","peter.jones@example.com"]]

with open("data1.csv","w") as file:
    writer = csv.writer(file)
    for x in data :
        writer.writerow(x)
import csv
with open("data1.csv","r") as file:
    reader = csv.reader(file)
    for x in data :
        print(x)


print("\n\n\n\n\n---database using sqlite---")
import sqlite3

# Define the database file name
DB_FILE = 'db2.db'

# Connect to the database. If it doesn't exist, SQLite will create it.
conn = sqlite3.connect(DB_FILE)
print(f"Connected to database: {DB_FILE}")

# Create a table called 'students'
# IF NOT EXISTS means it won't throw an error if the table already exists.
conn.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
print("Table 'students' created successfully or already exists.")

# Save the changes to the database
conn.commit()

# Insert some sample data into the 'students' table
students_data = [
    ('Alice', 20),
    ('Bob', 22),
    ('Charlie', 21)
]
# executemany is used to insert multiple rows at once
conn.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students_data)
print("\nInserted sample data into 'students' table.")

# Save the inserted data to the database
conn.commit()

# Select all data from the 'students' table
print("\n--- All students in the database: ---")
results = conn.execute("SELECT * FROM students")

# Loop through and print each row
for row in results:
    print(row)

# Close the database connection
conn.close()
print("\nDatabase connection closed.")