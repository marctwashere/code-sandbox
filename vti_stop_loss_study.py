import yfinance as yf
import pandas as pd

# Download VTI stock data for the last 10 years
ticker = 'VTI'
data = yf.download(ticker, period='10y', interval='1d')

# Initialize variables for trailing stop loss calculation
stop_loss_percentage = 0.15
max_price = 0
trigger_count = 0
stop_loss_price = 0

# Iterate through the stock data
for index, row in data.iterrows():
    current_price = row['Close']
    
    # Update the maximum price seen so far
    if current_price > max_price:
        max_price = current_price
        stop_loss_price = max_price * (1 - stop_loss_percentage)
    
    # Check if the current price triggers the trailing stop loss
    if current_price < stop_loss_price:
        trigger_count += 1
        print('Triggered:')
        print(row)
        # After a trigger, we reset the max_price to the current price
        max_price = current_price
        stop_loss_price = max_price * (1 - stop_loss_percentage)

# Output the result
print(f'Trailing stop loss order was triggered {trigger_count} times in the last 10 years for {ticker}.')