import requests
import datetime as dt
import time
import yagmail

class News():
    def __init__(self, search_for='Apple', receiver="RECEIVER MAIL", news_amount=3, language='en', month=dt.datetime.now().month):
        self.search_for = search_for
        self.receiver = receiver
        self.news_amount = news_amount
        self.language = language
        self.month = month
        
        #example lngauge = "en" for english
        
    def send_news(self):

        NEWS_API_KEY = YOUR API KEY


        NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


        news_parameters = {
            "apiKey":NEWS_API_KEY,
            "language":self.language,
            "sortBy":"relevancy",
            "q":self.search_for,
            "searchIn":"title,description", 
        }

        response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)

        response_news.raise_for_status()

        news_data = response_news.json()

        if True:
            titles = []
            descriptions = []
            urls = []
            for _ in range(self.news_amount):
                titles.append(news_data["articles"][_]["title"])
                descriptions.append(news_data["articles"][_]["description"])
                urls.append(news_data["articles"][_]["url"])

        for _ in range(self.news_amount):
            sender = yagmail.SMTP(user="YOUR GMAIL", password="YOUR GMAIL API PASSWORD")
            sender.send(to=self.receiver, subject=f"{titles[_]}", contents=f"{descriptions[_]}\n\nURL: {urls[_]}")

