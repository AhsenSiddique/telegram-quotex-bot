from flask import Flask, render_template, request
from your_bot_module import start_bot
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            api_id = int(request.form["api_id"])
            api_hash = request.form["api_hash"]
            group_name = request.form["group_name"]

            t = threading.Thread(target=start_bot, args=(api_id, api_hash, group_name))
            t.daemon = True
            t.start()

            return "✅ Bot Started Successfully!"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
