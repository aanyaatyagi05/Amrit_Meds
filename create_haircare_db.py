import sqlite3

# Connect to a new SQLite database file (or open it if it already exists)
conn = sqlite3.connect('haircare.db')
cursor = conn.cursor()

# Create the table for haircare products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS haircare_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        description TEXT,
        price REAL,
        quantity TEXT,
        usage TEXT,
        company TEXT,
        image TEXT
    )
''')

# Insert data
haircare_products = [
    ("Minoxidil 5%", "Hair Growth", "Treats hair loss and promotes regrowth", 550, "60ml", "Apply to scalp twice daily", "Dr. Reddy's", "minoxidil.jpg"),
    ("Anaboom Shampoo", "Shampoo", "Anti-hair fall and scalp care formula", 380, "100ml", "Use thrice a week", "Sun Pharma", "anaboom.jpg"),
    ("Triclenz Shampoo", "Shampoo", "For hair and scalp cleansing", 410, "100ml", "Use every alternate day", "Curatio", "triclenz.jpg"),
    ("Hairbless Tablets", "Supplement", "Rich in biotin", 630, "30 tablets", "One tablet daily", "Ajanta Pharma", "hairbless.jpg"),
    ("Sebamed Anti-Hairloss Shampoo", "Shampoo", "Gentle pH 5.5 shampoo", 480, "200ml", "Use twice a week", "Sebamed", "sebamed.jpg"),
    ("Baidyanath Mahabhringraj Oil", "Hair Oil", "Ayurvedic oil", 180, "200ml", "Massage into scalp", "Baidyanath", "mahabhringraj.jpg"),
    ("Indulekha Bringha Oil", "Hair Oil", "Reduces hair fall", 430, "100ml", "Apply directly to scalp", "Hindustan Unilever", "indulekha.jpg")
]

cursor.executemany('''
    INSERT INTO haircare_products (name, category, description, price, quantity, usage, company, image)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', haircare_products)

# Save and close
conn.commit()
conn.close()

print("Database created and haircare products inserted.")
