import yfinance as yf

# Example: Get financial data for a company
ticker = 'AAPL'
stock = yf.Ticker(ticker)
financials = stock.financials
balance_sheet = stock.balance_sheet
cashflow = stock.cashflow
print(cashflow)
#hi i'm caroline