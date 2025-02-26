from functools import lru_cache
 
@lru_cache(maxsize=128)
def expensive_function(x):
    print(f"Computing {x}...")
    return x * x  # Simulate expensive computation
 
print(expensive_function(4))  # Computed
print(expensive_function(4))  # Cached
 