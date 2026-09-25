from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env (if present)
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

app = Flask(__name__)

@app.route('/api/compare', methods=['POST'])
def compare_prices():
    """Accept a product query and return placeholder price data.
    The real implementation will call external e‑commerce APIs or scrapers.
    """
    data = request.get_json() or {}
    product = data.get('product', '')

    # Placeholder results – replace with real data fetching logic later.
    results = [
        {"platform": "Amazon",   "price": "N/A", "url": ""},
        {"platform": "Flipkart", "price": "N/A", "url": ""},
        {"platform": "Meesho",   "price": "N/A", "url": ""},
        {"platform": "Snapdeal", "price": "N/A", "url": ""},
    ]
    return jsonify({"product": product, "results": results})

if __name__ == '__main__':
    # Running in development mode makes debugging easier.
    # Host 0.0.0.0 allows access from the frontend served separately.
    app.run(host='0.0.0.0', port=5000, debug=True)
