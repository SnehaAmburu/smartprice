# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import re

# Load backend/.env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)
CORS(app)

from scraper import fetch_url


def extract_price(html: str) -> str:
    """Simple price extractor for basic testing."""
    patterns = [
        r"₹\s?[\d,]+(?:\.\d{1,2})?",
        r"\$\s?[\d,]+(?:\.\d{1,2})?",
    ]

    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(0)

    return "N/A"


@app.route("/")
def home():
    return jsonify({
        "message": "SmartPrice backend is running"
    })


@app.route("/api/compare", methods=["POST"])
def compare_prices():
    data = request.get_json() or {}

    query = data.get("product", "").strip()
    direct_url = data.get("url", "").strip()

    if direct_url:
        result = fetch_url(direct_url)

        if "error" in result:
            return jsonify({
                "error": f"ScraperAPI failed: {result['error']}"
            }), 502

        price = extract_price(result["content"])

        return jsonify({
            "product": query,
            "results": [
                {
                    "platform": "Custom",
                    "price": price,
                    "url": direct_url
                }
            ]
        })

    placeholder = [
        {"platform": "Amazon", "price": "N/A", "url": ""},
        {"platform": "Flipkart", "price": "N/A", "url": ""},
        {"platform": "Meesho", "price": "N/A", "url": ""},
        {"platform": "Snapdeal", "price": "N/A", "url": ""},
    ]

    return jsonify({
        "product": query,
        "results": placeholder
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "0") == "1"
    )