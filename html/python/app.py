from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
import requests

#environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontpagewebsite.html')
@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/get-api-key')
def get_api_key():
    api_key = os.getenv('MY_API_KEY')
    return jsonify(api_key=api_key)

@app.route('/get-news-api-key')
def get_news_api_key():
    news_api_key = os.getenv('NEWS_API_KEY')
    return jsonify(api_key=news_api_key)


def get_sustainability_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "sustainability",
        "apiKey": os.getenv('NEWS_API_KEY'),  
        "pageSize": 10  # 10 articles 
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get("articles", [])
    
    
    formatted_articles = []
    for article in articles:
        formatted_article = {
            "title": article.get("title", "Sustainability News"),
            "description": article.get("description", "Latest updates on sustainability."),
            "url": article.get("url", "#"),
            "urlToImage": article.get("urlToImage", "/api/placeholder/400/200")
        }
        formatted_articles.append(formatted_article)
    
    return formatted_articles

@app.route('/news')
def news_page():
    articles = get_sustainability_news()
    return render_template('news.html', articles=articles)

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

posts = [
    {
        "content": "Just planted 100 trees in the local park! 🌳 #GreenInitiative",
        "date": "2025-01-19",
        "author": "EcoWarrior",
        "likes": 42
    },
    {
        "content": "New solar panel installation completed today. Reducing carbon footprint one house at a time! ☀️ #Sustainability",
        "date": "2025-01-19",
        "author": "SolarPower",
        "likes": 38
    },
    {
        "content": "Beach cleanup event this weekend removed 500 lbs of plastic! 🌊 #SaveTheOceans",
        "date": "2025-01-18",
        "author": "OceanGuardian",
        "likes": 156
    }
]

@app.route('/branches')
def branches_page():
    #posts by date, newest first
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    return render_template('branches.html', posts=sorted_posts)

if __name__ == '__main__':
    app.run(debug=True)
