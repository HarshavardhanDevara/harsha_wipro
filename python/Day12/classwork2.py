def currency_formatter(currency="USD"):

    symbols = {

        "USD": "$",

        "EUR": "€",

        "INR": "₹",

        "GBP": "£",

        "JPY": "¥"

    }

    def decorator(func):

        def wrapper(*args ):

            amount = func(*args)

            symbol = symbols.get(currency)

            return f"{symbol}{amount:,.2f} {currency}"

        return wrapper

    return decorator

# Usage examples

@currency_formatter("USD")

def get_price_usd():

    return 1000.50

@currency_formatter("INR")

def get_price_inr():

    return 85000

@currency_formatter("EUR")

def get_price_eur():

    return 1200.75

print(get_price_usd())  # Output: $1,000.50 USD

print(get_price_inr())  # Output: ₹85,000.00 INR

print(get_price_eur())  # Output: €1,200.75 EUR
 