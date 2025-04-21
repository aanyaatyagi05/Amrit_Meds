
# haircare.py

import sqlite3  # Needed to interact with SQLite databases

# This function connects to the database, fetches all products, and returns them
def get_haircare_products():
    conn = sqlite3.connect('haircare.db')  # Connect to haircare.db
    cursor = conn.cursor()                 # Create a cursor to run SQL
    cursor.execute("SELECT * FROM haircare")  # SQL command to get all rows
    products = cursor.fetchall()           # Fetch all rows from the result
    conn.close()                           # Close the database connection
    return products                        # Return the list of products
