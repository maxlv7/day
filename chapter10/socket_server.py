import socket
from threading import Thread
# tcp
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))

server.listen()


def handle(sock):
    while 1:
        data = sock.recv(1024)
        # sock.send("test".encode())
        print(data.decode('utf8'))
        if data.decode() == 'exit':
            sock.close()
# 一次获取1k的数据
# recv是系统调用
while 1:
    sock, addr = server.accept()
    print("addr..",addr)
    c_thread = Thread(target=handle,args=(sock,))
    c_thread.start()
