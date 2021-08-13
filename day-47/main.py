from utils.alert import Notify
from utils.scraper import Scraper

def main():
    url = 'https://www.amazon.com/dp/B001I8ZTJ0/'
    amz = Scraper(url, 330)
    if amz.compare_prices:
        mail = Notify()
        mail.send_email('example@test.com', 'Amazon Price Alert', f'Item on sale. Link: {url}')

if __name__ == '__main__':
    main()
