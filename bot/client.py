import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

def signed_request(method, endpoint, params):
    params["timestamp"] = int(time.time() * 1000)

    query = urlencode(params)

    signature = hmac.new(
        API_SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()

    url = f"{BASE_URL}{endpoint}?{query}&signature={signature}"

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.request(
        method,
        url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    return response.json()
