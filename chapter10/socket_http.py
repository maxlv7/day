from urllib.parse import urlparse
import socket


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path

    if path == "":
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except:
        pass
    # 不停询问连接是否建立好
    # 做计算任务，再次发起其它的连接请求
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b''
    while True:
        d = client.recv(1)
        if d:
            data += d
        else:
            break
    print(data.decode())


if __name__ == '__main__':
    get_url("http://www.my.com")
