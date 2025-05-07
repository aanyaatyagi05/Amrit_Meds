from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amritmeds.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
admin = Admin(app, name='Amrit Admin', template_mode='bootstrap3')

# Define a simple product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.String(50))

# Add the model to admin
admin.add_view(ModelView(Product, db.session))

if __name__ == '__main__':
    db.create_all()  # Run this once to create the DB
    app.run(debug=True)
@app.route('/cart')
def cart():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT cart.id AS cart_id, products.name, products.price, products.image_url, cart.quantity
        FROM cart JOIN products ON cart.product_id = products.id
        WHERE cart.user_id = 1
    """)
    cart_items = cursor.fetchall()
    cursor.close()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/wishlist')
def wishlist():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT wishlist.id AS wishlist_id, products.name, products.price, products.image_url
        FROM wishlist JOIN products ON wishlist.product_id = products.id
        WHERE wishlist.user_id = 1
    """)
    wishlist_items = cursor.fetchall()
    cursor.close()
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
def remove_from_cart(cart_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM cart WHERE id = %s", (cart_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('cart'))

@app.route('/remove_from_wishlist/<int:wishlist_id>', methods=['POST'])
def remove_from_wishlist(wishlist_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM wishlist WHERE id = %s", (wishlist_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('wishlist'))
