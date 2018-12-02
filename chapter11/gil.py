# gil global interpreter lock （cpython）
# python中一个线程对应于c语言中的一个线程
# gil使得同一个时刻只有一个线程在一个cpu上执行字节码, 无法将多个线程映射到多个cpu上执行

import dis,threading
from threading import Lock


lock = Lock()
x = 0

def add():
    global x
    for x in range(1000000):
        lock.acquire()
        x = x+1
        lock.release()

def desc():
    global x
    for x in range(500):
        x = x-1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(x)