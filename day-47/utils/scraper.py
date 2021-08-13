import requests
from bs4 import BeautifulSoup

class Scraper:
    """
    Class for scraping stuff
    """
    def __init__(self, url, target):
        self.url = url
        self.target_price = float(target)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Accept-Language': 'en',
            }
        self.soup_object = self.scrape_page()
        self.price = self.find_amz_price()

    def scrape_page(self):
        """
        Given a URL to scrap
        Return the soup object
        """
        response = requests.get(url=self.url, headers=self.headers)
        return BeautifulSoup(response.text, 'html.parser')

    def find_amz_price(self):
        """
        Given a soup object
        Find the price
        """
        price = self.soup_object.find(id="priceblock_ourprice").get_text().split("$")[1]
        return float(price)
        
    def compare_prices(self):
        """
        Compare discovered price and target price
        If discovered price is lower return True
        """
        if self.target_price >= self.price:
            return True
