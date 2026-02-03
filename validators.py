def validate_order(symbol, side, order_type, quantity, price):
    if not symbol.isupper():
        raise ValueError("Symbol must be uppercase (e.g., BTCUSDT)")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures supported")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")
