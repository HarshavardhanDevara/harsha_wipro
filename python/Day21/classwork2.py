from cachetools import TTLCache
 
cache = TTLCache(maxsize=100, ttl=10)  # 100 items, expires in 10 seconds
 
def get_cached_value(key):
    return cache.get(key, "Not Found")
 
cache["data"] = "Cached Result"
print(get_cached_value("data"))  # Cached Result
 