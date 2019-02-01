from urllib.parse import urlparse
import socket
import asyncio


async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path

    if path == "":
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    print('------------')
    reader, writer = await asyncio.open_connection(host,5000)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    lines = []
    async for line in reader:
        data = line.decode()
        lines.append(data)
    return lines




if __name__ == '__main__':
    tasks = [asyncio.ensure_future(get_url('http://localhost/test')) for x in range(50)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    # for task1 in asyncio.Task.all_tasks():
    #     # print(task)
    #     print(task1.result()[:1])