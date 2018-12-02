import threading
from threading import Lock,RLock

# 锁会引响性能
# lock = Lock()
lock = RLock()
t = 0

def add():
    global t
    for x in range(1000000):
        lock.acquire()
        lock.acquire()
        t = t+1
        lock.release()
        lock.release()

def desc():
    global t
    for x in range(1000000):
        lock.acquire()
        t = t-1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(t)