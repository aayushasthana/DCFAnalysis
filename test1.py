import yfinance as yf

# Example: Get financial data for a company
ticker = 'AAPL'
stock = yf.Ticker(ticker)
financials = stock.financials
balance_sheet = stock.balance_sheet
cashflow = stock.cashflow
#print(balance_sheet)

# Example UFCF calculation

EBIT = financials.loc['EBIT'].mean()  # Average EBIT
tax_rate = 0.21  # Assume a 21% tax rate
depreciation = cashflow.loc['Depreciation And Amortization'].mean()
capex = cashflow.loc['Capital Expenditure'].mean()

current_assets = balance_sheet.loc['Cash And Cash Equivalents'] + balance_sheet.loc['Other Short Term Investments']
# For now, without current liabilities, we'll use only current assets as an approximation
working_capital = current_assets  # Subtract current liabilities if available
change_in_working_capital = working_capital.diff().mean()  # Calculate the period-to-period change

UFCF = EBIT * (1 - tax_rate) + depreciation - capex - change_in_working_capital
print(UFCF)