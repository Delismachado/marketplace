from flask import Flask


app = Flask(__name__)

@app.route('/')

def home():
  h1 = '<h1>List all marketplaces</h1>'
  