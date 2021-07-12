import requests
import os

def check_change(stock):
    """
    Given a stock
    Check to see what's its change has been
    If >5% in either direction
    Return True
    """
    url = "https://www.alphavantage.co/query"
    token = os.environ.get('ALPHA_VANTAGE_KEY')
    params = {'function': 'TIME_SERIES_DAILY', 'symbol': stock, 'apikey':token}
    response = requests.get(url, params)

    if response.status_code == 200:
        if not 'Error Message' in response.json().keys():
            data = response.json()['Time Series (Daily)']
            data_list = [v for k, v in data.items()]
            yesterday_close = float(data_list[0]['4. close'])
            day_null = float(data_list[1]['4. close'])
            change = _compare_prices(yesterday_close, day_null)
            if change < -5 or change > 5:
                print('changed')
                return True      
    else:
        response.raise_for_status()


def _compare_prices(price1, price2):
    """
    Compare the prices of 2 items
    Retun the percentage changed
    """
    return (price1 - price2)/price2
