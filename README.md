# SmartPrice 🚀

**SmartPrice** is a simple online price comparison web application that demonstrates how to compare product prices across major e‑commerce platforms (Amazon, Flipkart, Meesho, Snapdeal).  It is built with a clear separation of concerns:

- **Frontend** – pure HTML, CSS and JavaScript.
- **Backend** – a lightweight Python Flask API.

The repository is structured to be **GitHub‑friendly** and easy for any developer (especially a college project) to clone, understand, modify, and extend.

---

## 📁 Folder Structure
```
smartshoppingproject/
├─ backend/                # Flask application
│   ├─ app.py             # Entry point & API routes
│   ├─ requirements.txt   # Python dependencies
│   ├─ .env.example       # Example environment variables (API keys)
│   └─ ...                # Future modules (scrapers, services)
├─ frontend/               # Static web UI
│   ├─ index.html         # Main page
│   ├─ style.css          # Styling
│   └─ app.js             # UI logic & API calls
├─ .gitignore             # Files/Folders to ignore in Git
└─ README.md              # You are reading it!
```

---

## 🛠️ Setup & Run
### Prerequisites
- **Python 3.9+** (for the backend)
- **Node.js** is **not** required – the frontend is plain static files.
- **Git** to clone the repo.

### 1️⃣ Clone the repository
```bash
git clone <repo‑url>
cd smartshoppingproject
```

### 2️⃣ Backend setup
```bash
# (optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Create a real .env based on the example (add your own API keys later)
cp backend/.env.example backend/.env   # Windows: copy
# Edit backend/.env and fill in any required keys.
```

### 3️⃣ Run the Flask API
```bash
python backend/app.py
```
The API will be available at `http://127.0.0.1:5000/api/compare`.

### 4️⃣ Open the Frontend
Simply open `frontend/index.html` in a browser (or serve the folder with any static server if you prefer). The UI will send a request to the running Flask server and display the (currently placeholder) price data.

---

## 📦 Extending SmartPrice
The project is deliberately minimal so you can add real data sources later:
1. **Implement scrapers or third‑party APIs** inside the `backend/` folder.
2. **Add environment variables** for required API keys in `.env.example` and read them with `python‑dotenv`.
3. **Expand the frontend** with more sophisticated UI components or a framework of your choice.
4. **Write tests** – the codebase is simple enough to add unit tests for the Flask routes.

---

## 🔐 Security Note
Never commit real API keys. Use the `.env.example` as a template and keep the actual `.env` file out of version control (it is listed in `.gitignore`).

---

## 📜 License
This starter project is released under the MIT License – feel free to use, modify, and share.
