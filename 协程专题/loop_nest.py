import asyncio


async def get_html(t):
    print('START... {}'.format(t))
    await asyncio.sleep(t)
    print('END...for {}'.format(t))


def callback(future):
    print(dir(future))
    future._loop.stop()
    print("send...")


if __name__ == '__main__':
    print(__package__)
    # 取消task
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(3)
    tasks = [task1, task2, task3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        all = asyncio.Task.all_tasks()
        print(len(all))
        for task in all:
            print("cancel:",end='')
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()