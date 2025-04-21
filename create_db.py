import sqlite3

# Connect to SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('medicines.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create the 'medicines' table if it doesn't already exist
c.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')

# Add a sample medicine record
c.execute("INSERT INTO medicines (name, description) VALUES (?, ?)",
          ("Paracetamol", "Used for fever and mild pain relief."))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and sample medicine added.")
