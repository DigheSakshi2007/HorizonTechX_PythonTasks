def stock_portfolio():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 310,
        "AMZN": 130
    }
    print("--- Available Stocks and Prices per share ---")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    total_investment = 0
    portfolio_details = []
    print("\nEnter your stocks (type 'done' when finished):")
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock_name == 'DONE':
            break  
        if stock_name not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
        except ValueError:
            print("Please enter a valid numeric quantity.")
            continue
        item_value = stock_prices[stock_name] * quantity
        total_investment += item_value
        portfolio_details.append(f"{stock_name}: {quantity} shares x ${stock_prices[stock_name]} = ${item_value}")
    print("\n--- Portfolio Summary ---")
    for detail in portfolio_details:
        print(detail)
    print(f"\nTotal Investment Value: ${total_investment}")
    save_option = input("\nDo you want to save this to a file? (yes/no): ").lower()
    if save_option == 'yes':
        with open("portfolio_report.txt", "w") as f:
            f.write("--- Portfolio Summary ---\n")
            for detail in portfolio_details:
                f.write(detail + "\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Report saved successfully as 'portfolio_report.txt'!")
if __name__ == "__main__":
    stock_portfolio()