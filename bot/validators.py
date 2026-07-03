def validate(side,otype,price):
    side=side.upper(); otype=otype.upper()
    if side not in ("BUY","SELL"): raise ValueError("Invalid side")
    if otype not in ("MARKET","LIMIT"): raise ValueError("Invalid order type")
    if otype=="LIMIT" and price is None: raise ValueError("LIMIT requires price")
    return side,otype
