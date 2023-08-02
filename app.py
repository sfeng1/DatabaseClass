from flask import Flask, render_template, json
from flask_navigation import Navigation
import database.db_connector as db
import os

# Configuration

app = Flask(__name__)
nav = Navigation(app)
db_connection = db.connect_to_database()

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
    query = "SELECT * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("customers.j2", customers=results)

@app.route('/campaigns')
def campaigns():
    query = "SELECT * FROM Campaigns;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("campaigns.j2", campaigns = results)

@app.route('/channels')
def channels():
    query = "SELECT * FROM Channels;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("channels.j2",channels = results)

@app.route('/inventory')
def inventory():
    query = "SELECT * FROM Inventory;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("inventory.j2", inventory=results)

@app.route('/products')
def products():
    query = "SELECT * FROM Products;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("products.j2", products=results)

@app.route('/saleItems')
def saleItems():
    query = "SELECT * FROM SaleItems;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("saleItems.j2", saleItems= results)

@app.route('/sales')
def sales():
    query = "SELECT * FROM Sales;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("sales.j2", sales = results)
# Listener


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9853)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 