import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# select + simple asyncio
selector = DefaultSelector()
stop = False


def connect(sock,address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        # 驱动协程执行
        f.set_result(None)

    selector.register(sock.fileno(), EVENT_WRITE, on_connected)
    yield from f
    selector.unregister(sock.fileno())

def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(),EVENT_READ,on_readable)
    chunk = yield from f
    selector.unregister(sock.fileno())
    return chunk

def read_all(sock):
    res = []
    chunk = yield from read(sock)
    while chunk:
        res.append(chunk)
        chunk = yield from read(sock)

    return b''.join(res)

# 未来对象，用来保存回调的结果
class Future():
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        # print(self._callbacks)
        self.result = result
        for f in self._callbacks:
            print("call f..."+f.__name__)
            print(self)
            f(self)

    def __iter__(self):
        yield self
        return self.result


class Crawler():
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        global stop
        sock = socket.socket()
        yield from connect(sock,('baidu.com', 80))
        get = 'GET {0} HTTP/1.0\r\nHost: baidu.com\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))
        self.response = yield from read_all(sock)
        stop = True


class Task():
    def __init__(self, cor):
        self.cor = cor
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        print(future)
        try:
            # 返回一个Future实例对象
            # 启动fetch
            next_future = self.cor.send(future.result)
            print(11111111)
        except StopIteration as e:
            print(e)
            return
        print(2222222222)
        next_future.add_done_callback(self.step)


def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    # 1. select本身是不支持register模式
    # 2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        print('----------')
        events = selector.select()
        for key, mask in events:
            print(key)
            # print(events)
            call_back = key.data
            call_back()
    # 回调+事件循环+select(poll\epoll)


if __name__ == "__main__":
    import time

    start_time = time.time()
    fetcher = Crawler('/')
    a = Task(fetcher.fetch())
    loop()
    print(fetcher.response)
    print(time.time() - start_time)
