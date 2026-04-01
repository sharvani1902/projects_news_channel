from flask import Flask, render_template
from fetch_news import get_live_news

app = Flask(__name__)

@app.route("/")
def home():
    news = get_live_news()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)