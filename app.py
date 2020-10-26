from flask import Flask, render_template, redirect, Response, jsonify
from flask_pymongo import PyMongo
import json


# Create an instance of Flask
app = Flask(__name__, static_url_path='', static_folder='static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/crime_db"
# Web Hosted MongoDB
# app.config["MONGO_URI"] = "mongodb+srv://admin:project2@cluster0.tbfxy.mongodb.net/earthquake_db?retryWrites=true&w=majority"
mongo = PyMongo(app)
crime = mongo.db.crime
earthquake.drop()
with open('file1.json') as f:
    data = json.load(f)
    for row in data:
        crime.insert_one(row)
        