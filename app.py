
from flask import Flask, request, render_template
from your_bot_module import start_bot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        telegram_api_id = request.form['telegram_api_id']
        telegram_api_hash = request.form['telegram_api_hash']
        telegram_group = request.form['telegram_group']
        quotex_email = request.form['quotex_email']
        quotex_password = request.form['quotex_password']
        trade_amount = request.form['trade_amount']
        account_type = request.form['account_type']

        start_bot(telegram_api_id, telegram_api_hash, telegram_group, quotex_email, quotex_password, trade_amount, account_type)
        return 'Bot Started! Check your Telegram & Quotex.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
