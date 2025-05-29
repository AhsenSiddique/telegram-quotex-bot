from flask import Flask, request, render_template
import threading
import your_bot_module

app = Flask(__name__)
bot_thread = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global bot_thread
    if request.method == 'POST':
        api_id = request.form['api_id']
        api_hash = request.form['api_hash']
        group_name = request.form['group_name']
        bot_token = request.form['bot_token']

        if bot_thread is None or not bot_thread.is_alive():
            bot_thread = threading.Thread(
                target=your_bot_module.start_bot,
                args=(api_id, api_hash, group_name, bot_token)
            )
            bot_thread.start()

        return "✅ Bot started successfully. Check Render logs for activity."

    return render_template('index.html')
