from binance.exceptions import BinanceAPIException, BinanceRequestException

def place_order(client, logger, symbol, side, order_type, quantity, price):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logger.info(f"SENT REQUEST: {params}")

    try:
        response = client.futures_create_order(**params)
        logger.info(f"RECEIVED RESPONSE: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"BINANCE API ERROR: {e.message}")
        raise

    except BinanceRequestException as e:
        logger.error(f"NETWORK ERROR: {str(e)}")
        raise
