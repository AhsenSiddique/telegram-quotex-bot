from telethon import TelegramClient, events, sync

def start_bot(api_id, api_hash, group_name, *args):
    print("Starting Telegram client...")

    client = TelegramClient('session_name', int(api_id), api_hash)
    client.start()
    print(f"Connected to Telegram as {client.get_me().username}")

    @client.on(events.NewMessage(chats=group_name))
    async def handler(event):
        msg = event.message.message
        print(f"New message in {group_name}: {msg}")

    print(f"Listening to messages in {group_name}...")
    client.run_until_disconnected()
