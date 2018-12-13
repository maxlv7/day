
# 生成器也可以接收值
def gen_fun():
    a = yield 1
    print(a)
    yield 2
    yield 3


# a = gen_fun()
# print(next(a))
# a.close()
# print(next(a))

def g1(iter):
    yield iter

def g2(item):
    yield from item

# for x in g1(range(10)):
#     print(x)

# for x in g2(range(10)):
#     print(x)


a= g2(range(10))
print((next(a)))
print((next(a)))
print((next(a)))
print((next(a)))
print((next(a)))