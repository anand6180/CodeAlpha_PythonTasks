def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "MSFT": 300
    }

    portfolio = {}
    total_investment = 0

    print("📈 Stock Portfolio Tracker")
    print("Available stocks:", list(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock in stock_prices:
            qty = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = qty
        else:
            print("❌ Stock not found!")

    print("\n🧾 Portfolio Summary:")
    with open("portfolio_summary.txt", "w") as file:
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            total_investment += value
            line = f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}"
            print(line)
            file.write(line + "\n")

        total_line = f"\nTotal Investment: ${total_investment}"
        print(total_line)
        file.write(total_line)

stock_portfolio_tracker()
