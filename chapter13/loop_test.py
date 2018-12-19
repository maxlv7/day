# 事件循环+回调（驱动生成器）+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted（scrapy， django channels）
# torando(实现web服务器)， django+flask(uwsgi, gunicorn+nginx)
# tornado可以直接部署， nginx+tornado


# 基本使用
import asyncio

async def get_html():
    print("start")
    await asyncio.sleep(2)
    return "li"

def callback(future):
    print("send email!")

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [get_html() for x in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))

# 获取协程的返回值
# loop = asyncio.get_event_loop()
# task = loop.create_task(get_html())
# task.add_done_callback(callback)
# loop.run_until_complete(task)
# print(task.result())

async def com(x,y):
    import math
    return math.pow(x,y)

async def compute(x, y):
    print("Compute %s & %s ..." % (x, y))
    res = await com(x,y)
    return res

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s  %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(2, 10))
loop.close()