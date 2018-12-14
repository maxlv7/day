# 事件循环+回调（驱动生成器）+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted（scrapy， django channels）
# torando(实现web服务器)， django+flask(uwsgi, gunicorn+nginx)
# tornado可以直接部署， nginx+tornado

import asyncio

async def get_html():
    print("start")
    await asyncio.sleep(2)
    print('end')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [get_html() for x in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))