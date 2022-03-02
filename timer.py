#!/usr/bin/env python3
# Timer

import time #to important the standard library

start_time = time.localtime()
print(f"Timer staretd at {time.strftime('%X', start_time)}")

# Wait for user tos top timer
input("Press 'Enter' to stop timer")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
