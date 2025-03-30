# Deployment Instructions

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
   - Deploy!