# Getting the Formatted Time
import time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Formatted time:", formatted_time)