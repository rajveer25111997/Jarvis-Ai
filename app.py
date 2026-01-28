from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # CoinGecko Trending API
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = response.json()
    
    # सिर्फ सिक्कों (coins) का डेटा निकाल रहे हैं
    trending_coins = data.get('coins', [])
    
    return render_template('index.html', coins=trending_coins)

if __name__ == '__main__':
    app.run(debug=True)
