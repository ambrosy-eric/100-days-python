import requests
import os
from .tools import send_sms

def get_news(stock):
    """
    Given a stock symbol
    Return the first 3 news items for it
    """
    url = "https://newsapi.org/v2/everything"
    token = os.environ.get('NEWS_TOKEN')
    params = {'q': stock, 'apiKey': token}

    response = requests.get(url, params)
    print(response)
    if response.status_code == 200:
        articles = response.json()['articles']
        most_recent_articles = articles[:3]
        messages = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in most_recent_articles]
        for message in messages:
            send_sms(message, os.environ.get('TEST_NUMBER'))
