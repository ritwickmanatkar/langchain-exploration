import yfinance as yf

if __name__ == '__main__':
    data = yf.download(tickers=['CRM', 'MSFT'], start="2012-03-11", end='2024-07-10')
    print(data.head(10))
