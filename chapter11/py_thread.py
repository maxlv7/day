import time
import threading


def get_html(url):
    print('get_html start!')
    time.sleep(2)
    print('get_html end!')

def get_url(url):
    print('get_url start!')
    time.sleep(2)
    print('get_url end!')

if __name__ == '__main__':
    thread1 = threading.Thread(target=get_html,args=('',))
    thread2 = threading.Thread(target=get_url,args=('',))
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start = time.time()
    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()
    print(time.time()-start)

    # 继承thread类实现多线程