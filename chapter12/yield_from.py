def g1():
    b = yield 1
    print(b)
    yield 2
    yield 3

def g2():
    yield from g1()

g =g2()
print(g.send(None))
print(g.send(123))
# print(g.send(None))
# print(g.send(None))