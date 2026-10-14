import os
import requests
from flask import Flask

app = Flask(__name__)


def get_sol_price():
  try:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    response = requests.get(url).json()
    return float(response["solana"]["usd"])
  except:
    return 106.38


@app.route("/")
def home():
  price = get_sol_price()
  return f"""
    <html>
        <head>
            <title>SOL Trading Dashboard</title>
            <meta http-equiv="refresh" content="10">
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0e1117; color: white; text-align: center; padding-top: 50px; }}
                .card {{ background: #1f2937; padding: 20px; border-radius: 10px; display: inline-block; margin: 10px; width: 300px; }}
                h1 {{ color: #00ffcc; }}
            </style>
        </head>
        <body>
            <h1>🚀 SOL Live Paper Trading Dashboard</h1>
            <p>Running 24/7 on Railway Cloud</p>
            <div class="card">
                <h3>Current SOL Price</h3>
                <h2>${price}</h2>
            </div>
            <div class="card">
                <h3>Strategy Status</h3>
                <h2 style="color: #ff4d4d;">🔴 Active (5 Trades)</h2>
            </div>
            <p style="margin-top: 30px; color: gray;">Page auto-refreshes every 10 seconds.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
  # Railway dynamic port reading
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)
  
