from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def start_bot(api_id, api_hash, group_name):
    # Will prompt for phone number on Render console
    with TelegramClient('session', api_id, api_hash) as client:
        # Get dialog list
        chats = []
        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        # Find your target group
        target_group = None
        for chat in chats:
            if chat.title == group_name:
                target_group = chat
                break

        if not target_group:
            print("❌ Group not found!")
            return

        print(f"✅ Listening to: {group_name}")

        @client.on(events.NewMessage(chats=target_group))
        async def handler(event):
            message = event.message.message
            print(f"New signal: {message}")
            # Add your logic here to parse message & send to Quotex bot

        client.run_until_disconnected()
