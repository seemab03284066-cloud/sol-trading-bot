import os
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
  try:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    response = requests.get(url).json()
    price = response["solana"]["usd"]
  except:
    price = 106.38

  return f"""
    <html>
        <body style="background-color: #0e1117; color: white; text-align: center; font-family: Arial; padding-top: 50px;">
            <h1>🚀 SOL Live Paper Trading Dashboard</h1>
            <h2>Current SOL Price: ${price}</h2>
            <h3 style="color: #ff4d4d;">Status: Active (5 Trades Running)</h3>
        </body>
    </html>
    """


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)
  
