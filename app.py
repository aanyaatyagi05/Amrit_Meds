from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors  # for dictionary cursor
import traceback        # for debugging errors

app = Flask(__name__)

# -----------------------------
# MySQL Configuration
# -----------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aanyat020'
app.config['MYSQL_DB'] = 'amrit_meds'

mysql = MySQL(app)

# -----------------------------
# Routes
# -----------------------------

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/haircare')
def haircare():
    return render_template('haircare.html')


@app.route('/skincare')
def skincare():
    return render_template('skincare.html')


@app.route('/sexual-wellness')
def sexual_wellness():
    return render_template('sexual-wellness.html')


@app.route('/medicines')
def show_medicines():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM medicine_products")
    data = cur.fetchall()
    cur.close()
    return render_template('medicines.html', medicines=data)


@app.route('/babysection')
def babysection():
    return render_template('babysection.html')


# -----------------------------
# Search Route (Fixed)
# -----------------------------
@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('query', '').strip()
    results = []

    if search_query:
        try:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            query = """
                SELECT id, image_path, name, price, quantity, description, dosage, company
                FROM medicine_products
                WHERE name LIKE %s
            """
            cur.execute(query, (f"%{search_query}%",))
            results = cur.fetchall()
            cur.close()
        except Exception as e:
            print("Error during search:", e)
            traceback.print_exc()

    return render_template('results.html', query=search_query, results=results)


# -----------------------------
# Cart and Wishlist (Dummy)
# -----------------------------
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    return f"Product {product_id} added to cart!"


@app.route('/add_to_wishlist/<int:product_id>', methods=['POST'])
def add_to_wishlist(product_id):
    return f"Product {product_id} added to wishlist!"


# -----------------------------
# Run the App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)

