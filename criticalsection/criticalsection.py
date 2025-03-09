import threading
lock = threading.Lock()
counter=0
def increment():
    global counter
    print('hello')
    with lock:
        counter+=1
def decrement():
    global counter
    print('hello2')
    with lock:
        counter-=1
for i in range(10000):
    t1=threading.Thread(target=increment)
    t2=threading.Thread(target=decrement)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
print(counter)