import argparse
from bot.validators import validate
from bot.orders import place_order
from bot.logging_config import logger
p=argparse.ArgumentParser()
p.add_argument("--symbol",required=True)
p.add_argument("--side",required=True)
p.add_argument("--type",required=True)
p.add_argument("--quantity",type=float,required=True)
p.add_argument("--price",type=float)
a=p.parse_args()
try:
    side,otype=validate(a.side,a.type,a.price)
    print("ORDER REQUEST",a.symbol,side,otype,a.quantity,a.price)
    res=place_order(a.symbol,side,otype,a.quantity,a.price)
    logger.info(res)
    print(res)
except Exception as e:
    logger.exception(e)
    print("FAILED:",e)
