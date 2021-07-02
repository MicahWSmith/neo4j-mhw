from .models import get_search_results
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_armor', methods=['POST'])
def search_armor():
    armor = request.form['armor']
    rank = request.form['rank']

    results = get_search_results(armor)
    return render_template('search.html', results=results)