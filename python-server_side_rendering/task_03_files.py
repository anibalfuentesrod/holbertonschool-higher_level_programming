from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error_message = None
    products = []

    if source == 'json':
        try:
            data = read_json('products.json')
            products = data
        except Exception as e:
            error_message = f"Error reading JSON file: {e}"
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception as e:
            error_message = f"Error reading CSV file: {e}"
    else:
        error_message = "Wrong source. Please specify 'json' or 'csv'."

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if int(product['id']) == product_id]
            if not products:
                error_message = "Product not found."
        except ValueError:
            error_message = "Invalid product id."

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)