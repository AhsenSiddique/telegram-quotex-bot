from telethon.sync import TelegramClient, events
from datetime import datetime
import re
import time

# Martingale config
BASE_AMOUNT = 500
MAX_GALES = 2

# Global trade tracking
open_trades = {}

def parse_signal(message):
    # Expected format: NZD/CHF;02:25;PUT
    try:
        parts = message.split(";")
        asset = parts[0].strip()
        time_str = parts[1].strip()
        direction = parts[2].strip().upper()
        return asset, time_str, direction
    except:
        return None

def place_trade(asset, direction, amount, step):
    print(f"[{datetime.now()}] Trade placed | Step {step} | {asset} | {direction} | Amount: R{amount}")

def start_bot(api_id, api_hash, group_name):
    client = TelegramClient("session", api_id, api_hash)

    @client.on(events.NewMessage)
    async def handler(event):
        if event.is_group:
            chat = await event.get_chat()
            if chat.title == group_name:
                text = event.message.message
                signal = parse_signal(text)
                if signal:
                    asset, time_str, direction = signal
                    print(f"[{datetime.now()}] Signal: {asset} at {time_str} as {direction}")
                    
                    # Reset Martingale
                    for step in range(MAX_GALES + 1):
                        amount = BASE_AMOUNT * (2 ** step)
                        place_trade(asset, direction, amount, step + 1)
                        time.sleep(2)  # Simulated wait
                        # In real bot, check result before next gale
                        if step < MAX_GALES:
                            print(f"➡️ Gale {step + 1} activated.")
                        else:
                            print("✅ Done. Restarting with base amount.")

    client.start()
    print("✅ Bot is live and listening for signals...")
    client.run_until_disconnected()
