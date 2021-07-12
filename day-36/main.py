from utils.stocks import check_change
from utils.news import get_news

def main():
    stocks = ['AAPL', 'DIS', 'NTDOY']

    for stock in stocks:
        if check_change(stock):
            get_news(stock)


if __name__ == '__main__':
    main()
