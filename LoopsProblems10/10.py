#10. Exponential Backoff
#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1
max_try = 5
attempts = 0

while attempts < max_try:
    print("Attempts" , attempts + 1 , "- wait time " , wait_time )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1