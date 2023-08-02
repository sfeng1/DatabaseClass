from flask import Flask, render_template
from flask_navigation import Navigation
import os

# Configuration

app = Flask(__name__)
nav = Navigation(app)


#initializing Navigations
nav.Bar('top',[
    nav.Item('index','index'),
    nav.Item('customers','customers'),
    nav.Item('campaigns','campaigns'),
    nav.Item('channels','channels'),
    nav.Item('inventory','inventory'),
    nav.Item('products','products'),
    nav.Item('sales','sales'),
    nav.Item('saleItem','saleItem')
])

# Routes 

@app.route('/')
def index():
    return render_template("index.j2")

@app.route('/customers')
def customers():
    return render_template("customers.j2")

@app.route('/campaigns')
def campaigns():
    return render_template("campaigns.j2")

@app.route('/channels')
def channels():
    return render_template("channels.j2")

@app.route('/inventory')
def inventory():
    return render_template("inventory.j2")

@app.route('/products')
def products():
    return render_template("products.j2")

@app.route('/saleItems')
def saleItems():
    return render_template("saleItems.j2")

@app.route('/sales')
def sales():
    return render_template("sales.j2")
# Listener


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9853)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 