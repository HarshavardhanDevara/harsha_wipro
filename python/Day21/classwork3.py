from diskcache import Cache
 
# cache = Cache("./cache_dir")  # Disk-based cache
cache = Cache(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day21/cache_dir")  # Disk-based cache
 
cache["key"] = "Persistent Value"
 
print(cache["key"])  # "Persistent Value"
 