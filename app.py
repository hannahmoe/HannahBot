import os
from flask import Flask, request, jsonify

app = Flask(__name__)


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

    # အခုအဆင့်မှာ message ကို လက်ခံပြီး log ထုတ်ရုံပဲလုပ်မယ်။
    # Token အသစ်ရပြီးမှ Viber reply API ထည့်မယ်။
    return jsonify({"status": "ok"}), 200
