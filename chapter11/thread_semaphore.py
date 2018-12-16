# Semaphore 是用于控制进入数量的锁
# 文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个
# 线程同步 用信号量来实现

import threading
from threading import Semaphore
import time

class Spider(threading.Thread):

    def __init__(self,sem):
        super(Spider, self).__init__()
        self.sem = sem

    def run(self):

        time.sleep(2)
        print('spider...')
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for x in range(20):
            self.sem.acquire()
            t = Spider(self.sem)
            t.start()

if __name__ == '__main__':
    sem = Semaphore(5)
    url_pro = UrlProducer(sem)
    url_pro.start()