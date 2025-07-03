from flask import Flask, render_template
from scraper import scrape_mock_market_data


app = Flask(__name__)

@app.route("/")
def home():
    data = scrape_mock_market_data()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
