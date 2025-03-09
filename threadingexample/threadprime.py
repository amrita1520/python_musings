import time
import threading
def is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if n == 1 or n == 0:
        is_prime = False
    return is_prime
def prime_range(l,r):
    ans=[]
    for i in range(l,r+1):
        if is_prime(i):
            ans.append(i)
time1 = time.time()
t1=threading.Thread(target=prime_range,args=(1,50001))
t1.start()
t1.join()
t2=threading.Thread(target=prime_range,args=(50000,100001))
t2.start()
t2.join()
time2 = time.time()
time_taken_ms = (time2 - time1)

print('Time taken for', 'prime numbers is', time_taken_ms, 'seconds')