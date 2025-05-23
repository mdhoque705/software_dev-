
from flask import Flask, render_template, request, redirect, url_for, flash, session
import psycopg2
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = psycopg2.connect(
        dbname='project2DB',
        user='postgres',
        password='Taseen@123',
        host='localhost'
    )
    return conn


@app.route('/')
@app.route('/')
def home():
    # T-Shirts
    tshirts = [
        {'id': 1, 'name': 'Classic Tee', 'price': 15.99, 'image': 'tshirt1.webp'},
        {'id': 2, 'name': 'Logo Tee', 'price': 17.99, 'image': 'tshirt2.webp'},
        {'id': 3, 'name': 'Striped Tee', 'price': 18.99, 'image': 'tshirt3.webp'},
        {'id': 4, 'name': 'Pocket Tee', 'price': 16.49, 'image': 'tshirt4.webp'},
        {'id': 5, 'name': 'Graphic Tee', 'price': 19.99, 'image': 'tshirt5.webp'},
        {'id': 6, 'name': 'Oversized Tee', 'price': 20.00, 'image': 'tshirt6.webp'},
    ]

    # Hoodies
    hoodies = [
        {'id': 7, 'name': 'Basic Hoodie', 'price': 29.99, 'image': 'hoodie1.webp'},
        {'id': 8, 'name': 'Zipper Hoodie', 'price': 34.99, 'image': 'hoodie2.webp'},
        {'id': 9, 'name': 'Fleece Hoodie', 'price': 39.99, 'image': 'hoodie3.webp'},
        {'id': 10, 'name': 'Printed Hoodie', 'price': 31.99, 'image': 'hoodie4.webp'},
        {'id': 11, 'name': 'Pullover Hoodie', 'price': 27.99, 'image': 'hoodie5.webp'},
        {'id': 12, 'name': 'Colorblock Hoodie', 'price': 35.00, 'image': 'hoodie6.webp'},
    ]

    return render_template('home.html', tshirts=tshirts, hoodies=hoodies)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if cur.fetchone():
            flash('Username or email already exists')
            return redirect(url_for('register'))

        cur.execute("INSERT INTO users (first_name, last_name, username, password, email, address) VALUES (%s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, username, password, email, address))
        conn.commit()
        cur.close()
        conn.close()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session['user_id'] = user[0]
            flash('Login successful')
            return redirect(url_for('checkout'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash("You must be logged in to checkout.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        items = request.form['items']
        total_price = request.form['total']
        user_id = session['user_id']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (user_id, items, total_price) VALUES (%s, %s, %s)",
                    (user_id, items, total_price))
        conn.commit()
        cur.close()
        conn.close()

        order_number = random.randint(10000, 99999)
        return render_template('confirmation.html', order_number=order_number)

    return render_template('checkout.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
