import asyncio
import time
from functools import partial


async def get_html(url):
    print('START...')
    await asyncio.sleep(0.2)
    print('END...')
    return "test"


def callback(future):
    print(dir(future))
    future._loop.stop()
    print("send...")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # task = asyncio.ensure_future(get_html(2))
    # task.add_done_callback(partial(callback, "baidu.com"))
    tasks = [get_html(2) for x in range(5)]
    tasks2 = [get_html(2) for x in range(5)]
    # wait 和 gather的区别
    # 使用wait
    # loop.run_until_complete(asyncio.wait([*tasks]))
    group1 = asyncio.gather(*tasks)
    group2 = asyncio.gather(*tasks2)
    group2.add_done_callback(callback)
    loop.run_until_complete(asyncio.gather(*[group1, group2]))
    # print(task.result())
