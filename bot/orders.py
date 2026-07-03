from .client import signed_request
def place_order(symbol,side,otype,qty,price=None):
    p={"symbol":symbol.upper(),"side":side,"type":otype,"quantity":qty}
    if otype=="LIMIT":
        p["price"]=price
        p["timeInForce"]="GTC"
    return signed_request("POST","/fapi/v1/order",p)
