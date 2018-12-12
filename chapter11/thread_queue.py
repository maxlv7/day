# 线程间通信
# 通过queue
import random,time
def get(queue):
    while True:
        try:
            x = queue.get(timeout=1)
            print(x)
        except:
            print("正在获取中~~~")
def send(queue):
    while True:
        queue.put(random.randint(1,100),timeout=1)
        time.sleep(2)
# get一直读取queue之间是否有东西，如果有的话就把它取出来
# send一直向queue之中放东西
# get 和 send的速度不一样

import queue
from threading import Thread
que = queue.Queue(maxsize=1000)
t1 = Thread(target=get,args=(que,))
t2 = Thread(target=send,args=(que,))
t1.start()
t2.start()
t1.join()
t2.join()
print("start...")
