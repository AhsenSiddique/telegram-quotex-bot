from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def start_bot(api_id, api_hash, group_name):
    with TelegramClient('session', api_id, api_hash) as client:
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

        target_group = None
        for chat in chats:
            if chat.title == group_name:
                target_group = chat
                break

        if not target_group:
            print(f"Group '{group_name}' not found.")
            return

        print(f"Target group '{group_name}' found!")

        base_amount = 1
        trade_amount = base_amount
        martingale_step = 0
        max_martingale_steps = 2

        @client.on(events.NewMessage(chats=target_group))
        async def handler(event):
            nonlocal trade_amount, martingale_step

            message = event.message.message
            print(f"New message: {message}")

            # Example: Check if message contains trading signals (adjust as needed)
            if "CALL" in message or "PUT" in message:
                # Placeholder for real trade result: here we randomly simulate win/loss
                import random
                trade_win = random.choice([True, False])

                if trade_win:
                    print(f"Trade WON with amount {trade_amount}")
                    trade_amount = base_amount
                    martingale_step = 0
                else:
                    print(f"Trade LOST with amount {trade_amount}")
                    if martingale_step < max_martingale_steps:
                        martingale_step += 1
                        trade_amount = base_amount * (2 ** martingale_step)
                    else:
                        print("Max Martingale steps reached, resetting.")
                        trade_amount = base_amount
                        martingale_step = 0

                print(f"Next trade amount: {trade_amount}")

        print("Starting client...")
        client.run_until_disconnected()
