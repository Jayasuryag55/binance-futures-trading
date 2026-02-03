import argparse
from bot.client import get_authenticated_client
from bot.orders import place_order
from bot.validators import validate
from bot.logging_config import setup_logger

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()
logger = setup_logger()

validate(args.symbol, args.side, args.type, args.quantity, args.price)
client = get_authenticated_client()

params = {
    "symbol": args.symbol,
    "side": args.side,
    "type": args.type,
    "quantity": args.quantity
}
if args.type == "LIMIT":
    params["price"] = args.price
    params["timeInForce"] = "GTC"

response = place_order(client, logger, params)
print(response)
