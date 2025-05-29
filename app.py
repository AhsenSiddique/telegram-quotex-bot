from flask import Flask, render_template, request
from your_bot_module import start_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            api_id = int(request.form["api_id"])
            api_hash = request.form["api_hash"]
            group_name = request.form["group_name"]

            start_bot(api_id, api_hash, group_name)
            return "✅ Bot Started Successfully! Please check your Telegram for login confirmation."
        except Exception as e:
            return f"❌ Error: {str(e)}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
