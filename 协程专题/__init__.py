def test():
    print("test")
    r = yield 5
    print(r)
    return "11111"
def test1():
    print("test1")
    r = yield from test()
    return r
cor = test1()
print(cor.send(None))
try:
    cor.send(666)
except StopIteration as e:
    print(e.value)