def currency(fn):
    def wrapper(*args):
        result = fn(*args)
        return f'${result}'
    return wrapper
 
@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)
 
 
print(net_price(100, 0.05))