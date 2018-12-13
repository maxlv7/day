
# 生成器也可以接收值
def gen_fun():
    a = yield 1
    print(a)
    yield 2
    yield 3


a = gen_fun()
print(next(a))
a.send("testestes")
print(next(a))