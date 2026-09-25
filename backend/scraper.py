# backend/scraper.py
import os
import requests
from urllib.parse import urlencode

SCRAPERAPI_KEY = os.getenv("SCRAPERAPI_KEY")
if not SCRAPERAPI_KEY:
    raise RuntimeError("SCRAPERAPI_KEY missing – set it in backend/.env")

def fetch_url(url: str, params: dict | None = None) -> dict:
    """
    Calls ScraperAPI and returns a dict:
        {"status_code": int, "content": str}   on success
        {"status_code": int|None, "error": str} on failure
    """
    query = {"api_key": SCRAPERAPI_KEY, "url": url, "render": "true"}
    if params:
        # Append query parameters to the target URL
        from urllib.parse import urlencode as uq
        target = f"{url}?{uq(params)}"
        query["url"] = target

    scraper_url = f"https://api.scraperapi.com/?{urlencode(query)}"
    try:
        resp = requests.get(scraper_url, timeout=30)
        resp.raise_for_status()
        return {"status_code": resp.status_code, "content": resp.text}
    except requests.RequestException as exc:
        return {"status_code": getattr(exc.response, "status_code", None),
                "error": str(exc)}