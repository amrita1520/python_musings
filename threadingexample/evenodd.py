import time
import threading

def is_even(n):
    return n % 2 == 0

def even_odd_range(l, r):
    evens = []
    odds = []
    for i in range(l, r + 1):
        if is_even(i):
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds

time1 = time.time()
num = 100000000
t1 = threading.Thread(target=even_odd_range, args=(1, num // 5))
t1.start()
t2 = threading.Thread(target=even_odd_range, args=(num // 5 + 1, num // 5 * 2))
t2.start()
t3 = threading.Thread(target=even_odd_range, args=(num // 5 * 2 + 1, num // 5 * 3))
t3.start()
t4 = threading.Thread(target=even_odd_range, args=(num // 5 * 3 + 1, num // 5 * 4))
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()

time2 = time.time()
time_taken_ms = (time2 - time1)

print('Time taken for', 'even and odd numbers is', time_taken_ms, 'seconds')