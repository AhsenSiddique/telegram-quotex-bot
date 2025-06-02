from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def start_bot(api_id, api_hash, group_name):
    # Use the saved 'session.session' file by naming it 'session'
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

        # You can add code here to find the target group by name or id
        # and process messages or send trades with Martingale logic

        print(f"Found {len(chats)} chats.")

        # Example: find group by name
        target_group = None
        for chat in chats:
            if chat.title == group_name:
                target_group = chat
                break
        
        if target_group:
            print(f"Target group '{group_name}' found!")
            # Here you can add more code to listen for messages and handle trades
        else:
            print(f"Group '{group_name}' not found.")
