from telethon import TelegramClient, events

def start_bot(api_id, api_hash, group_name, bot_token):
    print("▶️ Connecting with bot token...")

    client = TelegramClient('session', int(api_id), api_hash)
    client.start(bot_token=bot_token)
    print("✅ Bot connected!")

    @client.on(events.NewMessage(chats=group_name))
    async def handler(event):
        msg = event.message.message
        print(f"[{group_name}] {msg}")

        # Here you would add Martingale logic (if needed)

    print(f"📡 Listening for messages in '{group_name}'...")
    client.run_until_disconnected()
