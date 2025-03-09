import time
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
num=100000000
even_odd_range(1, num)
time2 = time.time()
time_taken_ms = (time2 - time1)

print('Time taken for', 'even and odd numbers is', time_taken_ms, 'seconds')