import concurrent.futures
import time

def worker(n):
    """Simulate a simple task"""
    time.sleep(10)  # Simulating some work
    return f"Task {n} completed"

def worker2(n):
    """Simulate a simple task2"""
    time.sleep(10)  # Simulating some work
    return f"Task2 {n} completed"

# Number of worker threads
NUM_THREADS = 4

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    # Submit multiple tasks
    jobs = [executor.submit(worker, i) for i in range(1, 5)]
    print("Tasks submitted")
    print(jobs)
    # Retrieve results as they complete
    for future in concurrent.futures.as_completed(jobs):
        print(future.result())

print("All tasks completed!")
