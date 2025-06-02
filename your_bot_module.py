from telethon import events

def start_bot(api_id, api_hash, group_name):
    with TelegramClient('session', api_id, api_hash) as client:
        # Find the target group
        chats = client.get_dialogs()
        target_group = None
        for chat in chats:
            if chat.title == group_name:
                target_group = chat
                break
        
        if not target_group:
            print(f"Group '{group_name}' not found!")
            return
        
        print(f"Listening to group '{group_name}'...")

        # Event handler for new messages in target group
        @client.on(events.NewMessage(chats=target_group.id))
        async def handler(event):
            message = event.raw_text
            print("New message:", message)
            # Here you will parse the signal and run trade logic (next step)

        client.run_until_disconnected()
