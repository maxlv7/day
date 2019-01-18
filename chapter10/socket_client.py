import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8000))

while 1:
    data = input(":")
    client.send(data.encode())
    # print(client.recv(1024).decode())
