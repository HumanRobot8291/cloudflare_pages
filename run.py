import os

def create_file(path, content):
    """Helper function to create a file with content."""
    with open(path, "w") as f:
        f.write(content)

def main():
    project_name = "crud_mongo_cloudflare"
    os.makedirs(project_name, exist_ok=True)

    # Directories
    folders = [
        "backend", "frontend", "backend/templates", "backend/static/css",
        "backend/static/js", "backend/static/img"
    ]
    for folder in folders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)

    # Backend (Flask) Code
    backend_code = """from flask import Flask, request, render_template, jsonify
import pymongo
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Connect to MongoDB Atlas App Services (Stitch)
MONGO_URI = "YOUR_MONGO_DB_URI_HERE"
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
    data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB _id
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)"""
    create_file(os.path.join(project_name, "backend", "app.py"), backend_code)

    # Frontend (HTML + JS)
    frontend_html = """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>MongoDB CRUD</title>
    <script src='static/js/script.js' defer></script>
</head>
<body>
    <h2>MongoDB CRUD Form</h2>
    <label>Name:</label> <input type='text' id='name'><br>
    <label>Number:</label> <input type='text' id='number'><br>
    <label>Email:</label> <input type='text' id='email'><br>
    <label>Message:</label> <input type='text' id='message'><br>
    <button onclick='submitData()'>Submit</button>
    <button onclick='fetchData()'>Show Data</button>
    <h3>Verify Your Data</h3>
    <textarea id='dataDisplay' rows='10' cols='50'></textarea>
</body>
</html>"""
    create_file(os.path.join(project_name, "backend", "templates", "index.html"), frontend_html)

    frontend_js = """function submitData() {
    let data = {
        name: document.getElementById('name').value,
        number: document.getElementById('number').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };
    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => alert(data.message));
}

function fetchData() {
    fetch('/get').then(response => response.json()).then(data => {
        document.getElementById('dataDisplay').value = JSON.stringify(data, null, 2);
    });
}"""
    create_file(os.path.join(project_name, "backend", "static", "js", "script.js"), frontend_js)

    # Cloudflare Pages Deployment Guide
    instructions = """# Deployment Instructions

1. **MongoDB Atlas Setup**
   - Go to MongoDB Atlas and create a cluster.
   - Enable Atlas App Services (formerly Stitch) and create an API endpoint.
   - Replace `YOUR_MONGO_DB_URI_HERE` in `app.py` with your MongoDB URI.

2. **Run Locally**
   ```sh
   cd backend
   pip install flask pymongo flask_cors
   python app.py
   ```
   - Open `http://127.0.0.1:5000/` in a browser.

3. **Deploy to Cloudflare Pages**
   - Push your code to GitHub.
   - Connect your repo to Cloudflare Pages.
   - Set the build command as `python backend/app.py`.
   - Configure environment variables (MongoDB URI, etc.).
   - Deploy!"""
    create_file(os.path.join(project_name, "README.md"), instructions)

    print(f"Project '{project_name}' created successfully!")

if __name__ == "__main__":
    main()
