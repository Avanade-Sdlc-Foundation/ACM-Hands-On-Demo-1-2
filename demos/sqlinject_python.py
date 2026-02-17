# -*- coding: utf-8 -*-
"""
SQL Injection Vulnerability Demo - Python Edition
Using Flask + SQLite
"""

import sqlite3
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Database setup
def setup_db():
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                     (id INTEGER PRIMARY KEY, name TEXT, costprice REAL, category TEXT)''')
    
    # Delete existing data
    cursor.execute("DELETE FROM products")
    
    # Insert sample data
    products = [
        (1, 'Apple', 0.50, 'Fruit'),
        (2, 'Banana', 0.30, 'Fruit'),
        (3, 'Carrot', 0.20, 'Vegetable'),
        (4, 'Date', 1.00, 'Fruit'),
        (5, 'Eggplant', 0.80, 'Vegetable'),
        (6, 'Fig', 1.20, 'Fruit'),
        (7, 'Grape', 0.90, 'Fruit'),
        (8, 'Honeydew', 2.00, 'Fruit'),
        (9, 'Iceberg Lettuce', 0.60, 'Vegetable'),
        (10, 'Jackfruit', 3.00, 'Fruit'),
        (11, 'Kiwi', 0.70, 'Fruit'),
        (12, 'Lemon', 0.40, 'Fruit'),
        (13, 'Mango', 1.50, 'Fruit'),
        (14, 'Nectarine', 1.10, 'Fruit'),
        (15, 'Orange', 0.60, 'Fruit'),
        (16, 'Papaya', 1.80, 'Fruit'),
        (17, 'Quince', 1.40, 'Fruit'),
        (18, 'Raspberry', 2.50, 'Fruit'),
        (19, 'Strawberry', 2.00, 'Fruit'),
        (20, 'Tomato', 0.50, 'Vegetable'),
        (21, 'Ugli Fruit', 2.20, 'Fruit'),
        (22, 'Vanilla Bean', 5.00, 'Spice'),
        (23, 'Watermelon', 3.50, 'Fruit'),
        (24, 'Xigua', 3.00, 'Fruit'),
        (25, 'Yam', 0.70, 'Vegetable'),
        (26, 'Zucchini', 0.60, 'Vegetable'),
        (27, 'Pineapple', 2.00, 'Fruit'),
        (28, 'Cucumber', 0.40, 'Vegetable'),
        (29, 'Peach', 1.20, 'Fruit'),
        (30, 'Pear', 1.00, 'Fruit'),
        (31, 'Plum', 0.90, 'Fruit'),
        (32, 'Apricot', 1.10, 'Fruit'),
        (33, 'Blackberry', 2.20, 'Fruit'),
        (34, 'Cantaloupe', 2.00, 'Fruit'),
        (35, 'Dragonfruit', 3.00, 'Fruit'),
        (36, 'Elderberry', 2.50, 'Fruit'),
        (37, 'Gooseberry', 2.00, 'Fruit'),
        (38, 'Lychee', 2.00, 'Fruit'),
        (39, 'Mulberry', 2.00, 'Fruit'),
        (40, 'Passionfruit', 2.50, 'Fruit'),
        (41, 'Starfruit', 2.20, 'Fruit')
    ]
    
    cursor.executemany("INSERT INTO products (id, name, costprice, category) VALUES (?, ?, ?, ?)", products)
    conn.commit()
    conn.close()

# Vulnerable search endpoint (SQL Injection target)
@app.route('/search')
def search():
    product_name = request.args.get('name', '')
    
    # VULNERABLE SQL query (DO NOT USE IN PRODUCTION!)
    query = f"SELECT * FROM products WHERE name LIKE '%{product_name}%'"
    
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Get results as dictionaries
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        
        # Convert results to list of dictionaries
        products = [dict(row) for row in results]
        return jsonify({'products': products})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return """
    <h1>SQL Injection Vulnerability Demo - Python Edition</h1>
    <h2>Usage:</h2>
    <ul>
        <li>Normal search: <a href="/search?name=Apple">/search?name=Apple</a></li>
        <li>SQL Injection attack: <a href="/search?name=' OR 1=1 --">/search?name=' OR 1=1 --</a></li>
    </ul>
    <p><strong>Warning:</strong> This is for demonstration purposes only. Never use such code in production!</p>
    """

if __name__ == '__main__':
    print("Setting up database...")
    setup_db()
    print("Starting server...")
    app.run(host='127.0.0.1', port=8080, debug=True)