import asyncio


async def get_url():
    print('get url...')
    await asyncio.sleep(5)
    await parse_html()


async def parse_html():
    print('parse html...')
    await save()


async def init_url():
    print('init url')
    await get_url()


async def save():
    print('save')
    pass


async def main():
    print('wait for pool...')
    await asyncio.sleep(3)
    await init_url()

async def test():
    await asyncio.sleep(20)
    print("3333333")
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(main()) for x in range(1)]
    loop.run_until_complete(asyncio.wait([*tasks, asyncio.ensure_future(test())]))
