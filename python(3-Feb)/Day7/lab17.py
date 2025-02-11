#The time Module
import time

print("Current time in seconds since epoch:", time.time())
print("Current local time:", time.ctime())
print("Sleep for 2 seconds...")
time.sleep(2)
print("Woke up!")