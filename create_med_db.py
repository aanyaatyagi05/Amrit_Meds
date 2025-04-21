import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('medicines.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS medicines')


# Create the medicines table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        price INTEGER
    )
''')

# List of medicine records
medicines = [
    ("Odloxacin", "Antibiotic", "Effective against a wide range of bacteria.", 75),
    ("Ciplox TZ", "Antibiotic", "Combination of Ciprofloxacin and Tinidazole.", 30),
    ("Liv 52 DS", "Liver Care", "Supports liver health and detoxification.", 100),
    ("I-AL", "Painkiller", "Relieves mild to moderate pain.", 200),
    ("Option", "Multivitamin", "Provides essential vitamins and minerals.", 150),
    ("Citrocin", "Antibiotic", "Treats respiratory and urinary tract infections.", 80),
    ("Aciloc", "Antacid", "Reduces stomach acid production.", 110),
    ("Aspirin", "Painkiller", "Relieves pain, fever, and inflammation.", 200),
    ("Disprin", "Painkiller", "Relieves headaches and minor aches.", 250),
]

# Insert data into the table
cursor.executemany('''
    INSERT INTO medicines (name, category, description, price)
    VALUES (?, ?, ?, ?)
''', medicines)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'medicines.db' created and populated successfully.")
