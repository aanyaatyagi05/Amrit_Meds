from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Medicine Search
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('medicines.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicines WHERE name LIKE ?", ('%' + query + '%',))
    results = cur.fetchall()
    conn.close()

    if not results:
        return render_template('no_results.html', query=query)
    return render_template('medicine.html', medicines=results)

# Option 1: Hardcoded haircare data
@app.route('/haircare')
def haircare():
    haircare_products = [
        {
            "name": "Minoxidil 5%", "category": "Hair Growth",
            "description": "Treats hair loss and promotes regrowth",
            "price": 550, "quantity": "60ml",
            "usage": "Apply to scalp twice daily",
            "company": "Dr. Reddy's",
            "image": "minoxidil.jpg"
        },
        {
            "name": "Anaboom Shampoo", "category": "Shampoo",
            "description": "Anti-hair fall and scalp care formula",
            "price": 380, "quantity": "100ml",
            "usage": "Use thrice a week",
            "company": "Sun Pharma",
            "image": "anaboom.jpg"
        },
        {
            "name": "Triclenz Shampoo", "category": "Shampoo",
            "description": "Dermatologist-recommended for hair and scalp cleansing",
            "price": 410, "quantity": "100ml",
            "usage": "Use every alternate day",
            "company": "Curatio",
            "image": "triclenz.jpg"
        },
        {
            "name": "Hairbless Tablets", "category": "Supplement",
            "description": "Strengthens hair from the root, rich in biotin",
            "price": 630, "quantity": "30 tablets",
            "usage": "One tablet daily after food",
            "company": "Ajanta Pharma",
            "image": "hairbless.jpg"
        },
        {
            "name": "Sebamed Anti-Hairloss Shampoo", "category": "Shampoo",
            "description": "Gentle shampoo with pH 5.5 to reduce hair fall",
            "price": 480, "quantity": "200ml",
            "usage": "Use twice a week",
            "company": "Sebamed",
            "image": "sebamed.jpg"
        },
        {
            "name": "Baidyanath Mahabhringraj Oil", "category": "Hair Oil",
            "description": "Ayurvedic oil for strong, black hair",
            "price": 180, "quantity": "200ml",
            "usage": "Massage into scalp before bedtime",
            "company": "Baidyanath",
            "image": "mahabhringraj.jpg"
        },
        {
            "name": "Indulekha Bringha Oil", "category": "Hair Oil",
            "description": "Ayurvedic proprietary medicine for hair fall",
            "price": 430, "quantity": "100ml",
            "usage": "Apply directly to scalp and leave overnight",
            "company": "Hindustan Unilever",
            "image": "indulekha.jpg"
        }
    ]
    return render_template('haircare.html', products=haircare_products)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)