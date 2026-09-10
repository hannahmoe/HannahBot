import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

VIBER_TOKEN = os.getenv("VIBER_AUTH_TOKEN")
WEBHOOK_URL = "https://hannahbot-rihm.onrender.com/viber/webhook"


def register_webhook( ):
    if not VIBER_TOKEN:
        print("VIBER_AUTH_TOKEN မတွေ့ပါ")
        return

    headers = {
        "Content-Type": "application/json",
        "X-Viber-Auth-Token": VIBER_TOKEN
    }

    payload = {
        "url": WEBHOOK_URL,
        "event_types": [
            "message",
            "subscribed",
            "unsubscribed",
            "conversation_started"
        ],
        "send_name": True,
        "send_photo": False
    }

    try:
        response = requests.post(
            "https://chatapi.viber.com/pa/set_webhook",
            headers=headers,
            json=payload,
            timeout=20
         )

        print("Webhook registration status:", response.status_code)
        print("Webhook registration response:", response.text)

    except Exception as error:
        print("Webhook registration error:", str(error))


@app.get("/")
def home():
    return "Viber bot server is running", 200


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/viber/webhook")
def viber_webhook():
    data = request.get_json(silent=True) or {}

    print("Received Viber event:", data)

    return jsonify({"status": "ok"}), 200


register_webhook()
