from app import app
from app.modeles import Product
from flask import render_template, redirect, url_for
@app.route('/')
@app.route('/index')
def index():
    return render_template("layout.html.jinja")

@app.route('/products')
def products():
    pass

@app.route('/product/<product_id>')
def product(product_id):
    pass

@app.route('/author')
def author():
    pass

@app.route('/extract/<product_id>')
def extract(product_id):
    product = Product(product_id)
    product.extract_opinions().analyze().export_to_json()
    
    return render_template(extract.html.jinja, product_id=product_id)