#!/usr/bin/python3
"""Flask app displaying product data from JSON or CSV files."""
import csv
import json
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
    else:
        return render_template('product_display.html', error="Wrong source")

    try:
        data = reader()
    except (OSError, ValueError, KeyError):
        return render_template('product_display.html',
                               error="Could not read data")

    if product_id is not None:
        data = [p for p in data if str(p.get('id')) == product_id]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
