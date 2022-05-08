import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

dizi = []


def balance_3():
    msft = yf.Ticker("msft")
    # msft.balance_sheet
    x = msft.quarterly_balance_sheet
    df = pd.read_csv(x)
    print(df)
    df.to_csv('AAPL.csv')


def data_read():
    yf.pdr_override()
    data = pdr.get_data_yahoo("msft", start="2022-01-01", end="2022-03-22")
    print(data)


def multiple_action():
    tickers = yf.Tickers('msft aapl goog')

    print(tickers.tickers.AAPL.history(period="1mo"))


def deneme():
    tesla = yf.Ticker('tsla')
    historical_data_tesla =tesla.history()
    print('Historical data')
    print(historical_data_tesla.head())


if __name__ == '__main__':
    # balance_3()
    # data_read()
    # multiple_action()
    deneme()
