#!/usr/bin/python3
"""Flask app displaying product data from JSON, CSV or SQLite."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename='products.json'):
    """Return the list of products from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)


def read_csv(filename='products.csv'):
    """Return the list of products from a CSV file."""
    products = []
    with open(filename, 'r', newline='') as f:
        for row in csv.DictReader(f):
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql(filename='products.db'):
    """Return the list of products from a SQLite database."""
    conn = sqlite3.connect(filename)
    try:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            'SELECT id, name, category, price FROM Products').fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def create_database(filename='products.db'):
    """Create and populate the Products table if needed."""
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        item_list = data.get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        reader = read_json
    elif source == 'csv':
        reader = read_csv
    elif source == 'sql':
        reader = read_sql
    else:
        return render_template('product_display.html', error="Wrong source")

    try:
        data = reader()
    except (OSError, ValueError, KeyError, sqlite3.Error):
        return render_template('product_display.html',
                               error="Could not read data")

    if product_id is not None:
        data = [p for p in data if str(p.get('id')) == product_id]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
