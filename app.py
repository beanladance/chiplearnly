from flask import Flask, render_template, request, jsonify, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/baitap')
def baitap():
    return render_template('baitap.html')

if __name__ == '__main__':
    app.run(debug=True)