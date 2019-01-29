import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# select + simple asyncio
selector = DefaultSelector()
stop = False


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


class Crawler():
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        try:
            sock.connect(('baidu.com', 80))
        except BlockingIOError:
            pass
        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield f
        # 已经三次握手成功
        selector.unregister(sock.fileno())
        get = 'GET {0} HTTP/1.0\r\nHost: baidu.com\r\n\r\n'.format(self.url).encode()
        sock.send(get)

        global stop
        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(1024))

            selector.register(sock.fileno(), EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                print(self.response)
                stop = True
                break


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
    Task(fetcher.fetch())
    loop()
    print(time.time() - start_time)
