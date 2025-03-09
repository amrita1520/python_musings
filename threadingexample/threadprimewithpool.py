import time
import math
import concurrent.futures
import threading
# Shared global counter
num = 1
lock = threading.Lock()
primes = []

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Optimized to check up to √n
        if n % i == 0:
            return False
    return True

def prime_worker(max_num):
    """Thread worker function to check primes using a global counter."""
    global num
    local_primes = []  # Use a local list to reduce lock contention

    while True:
        with lock:  # Ensure only one thread modifies num at a time
            if num > max_num:
                break  # Stop when all numbers are processed
            current = num
            num += 1  # Increment global counter

        if is_prime(current):
            local_primes.append(current)

    # Append results outside lock to minimize contention
    with lock:
        primes.extend(local_primes)

# Configuration
NUM_THREADS = 4  # Number of worker threads
MAX_NUMBER = 100000  # Range limit

# Start measuring time
start_time = time.time()

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = [executor.submit(prime_worker, MAX_NUMBER) for _ in range(NUM_THREADS)]

# Wait for all threads to finish
concurrent.futures.wait(futures)

# End time
end_time = time.time()

print(f"Total prime numbers found: {len(primes)}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
