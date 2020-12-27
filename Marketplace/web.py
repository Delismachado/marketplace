from flask import Flask, render_template
from catalogo import Marketplace, Category, Subcategory

app = Flask(__name__)

marketplaces = [Marketplace('Enjoei'), Marketplace('BigCommerce'), Marketplace('Etsy'), Marketplace('Evolutto'), Marketplace('Arb')]
categories = [Category('Home', marketplaces[0]), Category('Dinner', marketplaces[1]), Category('Food', marketplaces[2])]
subcategories = [Subcategory('Lunch', categories[0]), Subcategory('Style', categories[1]), Subcategory('Go', categories[2])]

@app.route('/')
def index():
    return render_template('index.html', marketplaces = marketplaces)

@app.route('/category/<mkt>')
def category(mkt):
    return render_template('category.html', cat = categories, mkt = mkt)

@app.route('/subcategories/<cat>')
def subcategory(cat):
    return render_template('subcategories.html', subcat = subcategories, cat = cat)



app.run(debug=True)