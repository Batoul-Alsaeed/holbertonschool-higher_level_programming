from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        error = "Wrong source"

    if not error and product_id:
        data = [item for item in data if str(item.get('id')) == str(product_id)]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
