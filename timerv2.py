#!/usr/bin/env python3
# chapter7.4: Timer

#import time
from time import localtime, mktime, strftime # to import and call the standard library function directly

start_time = localtime()
print(f"Timer staretd at {strftime('%X', start_time)}")

# Wait for user tos top timer
input("Press 'Enter' to stop timer")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
