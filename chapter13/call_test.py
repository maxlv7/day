# call_soon call_later call_at call_soon_threadsafe

import asyncio

def callback(time):
    print("Now time:"+str(time))

def stop(loop):
    print("loop...")
    loop.stop()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.call_soon(callback,3)
    loop.call_soon(stop,loop)
    loop.call_later(3,callback,3)
    loop.call_later(2,callback,2)
    loop.call_later(1,callback,1)
    # loop.call_soon(stop,loop)
    loop.run_forever()

    # call_later 内部调用了call_at
    #