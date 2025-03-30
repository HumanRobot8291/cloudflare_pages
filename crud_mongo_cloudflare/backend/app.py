import os
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Secure connection using environment variable
MONGO_URI = os.getenv("MONGO_URI", "your_fallback_mongo_uri_here")
client = MongoClient(MONGO_URI)
db = client.your_database_name
collection = db.your_collection_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Data added successfully!"})

@app.route('/get', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
