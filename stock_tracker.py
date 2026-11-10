STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
}


def track_portfolio():
    portfolio = {}
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and sample prices (USD):")

    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")

    print("\nEnter a stock symbol and quantity. Type 'done' to finish.")

    while True:
        symbol = input("\nStock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Stock not found. Choose a symbol from the list.")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a valid whole-number quantity.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("\nNo stocks were entered.")
        return

    print("\n=== PORTFOLIO SUMMARY ===")
    total_investment = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_investment += value
        print(f"{symbol}: {quantity} x ${price:.2f} = ${value:.2f}")

    print(f"\nTotal investment: ${total_investment:.2f}")

    save = input("Save this summary to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")
            for symbol, quantity in portfolio.items():
                value = STOCK_PRICES[symbol] * quantity
                file.write(f"{symbol}: {quantity} shares = ${value:.2f}\n")
            file.write(f"Total investment: ${total_investment:.2f}\n")
        print("Summary saved to portfolio.txt.")


if __name__ == "__main__":
    track_portfolio()
