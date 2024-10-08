import yfinance as yf

# Example: Get financial data for a company
ticker = 'AAPL'
stock = yf.Ticker(ticker)
financials = stock.financials
balance_sheet = stock.balance_sheet
cashflow = stock.cashflow


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

# Example: Project UFCF for 5 years
growth_rate = 0.05  # Assume 5% growth
forecast_period = 5
projected_fcfs = [UFCF * (1 + growth_rate)**i for i in range(1, forecast_period + 1)]

# Terminal Value
terminal_growth_rate = 0.03  # Assume 3% perpetual growth
discount_rate = 0.112  #11.2% discount rate
terminal_value = projected_fcfs[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
print(terminal_value)
