def outer():
  print("I'm the outer function.")
  def inner():
    print("And I'm the inner function.")
  inner()
outer()
