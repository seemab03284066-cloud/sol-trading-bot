import time
import requests
import telebot

# Tumhara Telegram Bot Token aur Username Chat ID
TOKEN = "8958594212:AAEjgJjFfrzsJCsFlviwEGXRuvlQB9YdqhU"
CHAT_ID = "@Seemabkhan01"

bot = telebot.TeleBot(TOKEN)


def get_sol_price():
  try:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    response = requests.get(url).json()
    price = response["solana"]["usd"]
    return float(price)
  except Exception as e:
    print(f"Error fetching price: {e}")
    return None


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "🤖 Solana Trading Bot is active and running 24/7 on the cloud! 🚀",
  )


def start_trading():
  try:
    bot.send_message(
        CHAT_ID,
        "🟢 SOL Trading Bot deployed successfully and monitoring market gaps"
        " (0.10%)...",
    )
  except Exception as e:
    print(f"Init message error: {e}")

  last_price = get_sol_price()
  if not last_price:
    last_price = 150.0  # Fallback base price

  while True:
    current_price = get_sol_price()
    if current_price:
      price_diff_pct = abs(current_price - last_price) / last_price * 100

      if price_diff_pct >= 0.10:
        signal_type = (
            "LONG (BUY)" if current_price > last_price else "SHORT (SELL)"
        )
        msg = (
            f"📊 **Market Gap Signal Detected!**\n\nAsset: SOL/USDT\nAction:"
            f" {signal_type}\nPrice: ${current_price}\nPrevious:"
            f" ${last_price}\nChange: {price_diff_pct:.2f}%\nRisk-to-Reward:"
            " 1:2"
        )
        try:
          bot.send_message(CHAT_ID, msg, parse_mode="Markdown")
        except Exception as e:
          print(f"Signal send error: {e}")
        last_price = current_price

    time.sleep(30)


if __name__ == "__main__":
  print("Bot is starting...")
  try:
    bot.send_message(CHAT_ID, "🚀 Bot container started on Railway cloud!")
  except Exception as e:
    print(f"Startup message error: {e}")

  # Bot polling start karne ke liye
  bot.infinity_polling()
      
