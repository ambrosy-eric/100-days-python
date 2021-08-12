import requests
from bs4 import BeautifulSoup

class MusicScraping:
    """
    Class to facilitate scraping billboard top 100 for a give week
    """
    def __init__(self):
        self.week = None
        self.url = self._set_url()
        self.year = self.week.split('-')[0]

    def _set_week(self):
        """
        Prompt the user to imput a week
        """
        date = input('What date would you like to travel to? Dates should be in YYYY-MM-DD format. ')
        self.week = date

    def _set_url(self):
        """
        Set up url
        """
        base_url = f'https://www.billboard.com/charts/hot-100/'
        self._set_week()
        return base_url+self.week

    def get_top_100(self):
        """
        For a given week
        Return the top 100 song titles
        """
        top_100 = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
        top_100 = [title.getText() for title in titles]
        return top_100
