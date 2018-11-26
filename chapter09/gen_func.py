# 什么是生成器函数 只要函数里面有yield关键字

def gen_func():
    yield 1
    yield range(10)


if __name__ == '__main__':
    gen = gen_func()
    for x in gen:
        print(x)