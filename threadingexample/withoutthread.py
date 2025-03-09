
import time

def is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if n == 1 or n == 0:
        is_prime = False
    return is_prime

time1 = time.time()
l = []
for i in range(1, 100000):
    if is_prime(i):
        l.append(i)
time2 = time.time()
time_taken_ms = (time2 - time1)
print('Time taken for', len(l), 'prime numbers is', time_taken_ms, 'seconds')