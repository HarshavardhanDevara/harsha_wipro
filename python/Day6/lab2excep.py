class TooManyPizzasError(Exception):
      pass
 
def order_pizza(number):
    if number > 100:
        raise TooManyPizzasError("That's too many pizzas to handle!")

 
try:
    order_pizza(101)
except TooManyPizzasError as e:
    print(f"Order failed: {e}")